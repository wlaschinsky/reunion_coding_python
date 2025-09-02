# EXERCISES: ukazka


vek = int(input("napis vek: 20"))
if vek >= 18:
    print("Můžeš vstoupit")
print("Hotovo")

# EXERCISES : BOOLEAN

print(bool(0))
print(bool(42))
print(bool(""))
print(bool("Python"))
print(bool([]))
print(bool([0]))


# 1) print(bool(0))
# 	•	Výsledek: False
# 	•	Proč: nula je „prázdno“ u čísel → False.

# 2) print(bool(42))
# 	•	Výsledek: True
# 	•	Proč: nenulové číslo → True.

# 3) print(bool(""))
# 	•	Výsledek: False
# 	•	Proč: prázdný řetězec → False.

# 4) print(bool("Python"))
# 	•	Výsledek: True
# 	•	Proč: ne-prázdný řetězec → True.

# 5) print(bool([]))
# 	•	Výsledek: False
# 	•	Proč: prázdný list → False.

# 6) print(bool([0]))
# 	•	Výsledek: True
# 	•	Proč: neprázdný list je vždy True bez ohledu na to, co uvnitř je. I bool([0]), bool([False]) a dokonce bool([[]]) jsou True, protože list obsahuje nějaký prvek.



bool(1-1) # False (nula je „prázdno“ u čísel)
bool([[], []]) # True  - Pozor: je to neprázdný list (obsahuje dva prvky, i když jsou to prázdné listy). U kontejnerů rozhoduje prázdnost, ne obsah.
bool("   ")   # True Řetězec s mezerami je pořád neprázdný string.
bool([False]) # True - rozhoduje prazdnost u listu a tuple
bool("False")  # True - jedna se o string 
bool(0.000)  # False - je to nula

