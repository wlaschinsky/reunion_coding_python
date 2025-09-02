# TOPIC: TUPLE -> Tuple je jako list, ale nemění se. Je to neměnná (immutable) kolekce hodnot. tuple (česky n-tice), což je takový „bratranec“ listu – podobný, ale neměnitelný. 

# +--------------------+---------------------+---------------------------+
# |                    | list                | tuple                     |
# +--------------------+---------------------+---------------------------+
# | Zápis              | ["a", "b", "c"]     | ("a", "b", "c")           |
# | Měnitelnost        | ✅ lze měnit         | ❌ nelze měnit             |
# | Použití            | běžné kolekce       | pevné, neměnné hodnoty    |
# | Paměť/výkon        | pomalejší           | rychlejší (často)         |
# +--------------------+---------------------+---------------------------+

list_mest = ["Praha", "Brno", "Ostrava"]
tuple_mest = ("Praha", "Brno", "Ostrava")

print(list_mest[0])     # Praha
print(tuple_mest[0])    # Praha

list_mest[1] = "Plzeň"  # ✅ změna OK
tuple_mest[1] = "Plzeň" # ❌ TypeError – tuple nejde měnit

# EXERCISES: 1.	Vytvoř tuple se třemi oblíbenými jídly.
# EXERCISES: 2.	Vypiš druhé jídlo.
# EXERCISES: 3.	Zkus přepsat první jídlo – co se stane?
# EXERCISES: 4.	Zkus vypsat tuple pozpátku pomocí slicing/striding.
# EXERCISES: 5.	Pomocí type() ověř, že proměnná je tuple.



meals = ("hranolky", "hambac", "smazak")
print(meals[1])
# hambac
meals[1]="svickova"
# Traceback (most recent call last):
#   File "<python-input-181>", line 1, in <module>
#     meals[1]="svickova"
#     ~~~~~^^^
# TypeError: 'tuple' object does not support item assignment
print(meals[::-1])
# ('smazak', 'hambac', 'hranolky')
print(type(meals))
# <class 'tuple'>
emin


# TOPIC: vnorena struktura -> Tuple může obsahovat další tuple nebo listy, což umožňuje vytvářet složitější struktury dat.

# List obsahující tuple:
	# •	data[0] → ("Karel", 21)
	# •	data[0][1] → 21
data = [("Karel", 21), ("Tereza", 23)]

# Tuple obsahující listy:
data = (["Karel", 21], ["Tereza", 23])
	# •	data[0][0] → "Karel"
 
#  📛 Pozor: I když data je tuple (neměnná), ty listy uvnitř můžeš měnit!
data[0][1] = 22  # ✅ Platí – upravuješ vnitřní list
data[0] = ["Petr", 20]  # ❌ Chyba – tuple jako celek nejde měnit

# +-------------------------+-------------------------------+
# | Co máš                  | Co můžeš udělat               |
# +-------------------------+-------------------------------+
# | list obsahující tuple   | ✅ přidat, ❌ upravit tuple    |
# | tuple obsahující list   | ❌ přidat, ✅ upravit list     |
# +-------------------------+-------------------------------+


# -------------------------------------------
# TUPLE OBSAHUJÍCÍ LISTY – příklady a poznámky
# -------------------------------------------

# Vytvoření tuple, který obsahuje dva listy (každý list má jméno a věk)
zaznam = (["Karel", 21], ["Tereza", 23])

# ✅ Přístup k jednotlivým prvkům:
print(zaznam[0])        # ['Karel', 21]
print(zaznam[1][0])     # 'Tereza'
print(zaznam[1][1])     # 23

# ✅ Změna hodnoty ve vnitřním listu:
zaznam[1][1] = 24       # Změníme věk Terezy
print(zaznam[1])        # ['Tereza', 24]

# ✅ Přidání nového údaje do vnitřního listu:
zaznam[1].append("studentka")   # Přidáme další informaci
print(zaznam[1])        # ['Tereza', 24, 'studentka']

# ❌ Nelze změnit celý záznam – tuple jako celek je neměnný:
# zaznam[1] = ["Eliška", 22]  # → vyhodí chybu!

# ✅ Ale vnitřní list měnit můžeme – např. přidání oboru Karlovi:
zaznam[0].append("IT")
print(zaznam[0])        # ['Karel', 21, 'IT']


# EXERCISES:  1. Vytvoř tuple se dvěma listy: ["Samuel", 34] a ["Teo", 5]
lidi = (["Samuel, 34"], ["Teo", 5])

# EXERCISES:  Přidej ke každému oblíbenou barvu
lidi[0].append("modrá")  # Přidá barvu k Samuelovi
lidi[1].append("zelená")  # Přidá barvu k Teovi

# EXERCISES:   Změň Tea na věk 6
lidi[1][1] = 6  # Změní věk Tea na 6

# EXERCISES:   Vypiš celý tuple
print(lidi)