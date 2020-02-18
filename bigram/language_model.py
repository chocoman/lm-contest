from collections import Counter
import json
import os

class LanguageModel:
    def __init__(self):
        self.character_counts = Counter()
        self.bigram_counts = Counter()

    def train_batch(self, text):
        text = '\n' + text
        for i in range(1, len(text)):
            character = text[i]
            bigram = text[i - 1 : i + 1]
            self.character_counts[character] += 1
            self.bigram_counts[bigram] += 1

    def get_next_character(self, last_letter):
        best_score = 0
        most_likely = None
        for character in self.character_counts:
            bigram_count = self.bigram_counts[last_letter + character]
            character_count = self.character_counts[character]
            score = bigram_count + 0.0001 * character_count
            if score > best_score:
                best_score = score
                most_likely = character
        return most_likely

    def predict(self, prefix):
        last_letter = '\n'
        if len(prefix) > 0: last_letter = prefix[-1]
        return self.get_next_character(last_letter)

    def load(self, directory):
        model_json = json.load(open(os.path.join(directory, 'model.json'), 'r'))
        for character in model_json['character_counts']:
            self.character_counts[character] += model_json['character_counts'][character]
        for bigram in model_json['bigram_counts']:
            self.bigram_counts[bigram] += model_json['bigram_counts'][bigram]

    def export(self):
        return {
            'character_counts': self.character_counts,
            'bigram_counts': self.bigram_counts,
        }
