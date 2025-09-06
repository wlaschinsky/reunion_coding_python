# # ---------------------------------------------
# # CVIČENÍ: Podmínky (if, elif, else, pass)
# # ---------------------------------------------

# # 1) Věk a vstup
# vek = 15
# # Úkol:
# # - Pokud je vek >= 18 → vytiskni "Může vstoupit"
# # - Jinak vytiskni "Vstup zakázán"

# if vek >= 18:
#     print("Muze vstoupit")
# else:
#     print("Vstup zakázán")
    
# # 2) Heslo
# heslo = "tajne"
# # Úkol:
# # - Pokud je heslo "tajne" → vytiskni "OK"
# # - Jinak vytiskni "Špatné heslo"
# if heslo == "tajne":
#     print("OK")
# else: 
#     print("špatně")

# # 3) Známka
# znamka = 2
# # Úkol:
# # - Pokud je 1 → "Výborně"
# # - Pokud je 2 → "Chvalitebně"
# # - Pokud je 3 → "Dobře"
# # - Jinak → "Nedostatečně"

# if znamka==1:
#     print("výborně")
# elif znamka==2:
#     print("chvalitebně")
# elif znamka==3:
#     print("dobře")
# else:
#     print("nedostatečně")
    
# # 4) Vnořená podmínka
# vek = 20
# obcan = False
# # Úkol:
# # - Pokud je vek >= 18, pak zkontroluj obcan
# #   - Pokud obcan = True → vytiskni "Může volit"
# #   - Pokud obcan = False → vytiskni "Nemůže volit"
# if vek >= 18:
#     if obcan:
#         print("Může volit")
#     # if obcan==False:
#     #     print("Nemůže volit")
#     else:
#         print("Nemůže volit")    

# # 5) Použití pass
# cislo = 5
# # Úkol:
# # - Pokud cislo je záporné → napiš "Záporné"
# # - Pokud cislo je nula → zatím nedělej nic (použij pass)
# # - Pokud cislo je kladné → napiš "Kladné"
# if cislo < 0:
#     print("Záporné")
# elif cislo == 0:
#     pass
# elif cislo > 0:
#     print("Kladné")


# # ---------------------------------------------
# # CVIČENÍ: Složitější podmínky
# # ---------------------------------------------

# # 1) Kino vstupné
# vek = 12
# # Úkol:
# # - Pokud je vek < 6 → vstup zdarma
# # - Pokud je 6–17 → vstupné 50 Kč
# # - Pokud je 18 a více → vstupné 100 Kč
# if vek < 6:
#     print("vstup zdarma")
# elif vek  >=6 and vek <= 17:
#     print("vstupné 50 Kč")
# elif vek  >= 18:
#     print("vstupné 100 Kč")

# # ✔️ Funguje.
# # 👉 Zjednodušit můžeš tím, že nemusíš psát celé vek >= 6 and vek <= 17. Jakmile jsi v elif, už víš, že vek >= 6, takže stačí vek <= 17.

# # if vek < 6:
# #     print("vstup zdarma")
# # elif vek <= 17:    # stačí tohle
# #     print("vstupné 50 Kč")
# # else:              # všechno ostatní je 18 a více
# #     print("vstupné 100 Kč")
    
# # 2) Přihlášení
# heslo = "tajne"
# # Úkol:
# # - Pokud je heslo prázdný string → vytiskni "Zadej heslo"
# # - Pokud je heslo správně "tajne" → vytiskni "Přístup povolen"
# # - Jinak → vytiskni "Špatné heslo"
# if heslo == "":
#     print("Zadej heslo")
# elif heslo == "tajne":
#     print("Přístup povolen")
# else: 
#     print("Špatné heslo")
    

# # 3) Známky z testu
# procenta = 73
# # Úkol:
# # - Pokud má student 90 % a více → "Výborně"
# # - 70–89 % → "Chvalitebně"
# # - 50–69 % → "Dobře"
# # - Jinak → "Nedostatečně"
# if procenta >= 90:
#     print("Výborně")
# elif procenta >=70 and procenta <= 89:
#     print("Chvalitebně")
# elif procenta >=50 and procenta <= 69:
#     print("Dobře")
# else:
#     print("Nedostatečně")
    
