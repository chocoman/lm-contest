
class LetterTrie:  #trie - each letter stores how many times it appeared after the previous letter and all its children -II-
    def __init__(self, letter):
        self.letter = letter
        self.how_many_times = 1 # how many times was this letter after the previous letter
        self.child_letters = [] # all letters that might appear after this one

    def add_word(rootnode, word): # gets the word and adds all of its letters
        node = rootnode
        for letter in word:             # raises the howmanytimes counter or creates a new node if it doesn't exist yet for each child (letter)
            found_in_children = False   # if this letter already appeared as a child
            for child in node.child_letters:  # searches for it in all of its child letters
                if (child.letter == letter):  # if it is in the child
                    found_in_children = True
                    child.how_many_times += 1
                    node = child # the next letter is going to check children of this letter
                    break # breaks the loop, because it found the letter
            if(found_in_children == False):   # if not, it creates a new node with this letter
                new_node = LetterTrie(letter)
                node.child_letters.append(new_node)
                node = new_node

    def return_best_child(self): # returns the most common child
        most_common_letter = " "
        highest_count = 0        # self explanatory... finds the child with highest count
        for child in self.child_letters:
            if(child.how_many_times > highest_count):
                highest_count = child.how_many_times
                most_common_letter = child.letter
        return most_common_letter

    def print_children_counts(self): # prints all children and their counts
        for child in self.child_letters:
            print(child.letter + " " + str(child.how_many_times))
