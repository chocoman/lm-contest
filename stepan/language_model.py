from collections import Counter
import json
import os

class LanguageModel:
    def __init__(self):
        self.character_groups = Counter()
        self.training_str_length = 7
        self.signed_groups = []
        
    def train_batch(self, text):
        for i in range(len(text) - self.training_str_length - 1):
            characters = text[i : (i + self.training_str_length)]
            last_character = text[i + self.training_str_length]
            if str(characters) not in self.signed_groups:
                self.signed_groups.append(str(characters))
                self.character_groups[characters] = Counter()
            self.character_groups[characters][last_character] += 1
        
    def predict(self, prefix):
        if len(prefix)<self.training_str_length:
            return "e"
        prefix = prefix[(- self.training_str_length) :-1] + prefix [-1]
        prefix = str(prefix)
        
        try:
            following_characters = Counter(self.character_groups[prefix])
            best_character = str((following_characters.most_common(1))[0][0])
        except:
            return "e"
        return best_character

    def load(self, directory):
        model_json = json.load(open(os.path.join(directory, 'model.json'), 'r', encoding="utf8"))
        self.character_groups = model_json['character_groups']

    def export(self):
        return {'character_groups': self.character_groups}
