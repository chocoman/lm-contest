from collections import Counter
import json
import os

class LanguageModel:
    def __init__(self):
        self.character_groups = Counter()
        self.all_characters = []
        self.training_str_length = 3
        
    def train_batch(self, text):
        for i in range(len(text) - self.training_str_length):
            characters = text[i : (i + self.training_str_length)]
            if characters[-1] not in self.all_characters:
                self.all_characters.append(characters[-1])
            self.character_groups[characters] += 1
            
        signed_reduced_characters = []
        for full_characters in self.character_groups.elements():
            reduced_characters = str(full_characters)[0][0:-1]
            if reduced_characters not in signed_reduced_characters:
                signed_reduced_characters.append(reduced_characters)
        
        combinations = []
        for reduced_characters in signed_reduced_characters:
            for last_character in self.all_characters:
                combination = 

    def predict(self, prefix):
        if len(prefix)<self.training_str_length:
            return "e"
        prefix = prefix[- (self.training_str_length-1) ,-1] + prefix [-1]
        
        
        return best_character

    def load(self, directory):
        model_json = json.load(open(os.path.join(directory, 'model.json'), 'r', encoding="utf8"))
        self.self.all_characters = model_json['all_characters']
        for character in model_json['character_groups']:
            self.character_groups[character] += model_json['character_groups'][character]

    def export(self):
        return {
            'character_groups': self.character_groups,
            'all_characters': self.all_characters,
        }
