import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, redirect, request, session, url_for
from spotipy.exceptions import SpotifyException

app = Flask(__name__)

# Set your credentials here
CLIENT_ID = 'cc89a5c9ddfb430c9bf6ec1971462dde'
CLIENT_SECRET = '974d0cf178894c9ebf71ad2814ffc592'
REDIRECT_URI = 'http://127.0.0.1:8080/callback'

# Set up the spotipy instance with OAuth
sp_oauth = SpotifyOAuth(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, scope="user-library-read user-top-read playlist-modify-public")

app.secret_key = '974d0cf178894c9ebf71ad2814ffc592'

# Home route: Display a link to log in to Spotify
@app.route('/')
def home():
    return '<a href="/login">Login to Spotify</a>'

# Login route: Redirects to Spotify login page
@app.route('/login')
def login():
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

# Callback route: Spotify redirects here after user logs in
@app.route('/callback')
def callback():
    token_info = sp_oauth.get_access_token(request.args['code'])
    session['token_info'] = token_info
    return redirect(url_for('create_playlist'))

# Function to handle retry on rate-limited requests
def handle_rate_limit_error(e, retries=3, delay=5):
    """Handles rate-limiting error and retries the request."""
    if e.http_status == 429:  # Rate limit error
        print(f"Rate limit hit, retrying after {delay} seconds...")
        time.sleep(delay)  # Wait before retrying
        if retries > 0:
            return True
    return False

# Playlist creation route
@app.route('/create_playlist')
def create_playlist():
    token_info = session.get('token_info', None)
    if token_info:
        sp = spotipy.Spotify(auth=token_info['access_token'])
        retries = 3
        delay = 5

        try:
            # Fetch user's top tracks (you can modify this to use more features)
            top_tracks = sp.current_user_top_tracks(limit=50, time_range='long_term')

            # Collect track IDs
            track_ids = [track['id'] for track in top_tracks['items']]

            # Create playlist
            user = sp.current_user()
            playlist = sp.user_playlist_create(user['id'], 'Splaylist Playlist', public=True)

            # Add tracks to playlist
            sp.playlist_add_items(playlist['id'], track_ids)
            
            return f"Playlist created! Check it out: <a href='{playlist['external_urls']['spotify']}'>Your Playlist</a>"

        except SpotifyException as e:
            if handle_rate_limit_error(e, retries, delay):
                # Retry logic: decrement retries and try again
                return redirect(url_for('create_playlist'))
            else:
                return f"An error occurred: {e}"

    return "Please log in to Spotify."

if __name__ == '__main__':
    app.run(debug=True, port=8080)
    