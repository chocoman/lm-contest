from collections import Counter
import json
import os

class LanguageModel:
    def __init__(self):
        self.character_groups = Counter()
        self.training_str_length = 7
        self.signed_groups = []
        self.total_predictions = 0
        self.not_known = 0
        self.allowed_characters = "aáäbcčdďeéěfghiíjklmnňoóöpqrřsštťuúůüvwxyýzž "
        
    def train_batch(self, text):
        new_text = ""
        last_character = " "
        for character in text:
            if last_character == " " and character ==" ":
                break
            new_text = new_text + character
            last_character = character
        text = new_text
        for i in range(len(text) - self.training_str_length - 1):
            characters = text[i : (i + self.training_str_length)]
            last_character = text[i + self.training_str_length]
            if last_character not in self.allowed_characters:
                break
            if str(characters) not in self.signed_groups:
                self.signed_groups.append(str(characters))
                self.character_groups[characters] = Counter()
            self.character_groups[characters][last_character] += 1
        
    def predict(self, prefix):
        self.total_predictions = self.total_predictions + 1
        if len(prefix)<self.training_str_length:
            print("Předpovězeno: " + str(self.total_predictions) + "Procento neznámých prefixů: " + str(100 * self.not_known / self.total_predictions))
            return "e"
        prefix = prefix[(- self.training_str_length) :-1] + prefix [-1]
        prefix = str(prefix)
        try:
            following_characters = Counter(self.character_groups[prefix])
            best_character = str((following_characters.most_common(1))[0][0])
        except:
            self.not_known = self.not_known + 1
            best_character = " "
        print("Procento neznámých prefixů: " + str(100 * self.not_known / self.total_predictions))
        return best_character

    def load(self, directory):
        model_json = json.load(open(os.path.join(directory, 'model.json'), 'r', encoding="utf8"))
        self.character_groups = model_json['character_groups']

    def export(self):
        return {'character_groups': self.character_groups}
