class node:
  def __init__(self, character):
    self.character = character
    self.lower_nodes = []
    self.counter = Counter()
    
  def create_node(self, character):
    # ~ print("tvořím nový uzel \""+pismeno+"\"")
    next_node = node(character)
    self.lower_nodes.append(next_node)
    return(next_node)
    
  def find_next(self, wanted_character):
    if len(self.lower_nodes)  == 0:
      return(False)
    for lower in self.lower_nodes:
      if lower.character == wanted_character:
        return(lower)
    return(False)
    
  def save(self):
    result = self.character
    for lower in self.lower_nodes:
      result += lower.save()
    result += ")"
    return(result)
    
  def add_word(word):
    if len(word) > 0:
      wanted_character = word[0]
      word = word[1:]
      if counter[wanted_character] > 0:
        next_node = self.find_next(wanted_character)
      else:
        next_node = self.create_node(wanted_character)   
      next_node.add_word(word)
    else:
      next_node = self.create_node(" ")
    self.counter[wanted_character] += 1

# ~ def find(starting_node):
  # ~ word=input("zadejte slovo: ")
  # ~ word+=">"
  # ~ actual_node=starting node                #zkoumaný uzel
  # ~ while len(slovo)>0:
    # ~ print(slovo)
    # ~ zkpismeno=slovo[0]
    # ~ slovo=slovo[1:]
    # ~ dalsi=zkuzel.zjistidalsi(zkpismeno)
    # ~ if dalsi==False:
      # ~ return("Slovo ve slovníku není")
    # ~ zkuzel=dalsi
  # ~ pocet=zkuzel.pocet
  # ~ return("Slovo ve slovníku je "+str(pocet)+"krát")
def add_to_tria(starting_node, dataset):
  full_text = open(dataset, "r")
  lines = full_text.readlines()
  word = ""
  for line in lines:
    for character in line:
      if character != " ":
        word += character
      elif len(word) > 0:
        starting_node.add_word(word)
        word = ""
  full_text.close()
  return(starting_node)

def export_tria(starting_node):
  to_save = starting_node.save()
  export_file = open("tria.txt","w")
  export_file.write(to_save)
  export_file.close()

