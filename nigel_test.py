from lyricsgenius import Genius
from rauth import OAuth1Service
import os

lyrics_folder = 'nigel_artist_cache'
artist_name = "Sia"

# token generated on https://genius.com/api-clients
genius = Genius('mKm4v8Dj7SPcAIPOX2iB8HLXCdQY1QT579bMMr3tJxbiGqBuoTlevsR2sixGpvQG')

if artist_name not in os.listdir(lyrics_folder):
    os.mkdir(f"{lyrics_folder}/{artist_name}")

    artist = genius.search_artist(artist_name, max_songs=1, sort='popularity')


    for song in artist.songs:
        file = f"{lyrics_folder}/{artist_name}/{song.title}.txt"

        with open(file, 'w') as f:
            f.write(song.lyrics)

