class uzel:
  def __init__(self,naduzel,pismeno):
    self.pismeno=pismeno
    self.poduzly=[]
    self.naduzel=naduzel
  def vytvordalsi(self,pismeno):
    if pismeno in (list("aábcčdďeéěfghiíjklmnňoópqrřsštťuúůvwxyýzž")):
      dalsiuzel=uzel(self,pismeno)
    if pismeno==">":
      dalsiuzel=koncovyuzel(self)
    self.poduzly.append(dalsiuzel)
    return(dalsiuzel)
  def zjistidalsi(self,zkpismeno):
    if len(self.poduzly)==0:
      return(False)
    for poduzel in self.poduzly:
      if poduzel.pismeno==zkpismeno:
        return(poduzel)
    return(False)

class koncovyuzel:
  def __init__(self,naduzel):
    self.pocet=""
    self.pismeno=">"
    self.naduzel=naduzel


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
  return("Slovo ve slovníku je "+pocet+"krát")


soubor=open("trie.txt","r")
text=soubor.read()
zacatek=uzel(0,"<")
aktualni=zacatek
for znak in text:
  if znak in (list(">aábcčdďeéěfghiíjklmnňoópqrřsštťuúůvwxyýzž")):
    novy=aktualni.vytvordalsi(znak)
    aktualni=novy
  elif znak==")":
    aktualni=aktualni.naduzel
  elif znak in list("1234567890"):
    aktualni.pocet+=znak
while True:
  print(najdi(zacatek))

