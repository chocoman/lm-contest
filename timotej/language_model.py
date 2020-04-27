from . import tria
import os

class LanguageModel:
  def __init__(self):
    self.tria_words = tria.node(None, "<")
    self.tria_groups = tria.node(None, "<")
    self.predictions = 0
    self.unknown = 0
  def predict(self, prefix, statistics_mode = False):
    self.predictions += 1
    if len(prefix) == 0:
      way = "word"
      last_word = get_last_word(prefix)
      prediction = self.tria_words.predict(last_word)
      if prediction == ">": prediction = " "
    else:  
      if prefix[-1] in list(".,!?)-“;:"):
        way = "interpunction"
        prediction = " "
      elif prefix[-1] == " ":
        way = "group"
        prefix = prefix[-3:]
        prediction = self.tria_groups.predict(prefix)
      else:
        way = "word"
        prefix = get_last_word(prefix)
        prediction = self.tria_words.predict(prefix)
        if prediction == ">": prediction = " "
    if prediction == False:
      self.unknown += 1
      prediction = " "
    if statistics_mode:
      print(self.unknown, "/", self.predictions, "( =", self.unknown/self.predictions*100, "% )")
      return(prediction, way)
    else:
      return(prediction)
    
  def load(self, directory):
    tria.load_tria(self.tria_words, os.path.join(directory, "words_tria.txt"))
    tria.load_tria(self.tria_groups, os.path.join(directory, "groups_tria.txt"))

def get_last_word(string):
  word = ""
  for i in range(len(string)):
    i += 1
    if string[-i] in list("AÁBCČDĎEĚÉFGHIÍJKLMNŇOÓPQRŘSŠTŤUÚŮVWXYÝZŽaábcčdďeěéfghiíjklmnňoópqrřsštťuůúvwxyýzž,."):
      word = string[-i]+word
    else: break
  return word
