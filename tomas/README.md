#Natrénování modelu

Stáhněte korpus české wikipedie:

https://lindat.mff.cuni.cz/repository/xmlui/bitstream/handle/11234/1-2735/cs.txt.gz?sequence=54&isAllowed=y

a rozbalte ho zde.

Současnou složku contest odstraňte nebo přesuňte a spusťte příkaz
```

python3 train.py --savedir contest cs.txt

python3 contest_custom.py ./data/cs-CZ/ustava.txt
```
Předtrénovaný model je už uložen ve složce contest. 
