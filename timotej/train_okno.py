import tkinter as tk
from tkinter import filedialog as fd
import sys

from tria import node

ACCEPTED = list("AÁBCČDĎEĚÉFGHIÍJKLMNŇOÓPQRŘSŠTŤUÚŮVWXYÝZŽaábcčdďeěéfghiíjklmnňoópqrřsštťuůúvwxyýzž,.;„“?!()-")

class interface:
  def __init__(self):
    self.window = tk.Tk()
    self.window.title("trainer")
    self.label1 = tk.Label(self.window, text = "train from")
    self.label2 = tk.Label(self.window, text = "export groups to")
    self.label3 = tk.Label(self.window, text = "export words to")
    self.entry1 = tk.Entry(self.window)
    self.entry2 = tk.Entry(self.window)
    self.entry3 = tk.Entry(self.window)
    self.button1 = tk.Button(self.window, text = "choose", command = self.choose_dataset)
    self.button2 = tk.Button(self.window, text = "choose", command = self.choose_groups_export_file)
    self.button3 = tk.Button(self.window, text = "choose", command = self.choose_words_export_file)
    self.button_finish = tk.Button(self.window, text = "train", command=self.finish)
    self.label1.grid()
    self.label2.grid()
    self.label3.grid()
    self.entry1.grid(column = 1, row = 0)
    self.entry2.grid(column = 1, row = 1)
    self.entry3.grid(column = 1, row = 2)
    self.button1.grid(column = 2, row = 0)
    self.button2.grid(column = 2, row = 1)
    self.button3.grid(column = 2, row = 2)
    self.button_finish.grid(columnspan = 3)
  def choose_dataset(self):
    dataset = fd.askopenfilename(filetypes=[("Text files", "*.txt")])
    self.entry1.delete(0, "end")
    self.entry1.insert(0, dataset)
  def choose_groups_export_file(self):
    exp_file = fd.asksaveasfilename(filetypes=[("Text files", "*.txt")])
    self.entry2.delete(0, "end")
    self.entry2.insert(0, exp_file)
  def choose_words_export_file(self):
    exp_file = fd.asksaveasfilename(filetypes=[("Text files", "*.txt")])
    self.entry3.delete(0, "end")
    self.entry3.insert(0, exp_file)
  def finish(self):
    dataset = self.entry1.get()
    groups_exp = self.entry2.get()
    words_exp = self.entry3.get()
    self.window.destroy()
    train(dataset, groups_exp, words_exp)

def add_words(starting_node, dataset):
  full_text = open(dataset, "r", encoding = "utf-8")
  lines = full_text.read()
  word = ""
  length = len(lines)
  for i in range(length):
    if round((i/length)%0.0001, 7)==0:
      sys.stdout.write(f"\r{round((i/length)*100, 2)}%"))
      sys.stdout.flush()
    character = lines[i]
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
  length = len(lines)
  for i in range(length):
    if round((i/length)%0.0001, 7)==0:
      sys.stdout.write(f"\r{round((i/length)*100, 2)}%"))
      sys.stdout.flush()
    character = lines[i]
    if character in ACCEPTED + [" "]:
      group += character
    else: group = ""
    if len(group) > 6:
      group = group[1:]
    try:
      if group[-2] == " ":
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

def train(dataset, groups_exp, words_exp):  
  directory = dataset

  if len(words_exp)>0:
    print("training words...")
    words = node(None, "<")
    add_words(words, directory)
    export(words, words_exp)
  if len(groups_exp)>0:
    print("training groups...")
    groups = node(None, "<")
    add_groups(groups, directory)
    export(groups, groups_exp)

i = interface()

tk.mainloop()

