# TOPIC: ZÁKLADY PYTHONU

print("Hello!")
# viceradkovy print
print("""
Hello! 
neco.
""")
print(2**2)
# deleni s float
print(4/2)
# deleni bez float
print(4//2)
# prace se stringem - escapovani specialnich znaku jako "" a rozdeleni na vice radku 
print("I'm happy\n, said \"Why are you happy?\" ")
# overeni datoveho typu
print(type(210))
# pretypovani hodnoty
print(2 + float("2"))

# TOPIC: INDEXOVÁNÍ
# - slicing
# - striding
# - záporné indexy

# zezadu -1, -2, -3... začátek = poslední znak, konec = první znak
# zepredu 0, 1, 2... začátek = první znak, konec = poslední znak

text = "Python"
print(text[0])    # P
print(text[-1])   # n
print(text[-3])   # h


var = "Petr"
var_num = len(var)
for i in range(var_num):
    print(var[i])

# TOPIC: SLICING, STRIDING
# [start:end]  slicing (úsek)
# [start:end:step] striding (úsek + krokování)
# [::-1] obrácení celého řetězce
# Striding = krokování v rámci slicingu

# +-------------------+-----------------------------+
# | Co je třeba       | Kdy funguje                 |
# +-------------------+-----------------------------+
# | Kladný krok (+1)  | pouze když start < end      |
# | Záporný krok (-1) | pouze když start > end      |
# +-------------------+-----------------------------+

# +---------------------+------------+---------------------------------------------+
# | Zápis               | Funguje?   | Co dělá                                     |
# +---------------------+------------+---------------------------------------------+
# | text[2:5]           | Ano        | Vypíše znaky s indexy 2,3,4                 |
# | text[5:2]           | Ne         | Směr neodpovídá (step defaultně +1)        |
# | text[5:2:-1]        | Ano        | Vypíše znaky s indexy 5,4,3                 |
# | text[2:5:-1]        | Ne         | Směr neodpovídá (step -1, ale start < end) |
# | text[::-1]          | Ano        | Celý text pozpátku                          |
# | text[::2]           | Ano        | Každý druhý znak zleva                     |
# | text[::-3]          | Ano        | Každý třetí znak zprava                    |
# +---------------------+------------+---------------------------------------------+

soubor = "report.txt"
nazev = soubor[:-4]
print(nazev)  # "report"

# fcnejsi ekvivalent
soubor = "report.txt"
pozice_tečky = soubor.rfind(".")  # najdu index poslední tečky
nazev = soubor[:pozice_tečky]     # vezmu od začátku po tečku (ne včetně)
print(nazev)  # "report"

# získání přípony tečka 
soubor = "report.txt"
pozice_tečky = soubor.rfind(".")
if pozice_tečky != -1:
    pripona = soubor[pozice_tečky+1:]  # vezmu až za tečkou
else:
    pripona = ""
print(pripona)  # "txt"


# EXERCISES: ULOHA: Pomocí operací nad řetězcem a spojování řetězců vypište daný řetězec nejdříve normálně, poté pozpátku, poté každý třetí znak a poté poslední tři znaky. Vložte mezi segmenty nějaký oddělovač. Bude to například takto:
var = "Samuel Wlaschinsky"
print(var)
print(var[::-1])
print(var[::3])
print(var[-3:])  # poslední 3 znaky

# EXERCISES: Vypiš první tři znaky řetězce
var_text = "Python"
print(var_text[:3])  # nebo var_text[0:3]

# EXERCISES: Vypiš řetězec pozpátku, Použij striding a vypiš text úplně pozpátku.text = "Python", vypiš první tři znaky

text = "Python"
print(text[0:2])   # nebo text[:2] 

# EXERCISES: Vypiš každý druhý znak od začátku, Z řetězce "abcdefghij" vypiš každý druhý znak.
var_text = "abcdefghij"
print(var_text[::2])  # nebo var_text[0:len(var_text):2]

# EXERCISES: Vypiš posledních pět znaků, Z řetězce "Automobilismus" vypiš posledních 5 znaků.
var_text = "Automobilismus"
print(var_text[-5:])

# EXERCISES: Vypiš všechny znaky mezi indexem 2 a 8, Z řetězce "Banánovník" vypiš znaky od indexu 2 do indexu 7.
var_text = "Banánovník"
print(var_text[2:8])  # nebo var_text[2:7] (index 8 není zahrnut)

# EXERCISES: Vypiš každý třetí znak od konce - Vezmi řetězec "abcdefghijklmno" a vypiš každý třetí znak, začínaje od konce. Tip: Striding s krokem -3, tedy [:: -3], ale musíš začít správně od konce.
var_text = "abcdefghijklmno"
print(var_text[::-3])  # nebo var_text[-1::-3] (začíná od posledního znaku a jde pozpátku)

# EXERCISES: Ořízni řetězec do poloviny - Z řetězce "Programování" vytvoř nový řetězec, který obsahuje jen první polovinu písmen. počítáš délku pomocí len(). Vezmeš [ : len(text)//2 ].

# EXERCISES: Najdi a odděl příponu souboru - soubor = "dokumentace_finalni_verze.docx", Název souboru (bez přípony), Příponu (docx)
file = "dokumentace_finalni_verze.docx"
print(file[:-5])  # Název souboru bez přípony

# EXERCISES: Vytvoř šifru - "geheimnis" a vytvoř nový řetězec, který obsahuje každý druhý znak pozpátku.
text = "geheimnis"
print(text[::-2])  # nebo text[-1::-2] (začíná od posledního znaku a jde pozpátku)  

# EXERCISES: Získáš poslední čtyři znaky řetězce „prototypování“ bez použití -4: (použij len())
var = "mikrotelefon"
print(var[len(var)//2:])

# EXERCISES: Z textu „EngetoPythonKurs“ vytvoř nový text, který je pozpátku a obsahuje pouze každé třetí písmeno
text = "EngetoPythonKurs"
print(text[::-3])  # začínáme od konce, krok -3

# EXERCISES: 
# +-------------+------------------+
# | Zápis       | Výsledek         |
# +-------------+------------------+
# | city[::2]   | ['Plzen', 'Louny'] |
# | city[1::2]  | ['Brno']         |
# | city[::-1]  | ['Louny', 'Brno', 'Plzen']  ← obráceně
# +-------------+------------------+

city = ["Plzen", "Brno", "Louny"]
# indexy:     0        1        2
print(city[::2])
# puvodne jsem spatne vychazel z toho, ze vysledek bude Brno. Ale uz prvni hodnota se pocita takze druhou to preskocvi a treti berem, protoze je to druha od te prvni, takze vysledek je Plzen a Louny

print(city[1::2])  # Začni na indexu 1 a jdi po dvou
# Výstup: ['Brno']


# EXERCISES: Vypiš města pozpátku v tuple
meals = ("hranolky", "hambac", "smazak")
print(meals[::-3])
# indexy:     0           1         2
#             ^           ^         ^
#             0           1         2
print(meals[::-3])  # vezme index 2 ("smazak"), pak 2-3 = -1 → konec
# výstup: ('smazak',)
# 📌 Tj. -3 znamená: přeskoč 2 prvky dozadu → ale tuple už žádné další nemá → výstup obsahuje jen poslední prvek.
