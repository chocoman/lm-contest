from typing import Tuple
import pickle
import os
import sys
import re # using re.split instead of split to handle more separators than just white spaces

class LanguageModel:
    def __init__(self):                 # tested with wiki dataset and it worked pretty well I think
        self.trie = LetterTrie(" ")
        self.separator = "*"            # marks the end of the word
        # string containing all seperataros used for split when training and predicting
        self.split_chars = r'["\s(.*;,\s)\s]\s*'
        sys.setrecursionlimit(10000)

    def predict(self, prefix):    # splits the given prefix into words, takes the last word and decides if its last letter is a space
        #print("---------------")
        #print("given text: " + str(prefix))
        if(len(prefix) == 0):
            return " "
        if(prefix[-1].isspace()): # if the last character in prefix is a space
            letter = self.return_letter_after_space()
            #print("My prediction is " + letter)
            return letter         # it doesn't return space

        pref_list = re.split(self.split_chars, prefix) # prefix split into words
        last_word = pref_list[-1].lower()              # gets the last word
        if(last_word.isspace()):
            return "."  #if the last word "is" a space, it's because it replaced one of the self.split_chars characters (usually end of the sentence)

        predicted_letter = self.search_trough_trie(last_word)
        print("My prediction is " + predicted_letter)
        return predicted_letter

    def get_list_of_words(self, file_name):     # gets words from textfile and returns them sorted
        with open (file_name, "r", encoding = "utf8") as test_data:
          wordset = test_data.read()
        word_list =  tuple(re.split(self.split_chars, wordset))
        return sorted(word_list, key = str.lower)

    def add_words_to_trie(self, done_training, filename): # adds all words (strings) from given list to trie (used for testing a smaller trie)
        list_of_words = self.get_list_of_words(filename)
        #print(list_of_words)
        for word in list_of_words:
            trueword = word.lower() + self.separator
            self.trie.add_word(trueword)                  #transforms all words into their lowercase form
        #print("word " + trueword + " added to trie")
        if(done_training == True):                        # if this is the last training, it exports the trie as a json file
            self.export_trie('contest_model/')

    def return_letter_after_space(self):    # returns the most commonnly used letter after space
        return self.trie.return_best_child()# it doesn't consider the word/letter before the space yet

    def search_trough_trie(self, given_word): #tries to find an unfinished word in trie and predict the first missing character
        remaining_letters = len(given_word)
        node = self.trie
        predicted_letter = " "
        #self.trie.add_word(given_word)
        for letter in given_word: # for each letter in split word
            child_found = False
            for child in node.child_letters: # for each of the child letters of current node
                if child.letter == letter:   # if the letter is indeed found ind the children
                    node = child
                    remaining_letters -= 1
                    child_found = True
                    if(remaining_letters == 0):
                        predicted_letter = node.return_best_child()
            if(child_found == False):
                return " "
        if(predicted_letter == self.separator):
            predicted_letter = " "
        return predicted_letter

    def export_trie(self, directory): # exports the trie as a pickle file
        #print("Exporting")
        filename = os.path.join(directory, "trie.pickle")
        exported_trie = open(filename,"wb")
        pickle.dump(self.trie, exported_trie)
        exported_trie.close()
        #print("Exporting Finished")

    def load(self, directory): # loads the trie from the pickle file
        #print("Loading")
        #print(str(os.path.join(directory, "trie.pickle")))
        filename = os.path.join(directory, "trie.pickle")
        loaded_trie = open(filename, "rb")
        self.trie = pickle.load(loaded_trie)
        loaded_trie.close()
        #print("Loading Finished")

class LetterTrie:  #trie - each letter stores how many times it appeared after the previous letter and all its children -II-
    def __init__(self, letter):
        self.letter = letter
        self.how_many_times = 1 # how many times was this letter after the previous letter
        self.child_letters = [] # all letters that might appear after this one

    def add_word(self, word): # gets the word and adds all of its letters
        node = self
        for letter in word:                     # raises the howmanytimes counter or creates a new node if it doesn't exist yet for each child (letter)
            found_in_children = False           # if this letter already appeared as a child
            for child in node.child_letters:    # searches for it in all of its child letters
                if (child.letter == letter):    # if it is found
                    found_in_children = True
                    child.how_many_times += 1
                    node = child                # the next letter is going to check children of this letter
                    break
            if(found_in_children == False):     # if not, it creates a new node with this letter
                new_node = LetterTrie(letter)
                node.child_letters.append(new_node)
                node = new_node

    def return_best_child(self): # finds the child letter with highest count and returns it
        most_common_letter = " "
        highest_count = 0
        for child in self.child_letters:
            if(child.how_many_times > highest_count):
                highest_count = child.how_many_times
                most_common_letter = child.letter
        return most_common_letter

    def print_children_counts(self): # prints all children and their counts
        for child in self.child_letters:
            print(child.letter + " " + str(child.how_many_times))
