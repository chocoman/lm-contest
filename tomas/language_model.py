from collections import Counter
import json
import os

class LanguageModel:
    def __init__(self):
        self.total_characters = 0
        self.next_character = Counter()
        self.dictionary = {}
        self.written_down = []
        self.prefixlen = 4

    def whitelist(self, text):
        whitelist = "QWERTYUIOPASDFGHJKLZXCVBNMĚŠČŘŽÝÁÍÉĎŮÚŇŤ ňťwe–rtyuÓóöüÖÜiop„“asdďfghjklzxccvbnměščřžýáíéúů)(,:.'!?1234567890;-" + '"'
        new_text = ""
        for char in text:
            if (char in whitelist):
                new_text = new_text + char
            else:
                new_text = new_text + "^"
                #print(char)
        return(new_text)
        
    def train_batch(self, text):
        text = self. whitelist(text)
        self.previous_characters = PreviousCharacters(self.dictionary)
        for i in range((len(text)-self.prefixlen)):
            first = text[(i-self.prefixlen+1):(i+1)]
            last = text[i+1]
            if (first not in self.written_down):
                self.previous_characters.create_character(first)
                self.written_down.append(first)
            self.previous_characters.increase_character_count(first, last)
            
            
            
            #self.next_character[characters[:2]] +=1
            #self.last_character[characters[:1]] = characters[1:]
        self.dictionary = self.previous_characters.get_dictionary()
        self.total_characters += len(text)

    def get_most_frequent_character(self, previous_character):
        best_character_count = 0
        most_likely = None
        try:
            for character in self.dictionary[previous_character]:
                character_count = self.dictionary[previous_character][character] 
                #print (character)
                if character_count > best_character_count and character != "^":
                    best_character_count = character_count
                    most_likely = character
        except:
            return(" ")
        if most_likely==None:
            return(" ")
        return most_likely

    def predict(self, prefix):
        prefix = self.whitelist(prefix)
        if (len(prefix)>=self.prefixlen):
            last_character = prefix[(len(prefix)-self.prefixlen):]
        else:
            print("Predicting: a (first character on line)")
            return('a')
        
        print("Predicting: " + self.get_most_frequent_character(last_character))
        return self.get_most_frequent_character(last_character)

    def load(self, directory):
        model_json = json.load(open(os.path.join(directory, 'model.json'), 'r', encoding="utf8"))
        self.total_characters = model_json['total_characters']
        for character in model_json['next_characters']:
            self.dictionary[character] = model_json['next_characters'][character]

    def export(self):
        return {
            'next_characters': self.previous_characters.get_dictionary(),
            'total_characters': self.total_characters,
        }

class PreviousCharacters:
    def __init__ (self, dictionary):
        self.firsts=dictionary

    def create_character(self, character):
        self.firsts[character] = Counter()

    def increase_character_count(self, previous, last):
        self.firsts[previous] [last] += 1

    def get_dictionary(self):
        return(self.firsts)

    def set_dictionary(self, dictionary):
        self.firsts = dictionary
