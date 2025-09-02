# ---------------------------------------------
# ÚLOHA: Školení – přehled a analýza
# Kombinace: list + tuple + slicing + podmínky + počítání
# ---------------------------------------------

# 1. Vytvoř list `skoleni`, který bude obsahovat 4 školení.
#    Každé školení je tuple ve formátu:
#    (název_skoleni, [lektor, stav])
#
#    Školení:
#    - "Python", lektor "Anna", stav "probíhá"
#    - "Git", lektor "David", stav "naplánováno"
#    - "Docker", lektor "Lucie", stav "hotovo"
#    - "Playwright", lektor "Samuel", stav "naplánováno"

# 2. Vypiš všechna školení, která ještě nezačala (= stav je "naplánováno")

# 3. Spočítej, kolik školení právě probíhá

# 4. Vypiš všechna jména lektorů, jejichž jméno začíná na písmeno "L"

# 5. Vypiš názvy školení, které mají víc než 6 znaků

# 6. BONUS: Vytvoř nový list `aktivni`, který bude obsahovat jen školení,
#    která mají stav "probíhá" nebo "hotovo"
#    → potom vypiš tento nový list


skoleni = [
    ("Python", ["Anna",  "probíhá"]),
    ("Git", ["David",  "naplánováno"]),
    ("Docker", ["Lucie",  "hotovo"]),
    ("Playwright", ["Samuel",  "naplánováno"]),
]

for item in skoleni:
    typ_skoleni = item[0]        # název školení
    stav = item[1][1]            # stav z vnitřního listu
    if stav == "naplánováno":
        print(typ_skoleni)

    
count = 0
for item in skoleni:
    if item[1][1] == "probíhá":
        count += 1
print("Probíhá školení:", count)

for item in skoleni:
    lektor = item[1][0]
    if lektor.startswith("L"):
        print(lektor)

for item in skoleni:
    nazev = item[0]
    if len(nazev) > 6:
        print(nazev)
        
aktivni = []
for item in skoleni:
    stav = item[1][1]
    if stav == "probíhá" or stav == "hotovo":
        aktivni.append(item)

print("Aktivní školení:")
for zaznam in aktivni:
    print(zaznam[0], "-", zaznam[1][0], "-", zaznam[1][1])
