import pandas as pd
import spotipy
import time
import os
import requests
from flask import Flask, redirect, request, session, url_for, Response
from spotipy.oauth2 import SpotifyOAuth
from model import build_model, build_model_from_csv
from visualize import plot_clusters, visualize_from_csv
from functools import wraps
from datetime import datetime
from spotipy import Spotify

app = Flask(__name__)
app.secret_key = '974d0cf178894c9ebf71ad2814ffc592'

# Configure Spotify OAuth.
# (By default, Spotipy will use a cache file named ".cache" in the working directory.)
sp_oauth = SpotifyOAuth(
    client_id='cc89a5c9ddfb430c9bf6ec1971462dde',
    client_secret='974d0cf178894c9ebf71ad2814ffc592',
    redirect_uri='http://127.0.0.1:8080/callback',
    scope="user-library-read user-top-read playlist-modify-public"
)

# ==================== Basic Authentication ====================
def check_auth(username, password):
    return username == 'rishi' and password == '123'

def authenticate():
    return Response(
        'Unauthorized. Login Required.', 401,
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

# ==================== Token Refresh ====================
def refresh_token_if_needed():
    token_info = session.get('token_info', None)
    if token_info:
        if sp_oauth.is_token_expired(token_info):
            print("Token expired, refreshing...")
            token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])
            session['token_info'] = token_info  # Save refreshed token
        return token_info['access_token']
    return None

# ==================== Spotify Client Getter ====================
def get_spotify_client():
    try:
        token_info = session.get('token_info', None)
        if not token_info:
            print("[ERROR] No token info in session")
            return None
        if sp_oauth.is_token_expired(token_info):
            print("[INFO] Refreshing expired token")
            token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])
            session['token_info'] = token_info
        sp = spotipy.Spotify(auth=token_info['access_token'])
        return sp
    except Exception as e:
        print("[ERROR] Failed to get Spotify client:", e)
        return None

# ==================== Get Audio Features ====================
def get_audio_features_filtered(sp, track_ids, chunk_size=20):
    all_features = {}
    failed_track_ids = []
    for i in range(0, len(track_ids), chunk_size):
        chunk = track_ids[i:i + chunk_size]
        try:
            chunk_features = sp.audio_features(chunk)
            if chunk_features:
                for tid, feat in zip(chunk, chunk_features):
                    if feat is not None:
                        all_features[tid] = feat
                    else:
                        failed_track_ids.append(tid)
            time.sleep(0.2)  # To avoid rate limiting
        except Exception as e:
            print(f"[ERROR] Error fetching chunk {chunk}: {e}")
            failed_track_ids.extend(chunk)
    for tid in failed_track_ids:
        try:
            time.sleep(0.1)
            feat = sp.audio_features([tid])[0]
            if feat:
                all_features[tid] = feat
            else:
                print(f"[WARN] No features for track {tid}")
        except Exception as sub_e:
            print(f"[FAIL] Could not fetch {tid}: {sub_e}")
    return all_features

# ==================== Routes ====================
@app.route('/')
def home():
    return '''
        <h2>Splaylist - Group Music Taste</h2>
        <a href="/login">Login to Spotify</a><br>
        <a href="/logout">Logout</a><br>
        <a href="/add_user">Add another user</a><br>
        <a href="/create_playlist">Create Playlist</a>
    '''

# -------------------- LOGIN --------------------
@app.route('/login')
def login():
    # Delete the cache file to force a new login.
    if os.path.exists(".cache"):
        os.remove(".cache")
    session.clear()  # Clear the Flask session
    auth_url = sp_oauth.get_authorize_url() + "&show_dialog=true"
    return redirect(auth_url)

# -------------------- LOGOUT --------------------
@app.route('/logout')
def logout():
    # Optionally, delete the cache file as well.
    if os.path.exists(".cache"):
        os.remove(".cache")
    session.clear()
    return redirect('/')

