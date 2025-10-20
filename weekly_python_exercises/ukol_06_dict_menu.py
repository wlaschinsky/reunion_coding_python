# 🐍 TÝDENNÍ MINIÚKOL #6
# Téma: Slovník (dict) + výběr z nabídky + výpis

# ÚKOL:
# 1. Vytvoř slovník `jidelnicek`, kde klíč bude jídlo a hodnota počet kalorií.
#    Např.:
#    jidelnicek = {
#        "banán": 90,
#        "chleba": 250,
#        "vejce": 155
#    }

# 2. Zeptej se uživatele 3×, co z toho snědl (pomocí input).
#    Každý výběr ulož do seznamu `vybrane_polozky`.

# 3. Na konci vypiš:
#    - co si vybral
#    - celkový počet kalorií, které tím snědl

# BONUS:
# Pokud uživatel zadá jídlo, které není ve slovníku, vypiš varování:
# "Tuto položku neznám: ___" a nezapočítej ji.

# Příklad chování:
# Co jsi snědl? banán
# Co jsi snědl? rohlík
# Tuto položku neznám: rohlík
# Co jsi snědl? vejce

# Výstup:
# Snědl jsi: ['banán', 'vejce']
# Celkem kalorií: 245


jidelnicek = {
       "banán": 90,
       "chleba": 250,
       "vejce": 155, 
       "kofola": 600,
       "eidam": 250
   }

snedene_jidlo = []
celkem_kalorii = 0

for item in range(3):
    nazev_jidla = input("Co jsi snedl (vyber ze seznamu: ")
    
    if nazev_jidla not in jidelnicek:
        print("Zkus to znovu, tohle neznám: ", nazev_jidla)
    
    else:
        snedene_jidlo.append(nazev_jidla)
        celkem_kalorii += jidelnicek[nazev_jidla]
        
print(snedene_jidlo) 

print("Snědl jsi:", snedene_jidlo)
print("Celkem kalorií:", celkem_kalorii)