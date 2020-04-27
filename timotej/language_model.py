from . import tria
import os

class LanguageModel:
  def __init__(self):
    self.tria_words = tria.node(None, "<")
    self.tria_quartets = tria.node(None, "<")
    self.predictions = 0
    self.unknown = 0
  def predict(self, prefix):
    self.predictions += 1
    if len(prefix) == 0:
      last_word = get_last_word(prefix)
      prediction = self.tria_words.predict(last_word)
      if prediction == ">": prediction = " "
    else:  
      if prefix[-1] in list(".,!?)-“;:"):
        prediction = " "
      elif prefix[-1] == " ":
        prefix = prefix[-3:]
        prediction = self.tria_quartets.predict(prefix)
      else:
        prefix = get_last_word(prefix)
        prediction = self.tria_words.predict(prefix)
        if prediction == ">": prediction = " "
    if prediction == False:
      self.unknown += 1
      print(f"i have no idea what could be after {prefix}")
      prediction = " "
    print(self.unknown, "/", self.predictions, "( =", self.unknown/self.predictions*100, "% )")
    return(prediction)
    
  def load(self, directory):
    tria.load_tria(self.tria_words, os.path.join(directory, "words_tria.txt"))
    tria.load_tria(self.tria_quartets, os.path.join(directory, "quartets_tria.txt"))

def get_last_word(string):
  word = ""
  for i in range(len(string)):
    i += 1
    if string[-i] in list("AÁBCČDĎEĚÉFGHIÍJKLMNŇOÓPQRŘSŠTŤUÚŮVWXYÝZŽaábcčdďeěéfghiíjklmnňoópqrřsštťuůúvwxyýzž,."):
      word = string[-i]+word
    else: break
  return word
