# 🐍 TÝDENNÍ MINIÚKOL #8
# Téma: Slovník (dict) + input + sčítání + podmínka

# ÚKOL:
# 1. Vytvoř slovník `napoje`, kde klíč bude název nápoje, a hodnota počet mililitrů.
#    napoje = {
#        "voda": 250,
#        "čaj": 200,
#        "kofola": 500,
#        "pomerančový džus": 300
#    }

# 2. Pomocí cyklu `while` se opakovaně ptej uživatele, co pil. Ukončení zadávání pomocí "konec".

# 3. Každý platný nápoj přičti do `celkem_ml`.

# 4. Po zadání "konec" vypiš:
#    - Celkový objem vypitých tekutin
#    - Pokud je to méně než 2000 ml, napiš: "Zkus toho vypít víc 💧"

# BONUS:
# 1. Vypiš, kolikrát byl který nápoj vybrán.
#    → třeba: "voda: 2x, čaj: 1x"


# napoje = {
#        "voda": 250,
#        "čaj": 200,
#        "kofola": 500,
#        "pomerančový džus": 300
#    }
# celkem_ml = 0

# while True:
#     vstup = input("Zadej co jsi pil (nebo konec): ")
    
#     if vstup == "konec":
#         break  # ukončí smyčku
#     elif vstup in napoje:
#         print("Zadal jsi:", vstup)
#         celkem_ml += napoje[vstup]
#     else:
#         print("Tuto položku neznám:", vstup)
# print(celkem_ml)


napoje = {
    "voda": 250,
    "čaj": 200,
    "kofola": 500,
    "pomerančový džus": 300
}

celkem_ml = 0  # správně mimo while

while True:
    vstup = input("Zadej co jsi pil (nebo 'konec'): ")
    
    if vstup == "konec":
        break

    elif vstup in napoje:
        print("Zadal jsi:", vstup)
        celkem_ml += napoje[vstup]
        print("Zatím vypito:", celkem_ml, "ml")
    
    else:
        print("Tuto položku neznám:", vstup)

print("Celkem vypito:", celkem_ml, "ml")