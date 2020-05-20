import sys
sys.path.append('..')
from ondrej.language_model import LanguageModel

#TESTING (WORKS! with local loading)
l = LanguageModel()
l.add_words_to_trie(True, "ustava.txt")
l.load('contest_model/')
#l.trie.print_children_counts()
wordlist = ["", "Soudc", "Ostro", "Hmm", "Guvernantk", "Kul", "Emm", "Em"]
for word in wordlist:
    prediction = l.predict(word)
    print(word + ' ' + prediction)
