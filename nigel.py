from lyricsgenius import Genius
from rauth import OAuth1Service
import os
import re
import nltk
import time

# token generated on https://genius.com/api-clients
genius = Genius('mKm4v8Dj7SPcAIPOX2iB8HLXCdQY1QT579bMMr3tJxbiGqBuoTlevsR2sixGpvQG')

lyrics_folder = 'nigel_artist_cache'


class Nigel:
    global lyrics_folder, genius

    def __init__(self, line1, artist_name=None, sort_criterion='popularity', search_timeout=60, rhyme_level=2):
        self.line1 = self.cleanup(line1)
        self.artist_name = artist_name
        self.sort_criterion = sort_criterion
        self.search_timeout = search_timeout
        self.rhyme_level = rhyme_level


    def find_lyrics(self):
        # downloads lyrics to all songs by given artist to database

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

        time_start = time.time()
        elapsed = 0

        while page and elapsed<self.search_timeout:
            request = genius.artist_songs(artist.id, sort=self.sort_criterion, per_page=50, page=page)
            songs = request['songs']
            print(len(songs))

            for song in songs:
                # cleans up for storing as txt file on windows
                song_title = re.sub('[/:*?<>|]','',song['title'])

                if song_title not in songs_exist:
                    print(song_title)

                    while True:
                        try:
                            lyrics = genius.lyrics(song_url=song['url'])
                            break
                        except Exception:
                            print('could not find lyrics, trying again...')

                    file = f"{lyrics_folder}/{self.artist_name}/{song_title}.txt"

                    with open(file, 'w', encoding='utf-8') as f:
                        f.write(lyrics)
            
            page = request['next_page']
            elapsed = time.time() - time_start
    

    def cleanup(self, line):
        # cleans up lines
        new_line = line
        for sign in '",.?!*/-':
            new_line = new_line.replace(sign, '')
        
        new_line = new_line.replace("in'", "ing")

        return new_line


    def list_rhymes(self, rhyme, level=None):
        # returns all words that rhyme with input word, given certain level of rhyme strictness

        if level==None:
            level = self.rhyme_level

        entries = nltk.corpus.cmudict.entries()
        syllables = [(word, syl) for word, syl in entries if word == rhyme]
        rhymes = []
        for (word, syllable) in syllables:
            rhymes += [word for word, pron in entries if pron[-level:] == syllable[-level:] and word != rhyme]
        return list(rhymes)


    def find_lines(self):
        # based on the artist input (artist name or None - meaning match is to be made with all songs by all artist in database)

        rhyme_word = (self.line1.split())[-1]
        rhymes = self.list_rhymes(rhyme_word)

        if rhyme_word.endswith('ing'):
            rhymes.extend(self.list_rhymes('in', level=2))

        rhyme_lines = []

        if self.artist_name == None:
            for artistN in os.listdir(lyrics_folder):
                for songN in os.listdir(f"{lyrics_folder}/{artistN}"):
                    with open(f"{lyrics_folder}/{artistN}/{songN}", encoding='utf-8') as f:
                        lyrics = f.readlines()

                    for line in lyrics:
                        line = line[:-1]
                        if line not in rhyme_lines:
                            clean_line = self.cleanup(line)
                            line_list = clean_line.split()

                            if len(line_list)>0:
                                line_word = line_list[-1]

                                if line_word in rhymes:
                                    rhyme_lines.append(line)

        return rhyme_lines

  
artist_name = None
sort_criterion = 'popularity'
line1 = "so clueless lil bitch boy gon need a mappin'"
search_timeout = 60
rhyme_level = 2

nigel = Nigel(artist_name=artist_name, sort_criterion=sort_criterion, line1=line1, search_timeout=search_timeout, rhyme_level=rhyme_level)

rhyme_lines = nigel.find_lines()

for line in rhyme_lines:
    print(line)