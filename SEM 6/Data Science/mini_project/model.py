import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, MultiLabelBinarizer

def clean_and_prepare(df):
    #! Fill NaN genres
    df['genres'] = df['genres'].fillna('')

    #! Convert comma-separated genres string to list
    df['genre_list'] = df['genres'].apply(lambda g: [genre.strip() for genre in g.split(',') if genre.strip()])

    #! Binarize genres (One-Hot style)
    mlb = MultiLabelBinarizer()
    genre_encoded = mlb.fit_transform(df['genre_list'])
    genre_df = pd.DataFrame(genre_encoded, columns=mlb.classes_)

    #! Combine with popularity
    model_df = pd.concat([df[['popularity']].reset_index(drop=True), genre_df.reset_index(drop=True)], axis=1)

    return model_df, df

def build_model_from_csv(csv_file='data/synthetic_user_music_data.csv'):
    df = pd.read_csv(csv_file)

    #! Clean and prepare data
    model_df, original_df = clean_and_prepare(df)

    #! Scale numeric features
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(model_df)

    #! Clustering
    kmeans = KMeans(n_clusters=3, random_state=42)
    original_df['cluster'] = kmeans.fit_predict(scaled_features)

    #! Save clustered dataset back for visualization usage
    clustered_csv = 'data/clustered_music_data.csv'
    original_df.to_csv(clustered_csv, index=False)
    print(f"✅ Clustering complete. Saved to {clustered_csv}")

    return original_df, kmeans
