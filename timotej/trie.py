class node:
  def __init__(self, character):
    self.character = character
    self.lower_nodes = []
    
  def create(self, character):
    # ~ print("tvořím nový uzel \""+pismeno+"\"")
    next_node = node(character)
    self.lower_nodes.append(next_node)
    return(next_node)
    
  def find_next(self, wanted_character):
    if len(self.lower_nodes)  == 0:
      return(False)
    for lower in self.lower_nodes:
      if lower.character == wanted_character:
        return(lower)
    return(False)
    
  def ulozse(self):
    odpoved=self.pismeno
    for poduzel in self.poduzly:
      odpoved+=poduzel.ulozse()
    odpoved+=")"
    return(odpoved)
    
class koncovyuzel:
  def __init__(self):
    self.pocet=1
    self.pismeno=">"
  def ulozse(self):
    odpoved=self.pismeno+str(self.pocet)+")"
    return(odpoved)
        
    
def pridejslovo(slovo):
  zkuzel=zacatek                #zkoumaný uzel
  while len(slovo)>0:
    # ~ print(slovo)
    zkpismeno=slovo[0]
    slovo=slovo[1:]
    dalsi=zkuzel.zjistidalsi(zkpismeno)
    if dalsi==False:
      dalsi=zkuzel.vytvordalsi(zkpismeno)      
    zkuzel=dalsi
  dalsi=zkuzel.zjistidalsi(">")
  if dalsi==False:
    dalsi=zkuzel.vytvordalsi(">")
  else:
    dalsi.pocet+=1

def najdi(zacatek):
  slovo=input("zadejte slovo: ")
  slovo+=">"
  zkuzel=zacatek                #zkoumaný uzel
  while len(slovo)>0:
    print(slovo)
    zkpismeno=slovo[0]
    slovo=slovo[1:]
    dalsi=zkuzel.zjistidalsi(zkpismeno)
    if dalsi==False:
      return("Slovo ve slovníku není")
    zkuzel=dalsi
  pocet=zkuzel.pocet
  return("Slovo ve slovníku je "+str(pocet)+"krát")

zacatek=uzel("<")

soubor=open("text.txt","r")
radky=soubor.readlines()
slovo=""
for radek in radky:
  radek=radek.lower()
  for znak in radek:
    if znak in (list("aábcčdďeéěfghiíjklmnňoópqrřsštťuúůvwxyýzž")):
      slovo+=znak
    elif len(slovo)>0:
      pridejslovo(slovo)
      slovo=""
soubor.close()

kulozeni=zacatek.ulozse()
ulozene=open("trie.txt","w")
ulozene.write(kulozeni)
ulozene.close()

while True:
  print(najdi(zacatek))


