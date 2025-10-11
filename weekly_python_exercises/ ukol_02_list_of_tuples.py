# 🐍 TÝDENNÍ MINIÚKOL #2
# Téma: List obsahující tuples + práce s cyklem for

# ÚKOL:
# 1. Vytvoř list tří souřadnic jako tuple, např.: [(1, 2), (3, 4), (5, 6)]
# 2. Pomocí `for` cyklu vypiš všechny body ve formátu: "Souřadnice: x=1, y=2"
# 3. BONUS: Vytiskni jen ty body, kde je x > 2

# BONUSOVÁ OTÁZKA:
# Jak bys slovně popsal rozdíl mezi "for x in seznam" a "if x in seznam"?

souradnice = [(1, 2), (3, 4), (5, 6)]

for bod in souradnice:
    print("Souřadnice: ", "x = ", bod[0], "x = ", bod[1], "= y" )


for bod in souradnice:
    if bod[0] > 2:
        print("Souřadnice: ", "x = ", bod[0], bod[1], "= y," )
        
        
# for x in seznam:    
# Prochází všechny prvky seznamu a s každým něco dělá 
# if x in seznam:
# Ověří, jestli jeden konkrétní prvek v seznamu je – vrátí True/False
