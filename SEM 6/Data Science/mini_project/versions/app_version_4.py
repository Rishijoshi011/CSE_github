from flask import Flask, redirect, request, session, url_for, Response
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from functools import wraps
import pandas as pd
import requests

app = Flask(__name__)
app.secret_key = '974d0cf178894c9ebf71ad2814ffc592'

sp_oauth = SpotifyOAuth(
    client_id='cc89a5c9ddfb430c9bf6ec1971462dde',
    client_secret='974d0cf178894c9ebf71ad2814ffc592',
    redirect_uri='http://127.0.0.1:8080/callback',
    scope="user-library-read user-top-read playlist-modify-public"
)

# Basic Auth
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

# Token refresh
def refresh_token_if_needed():
    token_info = session.get('token_info', None)
    if token_info:
        if sp_oauth.is_token_expired(token_info):
            token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])
            session['token_info'] = token_info
        return token_info['access_token']
    return None

@app.route('/')
def home():
    return '''
        <h2>Splaylist - Group Music Taste</h2>
        <a href="/login">Login to Spotify</a><br>
        <a href="/logout">Logout</a><br>
        <a href="/add_user">Add another user</a><br>
        <a href="/create_playlist">Create Playlist</a>
    '''
# Function to revoke the Spotify access token
def revoke_spotify_token(token):
    url = f'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    data = {
        'token': token
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return True
    else:
        return False
@app.route('/logout')
def logout():
    # Get the current token from the session
    token_info = session.get('token_info', None)
    
    if token_info:
        access_token = token_info.get('access_token')
        
        # Revoke the token from Spotify
        revoke_spotify_token(access_token)
    
    # Clear the session to remove all stored data
    session.clear()

    return redirect('http://127.0.0.1:8080/')

@app.route('/login')
def login():
    return redirect(sp_oauth.get_authorize_url())  # Redirect to Spotify's login page

@app.route('/callback')
def callback():
    code = request.args.get('code')
    token_info = sp_oauth.get_cached_token()
    if not token_info:
        token_info = sp_oauth.get_access_token(code, as_dict=True)
    session['token_info'] = token_info
    return redirect(url_for('add_user'))  # After login, go to add user page

@app.route('/add_user')
def add_user():
    # Ensure the user is logged in first
    token_info = session.get('token_info', None)
    if not token_info:
        return redirect('/login')  # If no token, ask for login again

    access_token = refresh_token_if_needed()
    if access_token:
        sp = spotipy.Spotify(auth=access_token)
        top_tracks = sp.current_user_top_tracks(limit=50, time_range='long_term')
        user = sp.current_user()

        track_data = []
        for track in top_tracks['items']:
            artist_id = track['artists'][0]['id']
            artist_name = track['artists'][0]['name']
            genre_list = []

            try:
                artist_info = sp.artist(artist_id)
                genre_list = artist_info.get('genres', [])
            except:
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
        file_name = 'user_music_data.csv'

        try:
            df.to_csv(file_name, mode='a', header=not pd.io.common.file_exists(file_name), index=False)
        except Exception as e:
            print(f"❌ Error saving to CSV: {e}")

        # Track user in session
        if 'users' not in session:
            session['users'] = []
        session['users'].append({
            'id': user['id'],
            'name': user['display_name'],
            'top_tracks': [track['id'] for track in top_tracks['items']]
        })

        return f'''
            <h3>✅ User Added: {user["display_name"]}</h3>
            <a href="/logout">Logout & Add Next User</a><br>
            <a href="/create_playlist">Create Playlist</a>
        '''
    else:
        return "❌ Token expired. Please login again."

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
            sp.playlist_add_items(playlist['id'], all_track_ids[:100])  # Limit to 100 to avoid rate limit

            return f"✅ Playlist created!<br><a href='{playlist['external_urls']['spotify']}' target='_blank'>🎵 Open Spotify Playlist</a>"
        else:
            return "❌ Token expired. Please login again."
    return "❌ Please login first."

if __name__ == '__main__':
    app.run(debug=True, port=8080)
