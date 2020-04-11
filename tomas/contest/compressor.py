import os
f = open("model.txt", "r")
text = (f.read())
f.close()
s = open("newmodel.txt", "w")
compressed=""
for i in text:
    if (i!=" "):
        compressed+=i
s.write(compressed)
s.close

