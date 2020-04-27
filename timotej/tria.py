class node:
  def __init__(self, upper_node, character):
    self.upper_node = upper_node
    self.character = character
    self.lower_nodes = []
    self.likelihood = 0
    
  def create_node(self, character):
    next_node = node(self, character)
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
    result += str(self.likelihood)
    for lower in self.lower_nodes:
      result += lower.save()
    result += "§"
    return(result)
    
  def add_word(self, word):
    wanted_character = word[0]
    word = word[1:]
    next_node = self.find_next(wanted_character)
    if next_node == False:
      next_node = self.create_node(wanted_character)
    next_node.likelihood += 1
    if len(word) > 0:
      next_node.add_word(word)

  def predict(self, word):
    if len(word) == 0:
      best = None
      best_likelihood =0
      for node in self.lower_nodes:
        if node.likelihood > best_likelihood:
          best = node.character
          best_likelihood = node.likelihood
      if best == None:
        # ~ print("no idea")
        best = False
      return(best)
    else:
      wanted_character = word[0]
      word = word[1:]
      next_node = self.find_next(wanted_character)
      if next_node == False:
        # ~ print("no idea")
        return(False)
      else:
        return(next_node.predict(word))


def load_tria(starting_node, file_name):
  print(f"loading {file_name}...")
  exported = open(file_name, "r", encoding = "utf-8")
  string = exported.read()
  actual_node = starting_node
  actual_node.likelihood = ""
  for character in string:
    if character in list("1234567890"):
      actual_node.likelihood += character
    elif character == "§":
      actual_node.likelihood = int(actual_node.likelihood)
      actual_node = actual_node.upper_node
    else:
      actual_node = actual_node.create_node(character)
      actual_node.likelihood = ""
  return(starting_node)
