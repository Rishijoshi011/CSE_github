from flask import Flask, redirect, request, session, url_for, Response
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from model import build_model, get_recommendations
from visualize import plot_clusters
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
    return '<a href="/login">Login to Spotify</a>'

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
    return redirect(url_for('create_playlist'))  # Start with playlist creation

# Playlist creation + behind-the-scenes analysis
@app.route('/create_playlist')
def create_playlist():
    token_info = session.get('token_info', None)
    if token_info:
        access_token = refresh_token_if_needed()  # Refresh token if needed
        if access_token:
            sp = spotipy.Spotify(auth=access_token)
            top_tracks = sp.current_user_top_tracks(limit=50, time_range='long_term')  # Get top 50 tracks
            track_ids = [track['id'] for track in top_tracks['items']]  # Get track IDs
            user = sp.current_user()  # Get user details

            # Create the playlist for the user
            playlist = sp.user_playlist_create(user['id'], 'Splaylist Playlist', public=True)
            sp.playlist_add_items(playlist['id'], track_ids)  # Add top tracks to the playlist

            # Return response with the link to the playlist
            return f"✅ Playlist created! <br><a href='{playlist['external_urls']['spotify']}' target='_blank'>🎵 Listen on Spotify</a>"
        else:
            return "❌ Token expired. Please login again."
    return "❌ Please login first."

# Protected route for analysis (for your debugging purposes)
@app.route('/analyze')
@requires_auth
def analyze():
    token_info = session.get('token_info', None)
    if token_info:
        access_token = refresh_token_if_needed()  # Refresh token if needed
        if access_token:
            sp = spotipy.Spotify(auth=access_token)
            top_tracks = sp.current_user_top_tracks(limit=50, time_range='long_term')  # Get top 50 tracks
            track_ids = [track['id'] for track in top_tracks['items']]  # Get track IDs

            # Fetch audio features for the top tracks in chunks
            features = get_audio_features_filtered(sp, track_ids, chunk_size=20)
            selected_features = [
                {k: f[k] for k in ['energy', 'valence', 'tempo', 'danceability']}
                for f in features if f
            ]

            if not selected_features:
                return "⚠️ No audio features could be retrieved for analysis."

            try:
                df, model = build_model(selected_features)
            except Exception as e:
                print("Error in build_model:", e)
                return f"Error during model building: {e}"

            # Save analysis to CSV with timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            df.to_csv(f"music_analysis_{timestamp}.csv", index=False)
            try:
                image_path = plot_clusters(df)
            except Exception as e:
                print("Error in plot_clusters:", e)
                return f"Error during cluster visualization: {e}"

            return f"<h2>Analysis Done!</h2><p>CSV saved as <b>music_analysis_{timestamp}.csv</b></p><img src='/{image_path}' />"
        return "❌ Token expired. Please login again."
    return "Please login first."

if __name__ == '__main__':
    app.run(debug=True, port=8080)
