# ------------------- IMPORTING REQUIRED LIBRARIES -------------------
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

# ------------------- STEP 1: GET USER INPUT FOR DATE -------------------
# Prompt the user to enter a date in the format YYYY-MM-DD
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year = date.split("-")[0]  # Extract the year portion from the date

# ------------------- STEP 2: SCRAPE BILLBOARD HOT 100 -------------------
# Use the Billboard URL pattern to access the top 100 songs for the entered date
BILLBOARD_URL = f"https://www.billboard.com/charts/hot-100/{date}/"

# Send a GET request to the Billboard URL
response = requests.get(BILLBOARD_URL)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Select all song title elements from the page
song_elements = soup.select("li ul li h3")

# Extract and clean the text for each song title
songs = [song.get_text(strip=True) for song in song_elements]

# Display the number of songs scraped
print(f"✅ Found {len(songs)} songs on Billboard Hot 100.")

# ------------------- STEP 3: SPOTIFY AUTHENTICATION -------------------
# Authenticate with Spotify using Spotipy and OAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",         # Permission to create private playlists
    redirect_uri="https://example.com/callback",  # Must match the URI in Spotify dashboard
    client_id="---------",                   # Replace with your Spotify Client ID
    client_secret="---------------",         # Replace with your Spotify Client Secret
    show_dialog=True,                        # Forces login every time
    cache_path="token.txt"                   # Stores token to avoid repeated login
))

# Get the current Spotify user's ID
user_id = sp.current_user()["id"]

# ------------------- STEP 4: SEARCH SONGS ON SPOTIFY -------------------
# Search for each song scraped from Billboard on Spotify

song_uris = []  # List to store Spotify URIs of found songs

for song in songs:
    query = f"track:{song} year:{year}"  # Spotify search query format
    result = sp.search(q=query, type="track", limit=1)  # Search Spotify for the track
    try:
        uri = result["tracks"]["items"][0]["uri"]  # Extract URI if found
        song_uris.append(uri)
    except IndexError:
        print(f"❌ {song} not found on Spotify. Skipped.")  # Song not found

# Display the number of songs found on Spotify
print(f"\n✅ Found {len(song_uris)} songs on Spotify.")

# ------------------- STEP 5: CREATE SPOTIFY PLAYLIST -------------------
# Create a new private playlist in the user's account

playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{date} Billboard 100",  # Playlist name
    public=False,                  # Make it a private playlist
    description=f"Top 100 songs from Billboard on {date}"  # Optional description
)

# Extract the playlist ID
playlist_id = playlist["id"]

# Add the found song URIs to the created playlist
sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)

# Success message
print(f"\n🎉 Success! Playlist '{playlist['name']}' created with {len(song_uris)} songs.")
