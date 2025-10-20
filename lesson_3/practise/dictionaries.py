# ---------------------------------------------
# CVIČENÍ: Slovníky – základy
# ---------------------------------------------

# 1) Uživatel
# - vytvoř slovník "uzivatel" s klíči: jmeno, vek, mesto
# - naplň je libovolnými hodnotami
# - vypiš jméno uživatele

# 2) Přístup k hodnotám
# - k předchozímu slovníku přidej klíč "email"
# - vypiš celé město uživatele
# - změň věk uživatele na jinou hodnotu

# 3) Mazání
# - smaž klíč "mesto" ze slovníku
# - vypiš aktuální obsah slovníku

# 4) Vnořený slovník
# - vytvoř slovník "student", kde klíče budou:
#   jmeno, rocnik, predmety
# - predmety bude další slovník s klíči: matematika, anglictina
# - vypiš známku z angličtiny

# 5) Kontrola hesla
# - vytvoř slovník "login" s klíči: username, password
# - username bude "admin", password třeba "tajne"
# - načti vstup od uživatele pro heslo (input)
# - ověř, jestli se shoduje s hodnotou v login["password"]
# - pokud ano → vytiskni "Přístup povolen"
# - jinak → "Špatné heslo"

# 1 - DONE
uzivatel = {"jmeno": "Samuel", "vek": 55, "mesto": "Praha "}
print(uzivatel["jmeno"])


#2 - 
