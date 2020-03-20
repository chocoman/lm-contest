from collections import Counter
import json
import os
from random import randint

class LanguageModel:
    def __init__(self):
        self.character_counts = Counter()
        self.total_characters = 0

    def train_batch(self, text):
        for i in range(len(text)):
            character = text[i]
            self.character_counts[character] += 1
        self.total_characters += len(text)

    def get_space(self):
        best_likelihood = 0
        most_likely = None
        for character in self.character_counts:
            likelihood = self.character_counts[character] / self.total_characters
            if likelihood > best_likelihood:
                best_likelihood = likelihood
                most_likely = character
        return most_likely
    
    def list_all_words(self):
        with open ("ustava.txt", "r") as data:
          dataset = data.read()
        word_list = dataset.split()
        word_list = tuple(word_list)
        return sorted(word_list, key=str.lower)
    
    def predict(self, prefix):
        return get_space()
        
    def load(self, directory):
        model_json = json.load(open(os.path.join(directory, 'model.json'), 'r'))
        self.total_characters = model_json['total_characters']
        for character in model_json['character_counts']:
            self.character_counts[character] += model_json['character_counts'][character]

    def export(self):
        return {
            'character_counts': self.character_counts,
            'total_characters': self.total_characters,
        }