# # ✔️ Funguje správně.
# # 👉 Opět jde zjednodušit: když už jsi ve větvi elif procenta >= 70, není nutné psát and procenta <= 89, protože 90 a více by spadlo do první větve.
# # if procenta >= 90:
# #     print("Výborně")
# # elif procenta >= 70:
# #     print("Chvalitebně")
# # elif procenta >= 50:
# #     print("Dobře")
# # else:
# #     print("Nedostatečně")

# # 4) Kontrola e-mailu
# email = "uzivatel@example.com"
# # Úkol:
# # - Pokud email obsahuje "@" a končí na ".com" → vytiskni "Platný email"
# # - Jinak → vytiskni "Neplatný email"
# if "@" in email and email.endswith(".com"):
#     print("Platný email")
# else:
#     print("Neplatný email")
    

# # 5) Vnořená podmínka – půjčka
# vek = 25
# prijem = 15000
# # Úkol:
# # - Pokud je vek >= 18:
# #       - Pokud prijem >= 20000 → vytiskni "Půjčka schválena"
# #       - Jinak → vytiskni "Půjčka zamítnuta"
# # - Jinak → "Musí ti být alespoň 18 let"

# if vek >= 18:
#     if prijem >= 20000:
#         print("Pujcka schvalena")
#     else: 
#         print("Pujcka zamítnuta")
# else: 
#     print()
 
# ---------------------------------------------
# CVIČENÍ: Oprav kód s chybami (bez nápověd)
# ---------------------------------------------

# 1) Kino – očekávané chování je v komentáři
vek = 5
if vek < 6:
    print("zdarma")
elif vek >= 6 and vek <= 17:
    print("50 Kč")
else:
    print("100 Kč")


# 2) Přihlášení – prázdný string → "Zadej heslo", "tajne" → "Přístup povolen", jinak "Špatné heslo"
heslo = "tajne"
if heslo == "":
    print("Zadej heslo")
elif heslo == "tajne":
    print("Přístup povolen")
else:
    print("Špatné heslo")


    # 3) Známka – 90+ Výborně, 70–89 Chvalitebně, 50–69 Dobře, jinak Nedostatečně            #TODO: tady ne
procenta = 95
if procenta >= 90:
    print("Výborně")
elif procenta >= 70:
    print("Chvalitebně")
elif procenta >= 50:
    print("Dobře")
else:
    print("Nedostatečně")


# 4) E-mail – platný pokud obsahuje "@" a končí na ".com"
email = "uzivatel@example.com"
if "@" in email and email.endswith(".com"):
    print("Platný")
else:
    print("Neplatný")


# 5) Půjčka – vek >= 18 a příjem >= 20000 → schváleno, jinak zamítnuto  
# ❗️Logika funguje, ale máš dvě nezávislá if uvnitř. Když příjem ≥ 20000, vytiskne se „Schváleno“, ale druhý if už neproběhne. Když příjem < 20000, vytiskne se „Zamítnuto“. Je to použitelné, ale čistší (a bezpečnější proti dvojtisku) je else:
vek = 25
prijem = 15000
if vek >= 18:
    if prijem >= 20000:
        print("Schváleno")
    else:
        print("Zamítnuto")
else:
    print("Zamítnuto")
    
if vek >= 18:
    if prijem >= 20000:
        print("Schváleno")
    if prijem < 20000:
        print("Zamítnuto")
else:
    print("Zamítnuto")


# 6) Jméno – neprázdné → "OK", prázdné → "Chybí jméno"
# citelnejsi
jmeno = ""
if jmeno:
    print("OK")
else:
    print("Chybí jméno")
    
#kod ktery jsem nedokazal orpavit
# if not len(jmeno) == 0:
#     print("OK")
# else:
#     print("Chybí jméno")


