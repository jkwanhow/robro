from lyricsgenius import Genius
from rauth import OAuth1Service
import os
import re

# token generated on https://genius.com/api-clients
genius = Genius('mKm4v8Dj7SPcAIPOX2iB8HLXCdQY1QT579bMMr3tJxbiGqBuoTlevsR2sixGpvQG')

lyrics_folder = 'nigel_artist_cache'


class Nigel:
    global lyrics_folder, genius


    def __init__(self, line1, artist_name=None, sort_criterion='popularity'):
        self.line1 = line1
        self.artist_name = artist_name
        self.sort_criterion = sort_criterion


    def find_lyrics(self):
        if self.artist_name not in os.listdir(lyrics_folder):
            os.mkdir(f"{lyrics_folder}/{self.artist_name}")

        songs_exist = [title[:-4] for title in os.listdir(f"{lyrics_folder}/{self.artist_name}")]

        while True:
            try:
                artist = genius.search_artist(self.artist_name, max_songs=1)
                break
            except Exception:
                print('connection timeout, trying again...')

        page = 1

        while page:
            request = genius.artist_songs(artist.id, sort=self.sort_criterion, per_page=50, page=page)
            songs = request['songs']
            print(len(songs))

            for song in songs:
                if song['title'] not in songs_exist:
                    print(song['title'])

                    while True:
                        try:
                            lyrics = genius.lyrics(song_url=song['url'])
                            break
                        except Exception:
                            print('could not find lyrics, trying again...')

                    file = f"{lyrics_folder}/{self.artist_name}/{re.sub('[/:*?<>|]','',song['title'])}.txt"

                    with open(file, 'w', encoding='utf-8') as f:
                        f.write(lyrics)
            
            page = request['next_page']
    

    def find_rhymes(self):
        if self.artist_name != None:
            song_bank = os.listdir(f"{lyrics_folder}/{self.artist_name}")
        

nigel = Nigel(line1='so clueless lil bitch boy gon need a map', artist_name='Drake')

nigel.find_lyrics()