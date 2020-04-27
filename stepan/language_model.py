from collections import Counter
import json
import os

class LanguageModel:
    def __init__(self):
        self.character_groups = Counter()
        self.training_str_length = 5
        self.signed_groups = []
        self.total_predictions = 0
        self.not_known = 0
        self.allowed_characters = "aáäbcčdďeéěfghiíjklmnňoóöpqrřsštťuúůüvwxyýzž "
        self.big_characters = "AÁÄBCČDĎEÉĚFGHIÍJKLMNŇOÓÖPQRŘSŠTŤUÚŮÜVWXYÝZŽ"
    
    def make_all_characters_small(self, sentence):
        new_sentence = ""
        for character in sentence:
            if character not in self.big_characters:
                new_sentence = new_sentence + character
            else:
                index = self.big_characters.index(character) 
                new_character = self.allowed_characters[index]
                new_sentence = new_sentence + new_character
        return new_sentence
    
    def remove_excess_spaces(self, sentence):
        new_sentence = ""
        last_character = " "
        for character in sentence:
            if last_character == " " and character ==" ":
                break
            new_sentence = new_sentence + character
            last_character = character
        return new_sentence
        
    def train_batch(self, sentence):
        sentence = self.remove_excess_spaces(sentence)
        sentence = self.make_all_characters_small(sentence)
        for i in range(len(sentence) - self.training_str_length - 1):
            characters = sentence[i : (i + self.training_str_length)]
            last_character = sentence[i + self.training_str_length]
            if last_character not in self.allowed_characters:
                break
            if str(characters) not in self.signed_groups:
                self.signed_groups.append(str(characters))
                self.character_groups[characters] = Counter()
            self.character_groups[characters][last_character] += 1
        
    def predict(self, prefix):
        self.total_predictions = self.total_predictions + 1
        prefix = self.remove_excess_spaces(prefix)
        if len(prefix)<self.training_str_length:
            print("Procento neznámých prefixů: " + str(100 * self.not_known / self.total_predictions))
            return "e"
        prefix = prefix[(- self.training_str_length) :-1] + prefix [-1]
        prefix = str(prefix)
        prefix = self.make_all_characters_small(prefix)
        try:
            following_characters = Counter(self.character_groups[prefix])
            best_character = str((following_characters.most_common(1))[0][0])
        except:
            self.not_known = self.not_known + 1
            best_character = " "
            print("Neznám prefix: " + prefix + "; procento neznámých prefixů: " + str(100 * self.not_known / self.total_predictions))
        return best_character

    def load(self, directory):
        model_json = json.load(open(os.path.join(directory, 'model.json'), 'r', encoding="utf8"))
        self.character_groups = model_json['character_groups']

    def export(self):
        return {'character_groups': self.character_groups}
