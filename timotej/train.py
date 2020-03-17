from tria import node, add_to_tria, export_tria

starting_node = node(None, "<")
directory = input("where do you want to train from? ")
print("training...")
add_to_tria(starting_node, directory)
print("exporting...")
export_tria(starting_node)
print("finished")
