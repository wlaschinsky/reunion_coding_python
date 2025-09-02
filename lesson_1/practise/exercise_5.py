# # EXERCISES: Vypiš délku, verzi velkými písmeny, abecedně seřazený seznam znaků (pomocí sorted()), a poslední 3 znaky pomocí slicingu.

# ceny = [249.9, 99.0, 149.5, 799.0, 35.0]

# print(len(ceny))
# print(min(ceny))
# print(max(ceny))
# print(sum(ceny))
# print(round(sum(ceny)/len(ceny),2))

# # EXERCISES: Vypiš délku, verzi velkými písmeny, abecedně seřazený seznam znaků (pomocí sorted()), a poslední 3 znaky pomocí slicingu.

# t = "Playwright Testing"
# print(len(t))
# print(t.upper())
# print(sorted(t))
# print(t[-3:])

# # EXERCISES: Seřaď je vzestupně do nové proměnné (původní neměň) a vypiš součet absolutních hodnot.

# cisla = [3, -7, 10, -2, 0]
# # rozepsany zapis
# soucet = 0
# for x in cisla:    #for x in seznam: znamená „vezmi každý prvek ze seznamu a ulož ho postupně do proměnné x“.
#     soucet += abs(x)   # k součtu přičítám absolutní hodnotu čísla
# print(soucet)

# # zkraceny zapis
# sum(abs(x) for x in cisla)

# cisla_2 = sorted(cisla)
# print(sum(cisla_2))


# # tip: = vytvoř nový list tak, že z každého prvku uděláš abs(x).
# cisla_abs = []
# for x in cisla:
#     cisla_abs.append(abs(x))
# print(sum(cisla_abs))

# # 1.	cisla = [3, -7, 10, -2, 0]
# # → máš seznam čísel.
# # 	2.	cisla_abs = []
# # → vytvoříš prázdný seznam.
# # 	3.	for x in cisla:
# # → Python vezme každé číslo z cisla a uloží ho do proměnné x.
# # 	•		1.	průchod: x = 3
# # 	•		2.	průchod: x = -7
# # 	•		3.	průchod: x = 10
# # 	•		4.	průchod: x = -2
# # 	•		5.	průchod: x = 0
# # 	4.	cisla_abs.append(abs(x))
# # 	•	abs(x) → funkce abs vezme absolutní hodnotu (-7 → 7).
# # 	•	.append(...) → přidá výsledek do seznamu cisla_abs.
# # Vývoj cisla_abs krok po kroku:
# # 	•	po 1. průchodu: [3]
# # 	•	po 2. průchodu: [3, 7]
# # 	•	po 3. průchodu: [3, 7, 10]
# # 	•	po 4. průchodu: [3, 7, 10, 2]
# # 	•	po 5. průchodu: [3, 7, 10, 2, 0]
# # 	5.	print(sum(cisla_abs))
# # 	•	sum() → sečte všechny prvky [3, 7, 10, 2, 0] = 22.


# # EXERCISES: Vytvoř nový seřazený seznam jmen bez ohledu na velikost písmen (hint: sorted(jmena, key=str.lower)).

# jmena = ["Anna", "adam", "Pavel", "petr"]
# jmena_2 = sorted(jmena, key=str.lower)


# # EXERCISES: Vypiš je ve formátu #1: Login, #2: Checkout, #3: Dashboard - enumerate().

# projekty = ["Login", "Checkout", "Dashboard"]

# projekty = ["Login", "Checkout", "Dashboard"]

# i = 0   #→ nastavíš pomocnou proměnnou i, která začne na hodnotě 0.(Slouží jako čítač/pořadí.)
# for projekt in projekty:      #	•	projekty je název seznamu (listu) •	projekt je jedna položka z toho seznamu, do které se přiřazuje hodnota postupně.
#     print(i, projekt)
#     i += 1      # po každém průchodu se čítač zvýší o 1, aby ukazoval na další pořadí.

# for i in range(len(projekty)):
#     print(i, projekty[i])
    
# # zacatek cislovani od 1:  
# for i, projekty in enumerate(projekty, start=1):
#     print("#", i, ":", projekty)
    
    
    
# ---------------------------------------------
# # EXERCISES: CVIČENÍ – Vestavěné funkce a metody (bez if)
# ---------------------------------------------
# Úkoly: jen funkce a metody, žádné podmínky ani složité smyčky
# ---------------------------------------------

# 1. len(), min(), max(), sum(), round()
# Máš seznam čísel:
import abc


cisla = [15, 42, 3, 88, 23]
# Úkoly:
# - Vypiš délku seznamu
# - Najdi minimum
# - Najdi maximum
# - Spočítej součet
# - Spočítej průměr (zaokrouhlený na 1 desetinné místo)

print(len(cisla))
print(min(cisla))
print(max(cisla))
print(sum(cisla))
print(round(sum(cisla) / len(cisla), 2))

# 2. upper(), lower(), sorted(), slicing
text = "Python is Fun"
# Úkoly:
# - Vypiš délku řetězce
# - Vypiš verzi velkými písmeny
# - Vypiš verzi malými písmeny
# - Vypiš seřazené znaky pomocí sorted()
# - Vypiš poslední 4 znaky pomocí slicingu
print(len(text))
print(text.upper())
print(text.lower())
print(sorted(text))
print(text.sort())
print(text[-4:])



# 3. abs(), sorted(), sum()
cisla = [4, -9, 12, -3, 0]
# Úkoly:
# - Vytvoř nový list abs_cisla, kde budou absolutní hodnoty všech čísel
#   (klasicky pomocí for a append())
# - Seřaď tento nový list vzestupně
# - Sečti hodnoty v abs_cisla
abs_cisla=[]
for cislo in cisla: 
    abs_cisla.append(abs(cislo))
sorted(abs_cisla)
print(abs_cisla)
print(sum(abs_cisla))

# 4. str(), int(), float()
# Úkoly:
# - Převeď číslo 123 na text a vypiš ho společně se stringem "abc" (pomocí +)
# - Převeď text "456" na číslo a přičti k němu 44
# - Převeď text "3.14" na číslo a vynásob ho 2
cislo_str = str(123)
abc_str = "abc"
print(cislo_str + abc_str)
text = "3.14"
text_num = float(text)
print(text_num * 2)

# 5. enumerate()
projekty = ["Login", "Checkout", "Dashboard", "Reports"]
# Úkoly:
# - Vypiš všechny projekty takto:
#   #1: Login
#   #2: Checkout
#   #3: Dashboard
#   #4: Reports
#   Použij enumerate() s start=1

# dobre
i = 1                     # začínáme od 1
for projekt in projekty:
    print("#" + str(i) + ":", projekt)
    i = i + 1             # ručně zvyšujeme čítač

# spravne s enumerate
for i, projekt in enumerate(projekty, start=1):
    print("#" + str(i) + ":", projekt)
    
# spatne
for projekt in projekty: 
    print(enumerate(projekt, start=1))



# METODA vs FCE jak si to zapamatovat 