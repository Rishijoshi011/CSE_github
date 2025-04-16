from flask import Flask, redirect, request, session, url_for, Response
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from model import build_model, build_model_from_csv
from visualize import plot_clusters, visualize_from_csv
from functools import wraps
import pandas as pd
from datetime import datetime
import time

app = Flask(__name__)

# Secret + Spotify OAuth setup
app.secret_key = '974d0cf178894c9ebf71ad2814ffc592'
sp_oauth = SpotifyOAuth(
    client_id='cc89a5c9ddfb430c9bf6ec1971462dde',
    client_secret='974d0cf178894c9ebf71ad2814ffc592',
    redirect_uri='http://127.0.0.1:8080/callback',
    scope="user-library-read user-top-read playlist-modify-public"
)

# Basic Auth for protected routes
def check_auth(username, password):
    return username == 'rishi' and password == '123'

def authenticate():
    return Response(
        'Could not verify your access level.\n'
        'Login with proper credentials.', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'}
    )

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

# Helper function: get audio features in chunks with fallback to individual requests
def get_audio_features_filtered(sp, track_ids, chunk_size=20):
    all_features = []
    for i in range(0, len(track_ids), chunk_size):
        chunk = track_ids[i:i+chunk_size]
        try:
            chunk_features = sp.audio_features(chunk)
            if chunk_features:
                valid_features = [f for f in chunk_features if f is not None]
                all_features.extend(valid_features)
        except Exception as e:
            print("Error fetching chunk, trying individual requests for chunk:", chunk, e)
            for tid in chunk:
                try:
                    feature = sp.audio_features([tid])[0]
                    if feature is not None:
                        all_features.append(feature)
                except Exception as sub_e:
                    print(f"Skipping track {tid} due to error: {sub_e}")
    return all_features

# Token refresh: refresh token if expired and return a valid access token
def refresh_token_if_needed():
    token_info = session.get('token_info', None)
    if token_info:
        if sp_oauth.is_token_expired(token_info):
            print("Token expired, refreshing...")
            token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])
            session['token_info'] = token_info
        return token_info['access_token']
    return None

# Home route
@app.route('/')
def home():
    return '''
        <a href="/login">Login to Spotify</a><br>
        <a href="/add_user">Add another user's music taste</a><br>
        <a href="/create_playlist">Create Playlist</a>
    '''

# Login route
@app.route('/login')
def login():
    return redirect(sp_oauth.get_authorize_url())

# Callback after Spotify login
@app.route('/callback')
def callback():
    code = request.args.get('code')
    token_info = sp_oauth.get_cached_token()
    if not token_info:
        token_info = sp_oauth.get_access_token(code, as_dict=True)
    session['token_info'] = token_info
    return redirect(url_for('add_user'))  # Start with adding a new user

# Add another user's music taste route
@app.route('/add_user')
def add_user():
    token_info = session.get('token_info', None)
    if token_info:
        access_token = refresh_token_if_needed()  # Refresh token if needed
        if access_token:
            sp = spotipy.Spotify(auth=access_token)
            top_tracks = sp.current_user_top_tracks(limit=50, time_range='long_term')  # Get top 50 tracks
            track_ids = [track['id'] for track in top_tracks['items']]  # Get track IDs
            user = sp.current_user()  # Get user details

            # Store user data in session for playlist creation later
            if 'users' not in session:
                session['users'] = []

            user_data = {
                'id': user['id'],
                'name': user['display_name'],
                'top_tracks': track_ids
            }
            session['users'].append(user_data)

            # Save user data to CSV file
            save_user_data_to_csv(user_data)

            # Redirect to allow adding another user or create playlist
            return '''
                <h3>User Added: {}</h3>
                <a href="/add_user">Add another user</a><br>
                <a href="/create_playlist">Create Playlist</a>
            '''.format(user['display_name'])
        else:
            return "❌ Token expired. Please login again."
    return "❌ Please login first."

# Function to save user data to CSV
def save_user_data_to_csv(user_data):
    # Prepare the data to be saved
    track_data = []
    for track_id in user_data['top_tracks']:
        track_data.append({
            'user_id': user_data['id'],
            'user_name': user_data['name'],
            'track_id': track_id
        })
    
    # Convert data to DataFrame
    df = pd.DataFrame(track_data)

    # Check if CSV file exists and append data, else create a new CSV
    file_name = 'user_music_data.csv'
    try:
        df.to_csv(file_name, mode='a', header=not pd.io.common.file_exists(file_name), index=False)
    except Exception as e:
        print(f"Error saving to CSV: {e}")

# Create Playlist route
@app.route('/create_playlist')
def create_playlist():
    if 'users' not in session or not session['users']:
        return "❌ No users added yet. Please add users first."

    token_info = session.get('token_info', None)
    if token_info:
        access_token = refresh_token_if_needed()  # Refresh token if needed
        if access_token:
            sp = spotipy.Spotify(auth=access_token)
            all_track_ids = []

            for user_data in session['users']:
                all_track_ids.extend(user_data['top_tracks'])

            user = sp.current_user()  # Get user details

            # Create the playlist for the user
            playlist = sp.user_playlist_create(user['id'], 'Splaylist Playlist', public=True)
            sp.playlist_add_items(playlist['id'], all_track_ids)  # Add all users' top tracks to the playlist

            # Return response with the link to the playlist
            return f"✅ Playlist created! <br><a href='{playlist['external_urls']['spotify']}' target='_blank'>🎵 Listen on Spotify</a>"
        else:
            return "❌ Token expired. Please login again."
    return "❌ Please login first."

if __name__ == '__main__':
    app.run(debug=True, port=8080)
