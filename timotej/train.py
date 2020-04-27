from tria import node

ACCEPTED = list("AÁBCČDĎEĚÉFGHIÍJKLMNŇOÓPQRŘSŠTŤUÚŮVWXYÝZŽaábcčdďeěéfghiíjklmnňoópqrřsštťuůúvwxyýzž,.;„“?!()-")

def add_words(starting_node, dataset):
  full_text = open(dataset, "r", encoding = "utf-8")
  lines = full_text.read()
  word = ""
  for character in lines:
    if character in ACCEPTED:
      word += character
    elif len(word) > 0:
      starting_node.add_word(word+">")
      word = ""
  full_text.close()
  return(starting_node)

def add_groups(starting_node, dataset):
  full_text = open(dataset, "r", encoding = "utf-8")
  lines = full_text.read()
  group = ""
  for character in lines:
    if character in ACCEPTED + [" "]:
      group += character
    else: group = ""
    if len(group) > 4:
      group = group[1:]
    try:
      if group[2] == " ":
        starting_node.add_word(group)
    except:  pass
  full_text.close()
  return(starting_node)

def export(starting_node, file_name):
  print(f"exporting to {file_name}...")
  to_save = starting_node.save()
  to_save = to_save[2:-1]
  export_file = open(file_name, "w", encoding = "utf-8")
  export_file.write(to_save)
  export_file.close()
  print("exported")
  
words = node(None, "<")
groups = node(None, "<")
directory = input("where do you want to train from? ")
print("training words...")
add_words(words, directory)
export(words, "words_tria.txt")
print("training groups...")
add_groups(groups, directory)
export(groups, "groups_tria.txt")


