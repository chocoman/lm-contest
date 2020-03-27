from . import tria
import os

class LanguageModel:
  def __init__(self):
    self.prophet = tria.node(None, "<")

  def predict(self, prefix):
    print(f"thinking about {prefix}")
    last_word = get_last_word(prefix)
    print(f"thinking about what could be after {last_word}")
    prediction = self.prophet.predict(last_word)
    return(prediction)
    
  def load(self, directory):
    tria.load_tria(self.prophet, os.path.join(directory, "tria_testing.txt"))

def get_last_word(string):
  word = ""
  for i in range(len(string)):
    i += 1
    print(string[-i])
    if string[-i] in list("AÁBCČDĎEĚÉFGHIÍJKLMNŇOÓPQRŘSŠTŤUÚŮVWXYÝZŽaábcčdďeěéfghiíjklmnňoópqrřsštťuůúvwxyýzž,."):
      word = string[-i]+word
    else: break
  return word
