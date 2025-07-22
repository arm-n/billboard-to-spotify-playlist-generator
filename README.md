
````markdown
# 🎵 Billboard to Spotify Playlist Generator

This Python project scrapes the Billboard Hot 100 chart for a given historical date and automatically creates a private Spotify playlist with those top 100 songs.

---

## 📌 What This Project Does

- Prompts you to enter a historical date (in `YYYY-MM-DD` format)
- Scrapes the Billboard Hot 100 songs for that date
- Searches for those songs on Spotify
- Creates a new private playlist in your Spotify account
- Adds all the available tracks to the playlist

---

## 🚀 Setup Instructions

### 🔧 1. Clone the Repo

```bash
git clone https://github.com/arm-n/billboard-to-spotify-playlist.git
cd billboard-spotify-playlist
````

### 📦 2. Install Dependencies

Make sure you have Python installed (3.7 or above), then install the required Python libraries:

```bash
pip install -r requirements.txt
```

If there's no `requirements.txt`, install manually:

```bash
pip install spotipy beautifulsoup4 requests
```

---

## 🎛️ Step-by-Step Guide

### 🗓️ Step 1: Input a Date

Run the script and enter a date in the format `YYYY-MM-DD` (e.g., `2000-08-12`).
The script will scrape the Billboard Hot 100 songs from that date.

---

### 🔐 Step 2: Set Up Spotify Authentication

#### 2.1 Create a Spotify Developer App

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
2. Log in with your Spotify account
3. Click **"Create an App"**
4. Give it a name and description
5. Add a Redirect URI:
   Use `https://example.com/callback`
   You **must** also add this same URI in your script under `redirect_uri`

#### 2.2 Replace Credentials

In `main.py`, replace the placeholders with your app credentials:

```python
client_id="YOUR_CLIENT_ID"
client_secret="YOUR_CLIENT_SECRET"
```

#### 2.3 On First Run

When you run the script for the first time:

* A browser window will open asking for Spotify login and permissions
* After granting access, you’ll be redirected to `example.com`
* Copy the full URL from your browser’s address bar and paste it into the terminal prompt

💾 This will generate a `token.txt` file storing your OAuth token for future runs.

---

### 🔍 Step 3: Scraping and Searching Songs

The script will:

* Scrape Billboard’s top 100 tracks using `requests` and `BeautifulSoup`
* Search each song on Spotify using the query format:
  `"track:{song_title} year:{year}"`
* Skip any songs not found on Spotify

---

### 🎵 Step 4: Creating the Playlist

* A private playlist will be created in your Spotify account named:

```
YYYY-MM-DD Billboard 100
```

* All found songs will be added to that playlist.

---

## 🛠️ Troubleshooting

### ❌ Redirect URI Error

If you see this error:

```
INVALID_CLIENT: Insecure redirect URI
```

✅ Make sure your `redirect_uri` in both your code **and** Spotify Dashboard matches exactly:

```
https://example.com/callback
```

### ❌ Token Cache / JSON Error

If the script says:

```
Couldn't decode JSON from cache at: token.txt
```

Just follow the prompt to re-authenticate. A fresh token will be generated.

### ❌ Songs Not Found

Not all Billboard songs exist on Spotify, especially older or niche ones.
These will be skipped automatically with a message like:

```
❌ {Song Title} not found on Spotify. Skipped.
```

---

## 💡 Extras

* You can edit the playlist name, description, or make it public by modifying the parameters in `sp.user_playlist_create()`
* Your authentication token expires every hour; the script refreshes it using the refresh token stored in `token.txt`

---

## 🧠 Credits & Inspiration

This project was inspired by an [Angela Yu Python challenge](https://www.udemy.com/course/100-days-of-code/) and built using:

* 🎵 [Spotify Web API](https://developer.spotify.com/documentation/web-api/)
* 📰 [Billboard Hot 100](https://www.billboard.com/charts/hot-100/)
* 🐍 Python + Spotipy + BeautifulSoup

---

## 📎 License

MIT License. Free to use, modify, and share.

