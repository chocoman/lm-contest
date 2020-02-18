# lm-contest


## Pravidla soutěže:

Do soutěže můžete každý týden odevzdat svůj natrénovaný jazykový model.
Uzávěrka je každé pondělí do 8:00 ráno, dokud soutěž neskončí.

Odevzdaný jazykový model bude jedna složka, jejíž jméno bude vaše křestní jméno
bez háčků a čárek s malým písmenem. Složku zabalenou do zipu, pošlete e-mailem
na adresu spanel@arcig.cz.

Složka půjde použít jako pythonový package a bude mimo jiné obsahovat modul
jménem language_model.py, ve kterém bude třída LanguageModel. Ta bude mít
konstruktor bez argumentů a kromě něj metodu predict_next_character(prefix),
která dostane prefix libovolné délky a vydá jediné písmeno - předpověď, jaké
písmeno následuje bezprostředně za prefixem. Vše musí fungovat bez jakékoli
další manipulace, nastavování, nebo spouštění čehokoli jiného než konstruktoru
a funkce predict_next_character(prefix). Speciálně pokud je jazykový model potřeba
trénovat, musí být ve složce už natrénovaný a uložený.

Ve složce musí kromě natrénovaného jazykového modelu být i instrukce k natrénování.

Složka example je příkladem správně připraveného jazykového modelu.

Každé pondělí se zvolí první hlavní zpráva, která vyjde na www.seznamzpravy.cz
po 8:00. Pro každý odstavec (včetně nadpisů) se jazykovému modelu postupně pošlou
všechny jeho prefixy (délky 0, 1, 2 a tak dále) k předpovězení následujícího písmena.
Skóre jazykového modelu bude poměr správně předpovězených znaků. Počítají se všechny
znaky, včetně diakritiky, konce řádku a cizích písmen.

