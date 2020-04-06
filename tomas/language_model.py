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
        self.nextwordprediction = False
        self.persumed_next_word = False
        self.previous_last = ""

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

    def wordlist(self, text, training):
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
        if training:
            return wordlist
        return wordlist, word
        
    def train_batch(self, text):
        text = self. whitelist(text)
        text = self.wordlist(text, True)
        for i in range((len(text)-1)):
            self.trie.add(text[i], text[i+1])            


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
        prefix, leftover = self.wordlist(prefix, False)

        if (len(prefix)>=1):
            #Prefix is longer than 1 word
            last_word = prefix[len(prefix)-1]
            if last_word!=self.previous_last:
                self.persumed_next_word = self.trie.predict_next_word(last_word, False)
                self.nextwordprediction=True
                self.previous_last=last_word
        else:
            #Prefix is less than one word
            #  individual letter prediction

            temp = self.trie.predict_next_word(leftover, True)
            if temp=="$":
                return(" ")
            if len(temp)<2:
                #print("this is temp " + temp)
                return(temp)
            
            
        
        #word based letter prediction
        if self.persumed_next_word!= False:
            if self.nextwordprediction==True:
                if leftover == self.persumed_next_word[0:len(leftover)]:
                    return(self.persumed_next_word[len(leftover)])



        #letter prediction backup
        #print("WORD PREDICTION FAILED")
        temp = self.trie.predict_next_word(leftover, True)
        if temp=="$":
            return(" ")
        if len(temp)==1:
            return(temp)
        return(" ")

    def load(self, directory):
        model_json = json.load(open(os.path.join(directory, 'model.json'), 'r', encoding="utf8"))
        self.trie = self.trie.load_trie(self.trie.root, model_json['trie'])
        

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
    
    def load_node(self, key, count):
        loadedNode = Node(key)
        self.next_nodes[key] = [loadedNode, count]
        return loadedNode

class Trie:
    def __init__(self):
        self.root = Node('^')

    def add_node(self, node):
        self.root = node
    
    def add (self, word, next_word):
        #print(next_word )
        word= "^"+word+"$"
        current_node = self.root
        for i in word:
            current_node = current_node.next(i)
        current_node.next(next_word)

    def save_trie(self):    
        node = self.root
        var = self.read_trie(node.next_nodes, False)
        return(var)

    def makelist (self, children,savecount):
        return([[children,savecount,[]]])

    def read_trie(self, node, isLast):
        nodes = []
        for children in node:
            savecount = node[children][1]
            if (children=="$"):
                temp=["",0]
                for i in node[children][0].next_nodes:
                    if (temp[1] < node[children][0].next_nodes[i][1]):
                        temp = [i,node[children][0].next_nodes[i][1]]
                savenode=temp[0]
                nodes.append([children,savecount,self.makelist(children,savecount)])
            else:
                savenode = self.read_trie(node[children][0].next_nodes, False)
                nodes.append([children,savecount,savenode])
        return nodes
    
    def load_trie(self, node, list):
        for i in list:
            char = i[0]
            count = i[1]
            sublist = i[2]
            self.load_trie(node.load_node(char, count),sublist)
        var = Trie()
        var.add_node(node)
        return var
            
    def predict_next_word(self, word, orLetter):
        #print(self.root.next_nodes["^"][0].next_nodes)
        current_node=self.root.next_nodes["^"][0]
        if(orLetter==False):
            word= word+"$"
        temp=["",0]
        #print("THIS SHOULD CHANGE: "+word)
        try:
            for i in word:
                current_node = current_node.next(i)
                temp=["",0]
                for j in current_node.next_nodes:
                    #print(j)
                    #print(current_node.next_nodes[j][1])
                    if (temp[1] < current_node.next_nodes[j][1] and ((len(j)>1)or orLetter)):
                        temp = [j,current_node.next_nodes[j][1]]
            if(orLetter):
                print("next letter: "+temp[0])
                return (temp[0])
            else:
                print("next word: "+ temp[0])
            return (temp[0]+" ")
        except:
            print("failed to predict")
            return(False)

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
