# 🐍 TÝDENNÍ MINIÚKOL #4
# Téma: Práce se vstupem uživatele + filtrování seznamu

# ÚKOL:
# 1. Vytvoř prázdný seznam jménem `cisla`.
# 2. Požádej uživatele 5× o zadání čísla (pomocí input).
#    Každé číslo převed' na int a ulož do seznamu.
# 3. Vytvoř nový seznam, kde budou jen ta čísla, která jsou větší než 10.
# 4. Vypiš obě verze seznamů:
#    - Původní seznam
#    - Filtrovaný seznam čísel > 10

# Příklad chování:
# Zadej číslo: 3
# Zadej číslo: 15
# ...
# Výstup:
# Původní seznam: [3, 15, ...]
# Čísla větší než 10: [15, ...]

# BONUS:
# Co se stane, když `input()` nenecháš převést na `int` a zkusíš porovnat s číslem?

cisla = []
filtrovana_cisla = []
for i in range(5):
    nove_cislo = int(input("Zadej cislo: "))
    cisla.append(nove_cislo)
    if nove_cislo > 10:
        filtrovana_cisla.append(nove_cislo)
        
print("Původní čísla: ", cisla)            
print("Čísla větší než 10: ", filtrovana_cisla)            

