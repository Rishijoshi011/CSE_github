# generate_dataset.py

from generate_songs import generate_synthetic_data  # This should already exist in your project

if __name__ == "__main__":
    output_csv_path = 'data/synthetic_user_music_data.csv'
    generate_synthetic_data(output_csv_path)
    print(f"✅ Synthetic dataset saved at: {output_csv_path}")