# 7) Role – admin → plný přístup, user → omezený, jinak neznámá
role = "user"
if role == "admin":
    print("Plný přístup")
elif role == "user":
    print("Omezený přístup")
else:
    print("Neznámá role")


# 8) Teplota – <0 mráz, 0–24 chladno, 25–34 teplo, 35+ vedro
t = 25
if t < 0:
    print("mráz")
elif t <= 24:
    print("chladno")
elif t <= 34:
    print("teplo")
else:
    print("vedro")


# 9) Heslo 2 – délka > 5 a obsahuje číslici → OK, jinak SLABÉ
heslo = "Abc123"
ma_cislici = False
for znak in heslo:
    if znak.isdigit():
        ma_cislici = True
        break
if len(heslo) > 5 and ma_cislici:
    print("OK")
else:
    print("SLABÉ")


# 10) Koncovka souboru – .csv → Tabulka, .txt → Text, jinak Jiný typ
soubor = "data.csv"
if soubor.endswith(".csv"):
    print("Tabulka")
elif soubor.endswith(".txt"):
    print("Text")
else:
    print("Jiný typ")


# 11) Členství – vytiskni True/False: "py" je uvnitř a "X" není uvnitř
slovo = "python"
print("py" in slovo and "X" not in slovo)


# 12) Porovnání řetězců bez ohledu na case
a = "Python"
b = "python"
if a.lower() == b.lower():
    print("Stejné")
else:
    print("Různé")


# 13) Číslo v intervalu 1–10 včetně (vytiskni True/False)
x = 10
print(x>=1 and x <= 10)


# 14) Věk a občanství – jedním ifem vytiskni "Může volit" jen pokud obě platí
vek = 19
obcan = True
if vek >= 18 and obcan:
    print("Může volit")


# 15) Prefix/suffix – True/False: začíná "Play" a končí "ing"   #TODO: to je spravne? 
text = "Playwright Testing"
print(text.startswith("Play") and text.endswith("ing"))


# 16) Body → A/B/C/D/F dle rozmezí v komentáři
pocet_bodu = 41
if pocet_bodu >= 80:
    znamka = "A"
elif pocet_bodu >= 60:
    znamka = "B"
elif pocet_bodu >= 40:
    znamka = "C"
elif pocet_bodu >= 20:
    znamka = "D"
elif pocet_bodu < 20:
    znamka = "F"
print(znamka)


# 17) List prázdný/neprázdný – neprázdný → "Má data", jinak "Prázdné"
seznam = []
# citelnejsi kod
if seznam:
    print("Má data")
else:
    print("Prázdné")
    
    
# if seznam is True:
#     print("Má data")
# else:
#     print("Prázdné")


# 18) Email – "Validní" pokud obsahuje "@" a NEkončí na ".com"
email = "user@firma.cz"
if "@" in email and not email.endswith(".com"):
    print("Validní")
else:
    print("Nevalidní")

# 19) Heslo – všechny znaky jsou písmena → "OK", jinak "NEOK"
heslo = "abcXYZ"
# tady chci aby cyklus prestal kdyz to najde cokoliv jineho nez pismeno, proto byla blbost hledat co ej True, protoze by mi to mohlo vratit i chybu, kdyz budu mit cislo v pulce stringu az
vse_pismena = True
for znak in heslo:
    if not znak.isalpha():
        vse_pismena = False
        break

if vse_pismena:
    print("OK")
else:
    print("NEOK")

# vse_pismena = False
# for znak in heslo:
#     if znak.isalpha():
#         vse_pismena = True
#         break
# if vse_pismena:
#     print("OK")
# else:
#     print("NOK")


# 20) Košík – polozky > 0 → vnořená kontrola kuponu; jinak "Košík je prázdný"       #TODO: tady jsme odtranil to dalsi else
polozky = 0
kupon = True
if polozky > 0:
    if kupon:
        print("Sleva uplatněna")
    else:
        print("Bez slevy")
else:
    print("Košík je prázdný")