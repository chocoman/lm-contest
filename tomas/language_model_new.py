from collections import Counter
import json
import os

class LanguageModel:
    def __init__(self):
        self.total_characters = 0
        self.next_character = Counter()
        self.dictionary = {}
        self.written_down = []
        self.prefixlen = 4
        self.trie = Trie()

    def whitelist(self, text):
        whitelist = "QWERTYUIOPASDFGHJKLZXCVBNMĚŠČŘŽÝÁÍÉĎŮÚŇŤ ňťwe–rtyuÓóöüÖÜiopasdďfghjklzxccvbnměščřžýáíéúů,:.'!?1234567890;-"
        new_text = ""
        for char in text:
            if (char in whitelist):
                new_text = new_text + char
            else:
                new_text = new_text + "^"
                #print(char)
        return(new_text)

    def wordlist(self, text):
        pausechar = [" ","^"]
        wordlist = []
        word = ""
        for i in text:
            if i in pausechar:
                if (word != ""):
                    wordlist.append(word)
                word = ""
            else:
                word = word+i
        print (wordlist)
        return wordlist
        
    def train_batch(self, text):
        text = self. whitelist(text)
        text = self.wordlist(text)
        for i in range((len(text)-1)):
            self.trie.add(text[i], text[i+1])            

        #self.previous_characters = PreviousCharacters(self.dictionary)
        #for i in range((len(text)-self.prefixlen)):
        #    first = text[(i-self.prefixlen+1):(i+1)]
        #    last = text[i+1]
        #    if (first not in self.written_down):
        #        self.previous_characters.create_character(first)
        #        self.written_down.append(first)
        #    self.previous_characters.increase_character_count(first, last)
            
            
            
            #self.next_character[characters[:2]] +=1
            #self.last_character[characters[:1]] = characters[1:]
        #self.dictionary = self.previous_characters.get_dictionary()
        #self.total_characters += len(text)

    def get_most_frequent_character(self, previous_character):
        best_character_count = 0
        most_likely = None
        try:
            for character in self.dictionary[previous_character]:
                character_count = self.dictionary[previous_character][character] 
                #print (character)
                if character_count > best_character_count and character != "^":
                    best_character_count = character_count
                    most_likely = character
        except:
            return(" ")
        if most_likely==None:
            return(" ")
        return most_likely

    def predict(self, prefix):
        prefix = self.whitelist(prefix)
        if (len(prefix)>=self.prefixlen):
            last_character = prefix[(len(prefix)-self.prefixlen):]
        else:
            if(len(prefix)==0):
                return('a')
            return(' ')
        
        print("Predicting: " + self.get_most_frequent_character(last_character))
        return self.get_most_frequent_character(last_character)

    def load(self, directory):
        model_json = json.load(open(os.path.join(directory, 'model.json'), 'r', encoding="utf8"))
        self.total_characters = model_json['total_characters']
        for character in model_json['next_characters']:
            self.dictionary[character] = model_json['next_characters'][character]

    def export(self):
        return {
            'trie': self.trie.save_trie(),
        }


class Node:
    def __init__(self, char):
        self.char = char
        self.next_nodes = {}
    
    def next(self, nextchar):
        if (nextchar in self.next_nodes):
            self.next_nodes[nextchar][1]+=1
            return self.next_nodes[nextchar][0]
        else:
            newNode = Node(nextchar)
            self.next_nodes[nextchar] = [newNode,1]
            return newNode

class Trie:
    def __init__(self):
        self.root = Node('^')
    
    def add (self, word, next_word):
        word= "^"+word+"$"
        current_node = self.root
        for i in word:
            current_node = current_node.next(i)
        current_node.next(next_word)

    def save_trie(self):    
        node = self.root
        var = self.read_trie(node.next_nodes)
        return(var)

    def read_trie(self, node):
        nodes = []
        for children in node:
            savecount = node[children][1]
            savenode = self.read_trie(node[children][0].next_nodes)
            nodes.append([children,savecount,savenode])
        return nodes

class PreviousCharacters:
    def __init__ (self, dictionary):
        self.firsts=dictionary

    def create_character(self, character):
        self.firsts[character] = Counter()

    def increase_character_count(self, previous, last):
        self.firsts[previous] [last] += 1

    def get_dictionary(self):
        return(self.firsts)

    def set_dictionary(self, dictionary):
        self.firsts = dictionary
