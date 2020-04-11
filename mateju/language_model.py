from collections import Counter
import json
import os

class LanguageModel:
    def __init__(self):
        self.character_counts = Counter()
        self.total_characters = 0
        self.tuples = {}

    def train_batch(self, text):
        for i in range(len(text)-1):
            character = text[i:i+1]
            self.character_counts[character] += 1
        self.total_characters += len(text)
        self.character_counts = self.character_counts.most_common()
        for y in range (len(self.character_counts)):
            if self.character_counts[y][0][0] not in self.tuples:
                self.tuples.update({character_counts[y][0][0] : character_counts[y][0][1]})

    def get_most_frequent_character(self):
        best_likelihood = 0
        most_likely = None
        if self.total_characters == 0:
            return "A"
        for character in self.character_counts:
            likelihood = self.character_counts[character] / self.total_characters
            if likelihood > best_likelihood:
                best_likelihood = likelihood
                most_likely = character
        return most_likely
    
    """
    def get_most_likely_pair(self):
        best_likelihood = 0
        most_likely = None
        first_pair_element = self.last_character
        
        if first_pair_element == None:
            return "A"
        for character in self.character_counts:
            if character == first_pair_element:
                likelyhood = self.character_counts[character+1] / self.total_characters
                if likelihood > best_likelihood:
                    best_likelihood = likelihood
                    most_likely = character+1
        return most_likely
        """

    def predict(self, prefix):
        last_character = prefix[-1]
        next_character = self.tuples.get(last_character)
        return next_character

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