# -------------------- CALLBACK --------------------
@app.route('/callback')
def callback():
    code = request.args.get('code')
    token_info = sp_oauth.get_cached_token()
    if not token_info:
        token_info = sp_oauth.get_access_token(code, as_dict=True)
    session['token_info'] = token_info
    return redirect(url_for('add_user'))  # After login, go to add user page

# -------------------- ADD ANOTHER USER --------------------
@app.route('/add_user')
def add_user():
    token_info = session.get('token_info', None)
    if not token_info:
        return redirect('/login')
    
    access_token = refresh_token_if_needed()
    if access_token:
        sp = spotipy.Spotify(auth=access_token)
        try:
            user = sp.current_user()
        except Exception as e:
            print(f"❌ Error fetching user info: {e}")
            return "❌ Failed to fetch user info."
        
        # Initialize the session 'users' list if not already
        if 'users' not in session:
            session['users'] = []
        
        # Check CSV to avoid duplicate user data
        existing_ids = set()
        file_name = 'user_music_data.csv'
        if os.path.exists(file_name):
            try:
                df_existing = pd.read_csv(file_name)
                existing_ids = set(df_existing['user_id'].unique())
            except Exception as e:
                print(f"[WARN] Could not read CSV for duplicate check: {e}")
        
        duplicate_msg = ""
        if user['id'] in existing_ids:
            duplicate_msg = f"⚠️ User {user['display_name']} is already in the CSV."

        # Get user's top tracks
        top_tracks = sp.current_user_top_tracks(limit=50, time_range='long_term')
        
        track_data = []
        for track in top_tracks['items']:
            artist_id = track['artists'][0]['id']
            artist_name = track['artists'][0]['name']
            genre_list = []
            try:
                artist_info = sp.artist(artist_id)
                genre_list = artist_info.get('genres', [])
            except Exception as e:
                genre_list = []
            track_data.append({
                'user_id': user['id'],
                'user_name': user['display_name'],
                'track_id': track['id'],
                'track_name': track['name'],
                'artist_name': artist_name,
                'popularity': track['popularity'],
                'genres': ', '.join(genre_list)
            })
        
        df = pd.DataFrame(track_data)
        try:
            df.to_csv(file_name, mode='a', header=not os.path.exists(file_name), index=False)
        except Exception as e:
            print(f"❌ Error saving to CSV: {e}")
        
        # Save user in session (avoid duplicates in the session)
        if not any(u['id'] == user['id'] for u in session.get('users', [])):
            session.setdefault('users', []).append({
                'id': user['id'],
                'name': user['display_name'],
                'top_tracks': [track['id'] for track in top_tracks['items']]
            })
        
        return f'''
            <h3>✅ User Added: {user["display_name"]}</h3>
            <p>{duplicate_msg}</p>
            <a href="/logout">Logout & Add Next User</a><br>
            <a href="/create_playlist">Create Playlist</a>
        '''
    else:
        return "❌ Token expired. Please login again."

# -------------------- CREATE PLAYLIST --------------------
@app.route('/create_playlist')
def create_playlist():
    if 'users' not in session or not session['users']:
        return "❌ No users added yet. Please add users first."
    token_info = session.get('token_info', None)
    if token_info:
        access_token = refresh_token_if_needed()
        if access_token:
            sp = spotipy.Spotify(auth=access_token)
            all_track_ids = []
            for user_data in session['users']:
                all_track_ids.extend(user_data['top_tracks'])
            user = sp.current_user()
            playlist = sp.user_playlist_create(user['id'], 'Splaylist Playlist', public=True)
            sp.playlist_add_items(playlist['id'], all_track_ids[:100])  # Limiting to 100 tracks
            return f"✅ Playlist created!<br><a href='{playlist['external_urls']['spotify']}' target='_blank'>🎵 Open Spotify Playlist</a>"
        else:
            return "❌ Token expired. Please login again."
    return "❌ Please login first."

if __name__ == '__main__':
    app.run(debug=True, port=8080)
