from encodings import utf_8
from lyricsgenius import Genius
from rauth import OAuth1Service
import os

lyrics_folder = 'nigel_artist_cache'
artist_name = 'Kendrick Lamar'
sort_criterion = 'popularity'
no_songs = 5

# token generated on https://genius.com/api-clients
genius = Genius('mKm4v8Dj7SPcAIPOX2iB8HLXCdQY1QT579bMMr3tJxbiGqBuoTlevsR2sixGpvQG')

def find_lyrics():
    if artist_name not in os.listdir(lyrics_folder):
        os.mkdir(f"{lyrics_folder}/{artist_name}")
        search = 'Y'

    else:
        songs_exist = os.listdir(f"{lyrics_folder}/{artist_name}")

        for title in songs_exist:
            print(title[:-4])
        
        search = str(input('Continue to search for songs from artist?\nY / N : '))

    if search == 'Y':
        artist = genius.search_artist(artist_name, max_songs=no_songs, sort=sort_criterion)

        for song in artist.songs:
            if song.title not in songs_exist:
                file = f"{lyrics_folder}/{artist_name}/{song.title}.txt"

                print(song.lyrics)

                with open(file, 'w', encoding='utf-8') as f:
                    f.write(song.lyrics)
    
find_lyrics()