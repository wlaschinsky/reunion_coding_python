# ---------------------------------------------
# EXERCISES: Firemní školení
# Kombinace: list + tuple + vnořené struktury + slicing + podmínka
# ---------------------------------------------

# 1. Vytvoř list `skoleni`, který bude obsahovat tři položky (tuple).
#    Každý tuple bude mít tento formát:
#    (název_skoleni, [lektor, stav])
#
#    Konkrétně zadej:
#    - ("Python základy", ["Lenka", "naplánováno"])
#    - ("Git", ["David", "probíhá"])
#    - ("Playwright", ["Samuel", "hotovo"])

# 2. Změň stav školení "Python základy" na "probíhá"

# 3. Přidej čtvrté školení:
#    - název: "Docker"
#    - lektor: "Lucie"
#    - stav: "naplánováno"

# 4. Vypiš jména všech lektorů pozpátku (např. "Lenka" → "akneL")

# 5. Vypiš první 4 znaky z názvu každého školení (např. "Play" z "Playwright")

# 6. BONUS:
#    Pro všechna školení, která mají stav "naplánováno", vypiš větu:
#    → "Školení <název> ještě nezačalo."

# ---------------------------------------------


# Vytvoření seznamu školení
skoleni = [
    ("Python základy", ["Lenka", "naplánováno"]),
    ("Git", ["David", "probíhá"]),
    ("Playwright", ["Samuel", "hotovo"])
]

# Změna stavu školení "Python základy" na "probíhá"
skoleni[0][1][1] = "probíhá"

# Přidání dalšího školení
skoleni.append(("Docker", ["Lucie", "naplánováno"]))


# Výpis jmen lektorů pozpátku
print("Lektori pozpátku:")
for zaznam in skoleni:
    lektor = zaznam[1][0]
    print(lektor[::-1])  # otočí jméno lektora

# Výpis prvních 3 písmen názvu školení
print("\nZkrácené názvy školení:")
for zaznam in skoleni:
    typ_skoleni = zaznam[0]
    print(typ_skoleni[0:3])

# Výpis upozornění pro školení, která ještě nezačala
print("\nNaplánovaná školení:")
for zaznam in skoleni:
    stage = zaznam[1][1]
    typ_skoleni = zaznam[0]
    if stage == "naplánováno":
        print("Školení", typ_skoleni, "ještě nezačalo.")
    
    


# ###########################################################
# # EXPLANATION - ruzne pripady, kdy vypsat objekty v tuplu #
# ###########################################################
# for zaznam in skoleni:
#     nazev = zaznam[0]        # název školení
#     jmeno = zaznam[1][0]     # jméno lektora
#     stav = zaznam[1][1]      # stav školení

# print(nazev, "-", jmeno, "-", stav, "-", zaznam)
    
# zaznam = skoleni[1]         # celý tuple: ("Git", ["David", "probíhá"])
# nazev = zaznam[0]           # "Git"
# jmeno = zaznam[1][0]        # "David"
# stav = zaznam[1][1]         # "probíhá"

# print(nazev, "-", jmeno, "-", stav)

# tuple_1 = skoleni[1]
# nazev = skoleni[1][0]
# jmeno = skoleni[1][1][0]
# stav = skoleni[1][1][1]

# print(nazev, "-", jmeno, "-", stav, "-", tuple_1)