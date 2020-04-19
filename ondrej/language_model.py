from typing import Tuple
from .trie import LetterTrie
import json
import os
import re # using re.split instead of split to handle more separators than just white spaces

class LanguageModel:            # work in progress - I need to figure out exporting and loading json (most likely) file with trie
    def __init__(self):                 # tested with wiki dataset and it worked pretty well I think
        self.trie = LetterTrie(" ")
        self.total_characters = 0
        self.separator = "*" # marks the end of the word
        self.splits = r'["\s(.*;,\s)\s]\s*' # string containing all seperataros used for split when training and predicting

    def predict(self, prefix):    # splits the given prefix into words, takes the last word and decides if its last letter is a space
        if(prefix[-1].isspace()): # if the last character in prefix is a space
            letter = self.return_letter_after_space()
            print("My prediction is " + letter)
            return letter         # it doesn't return space

        pref_list = re.split(self.splits, prefix) # prefix split into words
        #print(pref_list)
        last_word = pref_list[-1]                 # gets the last word
        if(last_word.isspace()):
            return "."  #if the last word "is" a space, it's because it replaced one of the self.splits characters (usually end of the sentence)

        predicted_letter = self.search_trough_trie(last_word)
        print("My prediction is " + predicted_letter)
        return predicted_letter

    def get_list_of_words(self, file_name):     # gets words from textfile
        with open (file_name, "r", encoding = "utf8") as test_data:
          wordset = test_data.read()
        word_list =  tuple(re.split(self.splits, wordset))
        return sorted(word_list, key = str.lower)

    def add_words_to_trie(self, done_training, filename): # adds all words (strings) from given list to trie (used for testing a smaller trie)
        list_of_words = self.get_list_of_words(filename)
        #print(list_of_words)
        for word in list_of_words:
            trueword = word.lower() + self.separator
            self.trie.add_word(trueword) #transforms all words into their lowercase form
        #print("word " + trueword + " added to trie")
        if(done_training == True):       # if this is the last training, it exports the trie as a json file
            self.export_trie()

    def return_letter_after_space(self):    # returns the most commonnly used letter after space
        return self.trie.return_best_child()# it doesn't consider the word/letter before the space yet


    def search_trough_trie(self, given_word): #tries to find an unfinished word in trie and predict the first missing character
        print("given word " + str(given_word))
        remaining_letters = len(given_word)
        #print("lenght of given word " + str(remaining_letters))
        node = self.trie
        predicted_letter = " "
        for letter in given_word: # for each letter in split word
            #print(letter)
            child_found = False
            for child in node.child_letters: # for each of the child letters of current node
                if child.letter == letter:   # if the letter is indeed found ind the children
                    node = child
                    remaining_letters -= 1
                    child_found = True
                    if(remaining_letters == 0): # if this is the final letter of given word
                        predicted_letter = node.return_best_child() # then it finds the best letter
            if(child_found == False):
                return " "
        if(predicted_letter == self.separator):
            predicted_letter = " "
        return predicted_letter

    def export_trie(self): # exports the trie as a json file (WIP)
        print("Exporting is work in progress")

    def load(self, directory): # WIP
        return
"""
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
"""
#Testing
"""
# TESTING (WORKS! with the ústava dataset)
l = LanguageModel()
l.add_words_to_trie(False, "ustava.txt")
l.trie.print_children_counts()
l.predict("so ")
l.predict("prezi")
l.predict("ústa")
l.predict("vra")
"""
