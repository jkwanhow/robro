import random

class Leo:
    def __init__(self, phrases_source):
        txt_file = open(phrases_source, 'r')
        lines = txt_file.readlines()
        phrases = []
        for phrase in lines:
            phrases.append(phrase)
        
        self.phrases = phrases
        txt_file.close()
        
    def use_verb(self, verb):
        phrase = random.choice(self.phrases)
        new_phrase = phrase.replace("-verb-", verb)
        return new_phrase

    def random_verb(self):
        #returns a random verb
        verbs = ["sleep", "run", "hike", "eat", "poop", "work", "play", "bike", "drink", "drive"]
        return random.choice(verbs)

    def random_line(self):
        return self.use_verb(self.random_verb())


    def add_phrase(self, phrases_source, phrase):
        #append a new special phrase into our text file oh phrases
        #You should create a new Leo object after calling this command to allow for a new
        #update list of phrases
        if not ("-verb-" in phrase):
            return "phrase needs to contain -verb- to insert verbs"
        if "\n" in phrase:
            return "Fuck you! Trying to use a new line? Think i wouldn't catch that?\n\
But for real don't fuck with my text file of Leo phrases, they're precious"
        txt_file = open(phrases_source, 'a')
        txt_file.write(f"\n{phrase}")
        txt_file.close()
        new_phrase = phrase.replace("-verb-", self.random_verb())
        return f"phrases added for example:\n'{new_phrase}'"

    def all_phrases(self):
        to_print = '\n'.join(self.phrases)
        return to_print

