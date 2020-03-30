from tria import node, add_to_tria

starting_node = node(None, "<")
directory = input("where do you want to train from? ")
print("training...")
add_to_tria(starting_node, directory)
print("exporting...")
to_save = starting_node.save()
to_save = to_save[2:-1]
export_file = open("tria.txt", "w", encoding = "utf-8")
export_file.write(to_save)
export_file.close()
print("finished")
