# 🐍 TÝDENNÍ MINIÚKOL #5
# Téma: Slovník (dict) + input od uživatele

# ÚKOL:
# 1. Vytvoř prázdný slovník `lide`.
# 2. 3× se zeptej uživatele na jméno a věk osoby.
#    Každý pár ulož do slovníku – jméno bude klíč, věk hodnota (např. {"Anna": 25}).
# 3. Nakonec vypiš celý slovník.

# Příklad chování:
# Zadej jméno: Anna
# Zadej věk: 251
# ...
# Výstup:
# {'Anna': 25, 'Karel': 31, 'Eva': 22}

# BONUS:
# Zkus ze slovníku vypsat jen lidi, kterým je víc než 25 let.
# Např.:
# "Anna má 28 let." (jen pokud je > 25)


lide = {}
for item in range (3):
        jmeno = input("Zadej jméno: ")
        vek = int(input("Zadej vek: "))
        if vek > 25:
            lide[jmeno] = vek 
print(lide)
