# # ---------------------------------------------
# # CVIČENÍ: input() a podmínky
# # ---------------------------------------------

# # 1) Věk
# # - zeptej se uživatele na věk
# # - pokud je 18 a více → vypiš "Dospělý"
# # - jinak → "Mladistvý"

vek = int(input("Kolik ti je? "))

if vek >= 18:
    print("Dospělý")
else: 
    print("Mladistvý")
    
# # 2) Heslo
# # - zeptej se na heslo
# # - pokud je prázdné → vypiš "Heslo chybí"
# # - pokud je "tajne" → vypiš "Přístup povolen"
# # - jinak → "Špatné heslo"

# heslo = (input("Zadej heslo: "))

if not heslo: 
    print("Heslo chybí")
elif heslo is "tajné":
    print("Přístup povolen")
else: 
    print("Špqtné heslo")
    
    
# # 3) Sudé nebo liché
# # - uživatel zadá celé číslo
# # - zjisti, jestli je číslo sudé nebo liché
# #   (nápověda: operátor % – zbytek po dělení)

cislo = int(input("Zadej cele cislo: "))

if cislo%2 == 0: 
    print("sude cislo")
else: 
    print("liche cislo")


# 4) Desetinné číslo
# - uživatel zadá číslo s desetinnou tečkou
# - vypiš, jestli je větší než 100.0

cislo = float(input("Zadej cislo s desetinnym mistem: "))

if cislo > 100.0: 
    print("je vetsi o" ,  cislo - 100.0)
else: 
    print("Neni vetsi")

# 5) Text a členství
# - uživatel zadá libovolný text
# - vypiš "Obsahuje Python", pokud v textu je slovo "Python" (bez ohledu na velikost písmen)
# - jinak vypiš "Neobsahuje Python"

text = input("Neco napis: ").lower()
if "python" in text:
    print("Obsahuje Python")
else:
    print("Neobsahuje Python")
    
    
    
    
