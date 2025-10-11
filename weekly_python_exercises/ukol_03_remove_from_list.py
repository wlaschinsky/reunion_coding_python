# 🐍 TÝDENNÍ MINIÚKOL #3
# Téma: Mazání hodnot ze seznamu, který obsahuje tuples

# ÚKOL:
# 1. Vytvoř list bodů (souřadnic), např.: [(1, 2), (3, 4), (5, 6), (2, 1)]
# 2. Vytvoř nový list, kde budou jen ty body, kde y > 2
#    (tedy odfiltruj body, kde y je menší nebo rovno 2)
# 3. Vypiš nový list pomocí for cyklu ve formátu: "Souřadnice: x = __ , y = __"

# BONUS:
# Víš, proč není dobré mazat prvky z listu uvnitř for smyčky?

souradnice = [(1, 2), (3, 4), (5, 6), (2, 1)]
souradnice_2 = []

for bod in souradnice:
    if bod[1] > 2:
        souradnice_2.append(bod)
        print("Souřadnice: x =", bod[0], ", y =", bod[1])

print("Nový seznam:", souradnice_2)
