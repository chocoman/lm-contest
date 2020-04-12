from . import tria
import os

class LanguageModel:
  def __init__(self):
    self.tria_words = tria.node(None, "<")
    self.tria_quartets = tria.node(None, "<")

  def predict(self, prefix):
    if prefix[-1] in list(".,!?)-“;:"):
      prediction = " "
    elif prefix[-1] == " ":
      last_three = prefix[-3:]
      prediction = self.tria_quartets.predict(last_three)
    else:
      last_word = get_last_word(prefix)
      prediction = self.tria_words.predict(last_word)
      if prediction == ">": prediction = " "
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
