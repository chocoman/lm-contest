from collections import Counter
import json
import os

class LanguageModel:
    def __init__(self):
        self.last_character = Counter()
        self.total_characters = 0
        self.next_character = Counter()
        self.dictionary = {}
        self.written_down = []

    def train_batch(self, text):
        self.previous_characters = PreviousCharacters(self.dictionary)
        for i in range((len(text)-1)):
            first = text[i]
            last = text[i+1]
            if (first not in self.written_down):
                self.previous_characters.create_character(first)
                self.written_down.append(first)
            self.previous_characters.increase_character_count(first, last)
            
            
            
            #self.next_character[characters[:2]] +=1
            #self.last_character[characters[:1]] = characters[1:]
        self.dictionary = self.previous_characters.get_dictionary()
        self.total_characters += len(text)

    def get_most_frequent_character(self):
        best_likelihood = 0
        most_likely = None
        for character in self.last_character:
            likelihood = self.last_character[character] / self.total_characters
            if likelihood > best_likelihood:
                best_likelihood = likelihood
                most_likely = character
        return most_likely

    def predict(self, prefix):
        return self.get_most_frequent_character()

    def load(self, directory):
        model_json = json.load(open(os.path.join(directory, 'model.json'), 'r', encoding="utf8"))
        self.total_characters = model_json['total_characters']
        for character in model_json['last_character']:
            self.last_character[character] += model_json['last_character'][character]

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