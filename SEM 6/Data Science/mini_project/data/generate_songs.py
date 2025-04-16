# generate_songs.py

import pandas as pd
import random
import string
import os

def generate_synthetic_data(output_file='data/synthetic_user_music_data.csv', target_rows=2000, users_file='data/user_music_data.csv'):
    synthetic_data = []

    # Load existing users from CSV
    if os.path.exists(users_file):
        users_df = pd.read_csv(users_file)
    else:
        print(f"❌ {users_file} not found! Please create a 'users.csv' with user_id and username columns.")
        return

    genre_pool = [
        "bollywood, hindi pop, desi",
        "phonk, drift phonk",
        "city pop, kayokyoku, j-pop",
        "post-punk, darkwave, cold wave",
        "jazz rap",
        "tamil, kollywood, tamil dance",
        "instrumental, chillhop, lo-fi",
        "trap, cloud rap",
        "edm, electronic",
        "rock, alternative",
        "hip hop, desi hip hop",
        "classical, indian classical",
        "synthwave, retro, 80s",
        "haryanvi, desi",
        "k-pop, dance pop",
        ""
    ]

    adjectives = ["Midnight", "Lost", "Neon", "Golden", "Crimson", "Lonely", "Burning", "Secret", "Frozen", "Electric"]
    nouns = ["Dreams", "Voices", "Memories", "Cross", "Rhythm", "Sky", "Edge", "Motion", "Code", "Loop"]

    prefixes = ["DJ", "MC", "The", "Lil", "Young", "S."]
    names = ["Omega Tribe", "Molchat Doma", "SoulChef", "Raja Kumari", "Ram Sampath", "Darshan Raval", "Divine", "Yuvan", "TV Girl", "Raftaar"]

    def generate_track_name():
        return f"{random.choice(adjectives)} {random.choice(nouns)}"

    def generate_artist_name():
        return f"{random.choice(prefixes)} {random.choice(names)}"

    def generate_track_id():
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=22))

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    for _ in range(target_rows):
        # Randomly pick a user from the users dataset
        user = users_df.sample(1).iloc[0]
        user_id = user['user_id']
        username = user['user_name']

        song = {
            "user_id": user_id,
            "user_name": username,
            "track_id": generate_track_id(),
            "track_name": generate_track_name(),
            "artist_name": generate_artist_name(),
            "popularity": random.randint(0, 100),
            "genres": random.choice(genre_pool),
        }
        synthetic_data.append(song)

    df = pd.DataFrame(synthetic_data)
    df.to_csv(output_file, index=False)
    print(f"✅ Realistic dataset with {target_rows} rows written to {output_file}")
