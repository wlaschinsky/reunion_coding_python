# TOPIC: 

print(), type(), len(), int(), float(), str(), round(), abs(),
min(), max(), sum(), sorted(), enumerate(), range()

+-----------+----------------------------------------------+ Příklad
| Funkce    | K čemu slouží                                |
+-----------+----------------------------------------------+---------------------------------------------+
| type()    | Vrátí typ hodnoty                            | type(3.14)  -> <class 'float'>
| len()     | Délka sekvence (str, list, tuple, ...)       | len("Python") -> 6
| int()     | Převod na celé číslo                         | int("42")    -> 42
| float()   | Převod na desetinné číslo                    | float("3.5") -> 3.5
| str()     | Převod na řetězec                            | str(123)     -> "123"
| round()   | Zaokrouhlení (volitelně na n desetinných)    | round(3.1415, 2) -> 3.14
| abs()     | Absolutní hodnota                            | abs(-7)      -> 7
| min()/max()| Minimum/maximum v iterovatelném objektu     | max([3,8,2]) -> 8
| sum()     | Součet čísel                                 | sum([1,2,3]) -> 6
| sorted()  | Vrátí seřazenou kopii                        | sorted([3,1,2]) -> [1,2,3]
| enumerate()| Číslované procházení v for-cyklu            | enumerate(["a","b"]) -> (0,"a"), (1,"b")
| range()   | Generátor posloupnosti čísel                 | range(3) -> 0,1,2
+-----------+----------------------------------------------+---------------------------------------------+

tips: 
	•	Průměr čísel: avg = sum(hodnoty) / len(hodnoty) (pozor na prázdný seznam → ZeroDivisionError).
	•	Seřazení beze změny původního listu: nova = sorted(puvodni).
	•	Zaokrouhlení: round(x, 2) (na 2 desetinná místa).
	•	Součet jen části seznamu (slicing umíš!): sum(ceny[:3]).

len(x)        → vestavěná funkce (globální)
x.upper()     → metoda objektu (string má svoje metody)
sorted(x)     → vestavěná funkce
x.append(y)   → metoda objektu (list má svoje metody)
enumerate(x)  → vestavěná funkce (vrací index + hodnotu)


from inspect import Parameter


text = "Samuel"
print(type(text))      # <class 'str'>
print(dir(text))       # seznam metod pro str
help(str.upper)        # detailní nápověda k metodě upper()


do funkce dam Parameter
len(x)        → vestavěná funkce (globální)


do etod objektu - musim k objetku priradit tu metodu 
x.upper()     → metoda objektu (string má svoje metody)




Metoda vs. Funkce (polopatě)
	•	Funkce je „obecná“ – voláš ji jako funkce(hodnota).
Příklady vestavěných funkcí:
	•	len("Python") → vrátí délku (6)
	•	abs(-7) → absolutní hodnota (7)
	•	round(3.1415, 2) → 3.14
	•	sorted([3,1,2]) → vrátí nový seřazený list
	•	Metoda „patří objektu“ – voláš ji jako objekt.metoda(...).
Příklady metod:
	•	"ahoj".upper() → "AHOJ" (metoda typu str)
	•	["a", "b"].append("c") → přidá do listu "c" (metoda typu list)
	•	"text".replace("t","T") → "Text"

💡 Mnemotechnická pomůcka:
	•	len(x) = „zeptám se Pythonu“ (globální funkce)
	•	x.upper() = „řeknu objektu x, ať se sám upraví/vrátí upravenou verzi“ (metoda daného typu)

⸻

Chceš, abych ti celek seskládal do jednoho „čistého“ souboru s komentáři (hotový materiál do editoru), nebo si to radši pošleš po částech do svých poznámek?


# ---------------------------------------------
# ROZDÍL MEZI sorted() A .sort()
# ---------------------------------------------
# sorted()  → je VESTAVĚNÁ FUNKCE
# .sort()   → je METODA objektu list
#
# Hlavní rozdíl:
# - sorted() vrací NOVÝ seřazený list, původní nemění
# - .sort() mění list NA MÍSTĚ a vrací None
#
# Obě podporují parametry:
#   key=      → funkce pro určení podle čeho řadit
#   reverse=  → True/False, jestli řadit sestupně
# ---------------------------------------------


# PŘÍKLAD 1 – sorted()
cisla = [3, 1, 4, 2]
nove = sorted(cisla)        # předávám objekt (list), chci kopii
print("Původní:", cisla)    # [3, 1, 4, 2] (nemění se)
print("Nový:", nove)        # [1, 2, 3, 4]


# PŘÍKLAD 2 – .sort()
cisla = [3, 1, 4, 2]
vysledek = cisla.sort()      # mění se přímo původní list
print("Výsledek volání sort():", vysledek)  # None
print("List po sort():", cisla)             # [1, 2, 3, 4]


# PŘÍKLAD 3 – parametry reverse a key
jmena = ["Adam", "petr", "anna"]

# sorted – case-insensitive
print(sorted(jmena, key=str.lower))  # ['Adam', 'anna', 'petr']

# sorted – sestupně
print(sorted(jmena, reverse=True))   # ['petr', 'anna', 'Adam']

# .sort – case-insensitive, mění list
jmena.sort(key=str.lower)
print(jmena)  # ['Adam', 'anna', 'petr']