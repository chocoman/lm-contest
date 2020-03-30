from collections import Counter
from typing import Tuple
import json
import os

class LanguageModel:
    def __init__(self):
        self.character_counts = Counter()
        self.total_characters = 0

    def predict(self, prefix): #just a placeholder code while trie is WIP
        pref_list = prefix.split() # all words in prefix
        last_word = pref_list[-1]  # just the last word
        last_word_split = [char for char in last_word] # splits the last word into characters, the rest doesn't matter
        last_letter = last_word_split[-1]
        print(last_letter)
        return " "

    def get_list_of_words(self, file_name):     # gets words from textfile
        with open (file_name, "r", encoding = "utf8") as test_data:
          wordset = test_data.read()
        word_list = wordset.split()
        word_list = tuple(word_list)    # transforms the list into tuple
        return sorted(word_list, key = str.lower)

    def sort_words(self):
        list_of_words = self.get_list_of_words(self, "ustava.txt")
        print(list_of_words)
        for word in list_of_words:
            for letter in word:
                print(letter)

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

class LetterTrie:  #trie - each letter stores how many times it appeared after the previous letter and all its children -II-
    def __init__(self, letter):
        self.letter = letter
        self.how_many_times = 1 # how many times was this letter after the previous letter
        self.child_letters = [] # all letters that might appear after this one

    def add_word(rootnode, word): # ets the word and adds all of its letters
        node = rootnode
        for letter in word:       # raises the howmanytimes counter or creates a new node if it doesnt exist yet for each child
            found_in_children = False # if this letter already appeared as a child
            for child in node.child_letters:
                if (child.letter == letter):  # if it is in the child
                    found_in_children = True
                    child.how_many_times += 1
                    node = child # the next letter is going to check children of this letter
                    break # breaks the loop
            if(found_in_children == False):   # if not, it creates a new node with this letter
                new_node = LetterTrie(letter)
                node.children.append(new_node)
                node = new_node

l = LanguageModel
result = l.predict(l, "hello there ")

