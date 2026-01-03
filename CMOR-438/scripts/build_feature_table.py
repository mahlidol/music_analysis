import os
import sys
import csv

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_PATH = os.path.join(PROJECT_ROOT, "src") 
sys.path.append(SRC_PATH)
from lanastance.preprocessing import extract_song_features
RAW_DATA_DIR = os.path.join(PROJECT_ROOT, "data", "raw") 
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "data", "features") 
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "song_features.csv")

def read_text(path): 
    with open(path, "r", encoding="utf-8") as f: 
        return f.read()

def build_feature_table():
    rows = []

    for artist in os.listdir(RAW_DATA_DIR):
        artist_dir = os.path.join(RAW_DATA_DIR, artist)
        if not os.path.isdir(artist_dir):
            continue

        for album in os.listdir(artist_dir):
            album_dir = os.path.join(artist_dir, album)
            if not os.path.isdir(album_dir):
                continue

            print(f"Processing artist: {artist} | album: {album}")

            for filename in os.listdir(album_dir):
                song_path = os.path.join(album_dir, filename)
                if not os.path.isfile(song_path):
                    continue

                song = os.path.splitext(filename)[0]

                print(f"  Processing song: {song}")

                try:
                    text = read_text(song_path)
                except UnicodeDecodeError:
                    print(f"    Skipping non-text file: {filename}")
                    continue

                features = extract_song_features(text)

                row = {
                    "artist": artist,
                    "album": album,
                    "song": song,
                    **features
                }

                rows.append(row)

    if not rows:
        raise ValueError("No songs found. Check data/raw directory.")

    print(f"Total songs processed: {len(rows)}")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # FIX: collect all fieldnames
    fieldnames = set()
    for row in rows:
        fieldnames.update(row.keys())
    fieldnames = list(fieldnames)

    with open(OUTPUT_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nWrote feature table to {OUTPUT_PATH}")

if __name__ == "__main__":
    build_feature_table()
