import tria

class LanguageModel:
  def __init__(self):
    self.prophet = tria.node(None, "<")

  def predict(self, prefix):
    print(f"thinking about{prefix}")
    last_word = get_last_word(prefix)
    print(f"thinking about what could be after{last_word}")
    prediction = self.prophet.predict(last_word)
    return(prediction)
    
  def load(self, memory):
    tria.load_tria(self.prophet, memory)

def get_last_word(string):
  word = ""
  for i in range(len(string)):
    print(string[-i])
    if string[-i] in list("AÁBCČDĎEĚÉFGHIÍJKLMNŇOÓPQRŘSŠTŤUÚŮVWXYÝZŽaábcčdďeěéfghiíjklmnňoópqrřsštťuůúvwxyýzž,."):
      word = string[-i]+word
    else: break
  return word

model = LanguageModel()
model.load("tria.txt")
print(model.predict("schválně jestli se chyt"))
