# EXERCISES 1:
# 	1.	Vytvoř list kontakty, kde budou dva tuple – každý obsahuje (jméno, věk)
# Například: ("Samuel", 34) a ("Teo", 5)
# 	2.	Změň věk Tea na 6 (musíš vymyslet, jak na to, když tuple nejde měnit přímo)
# Tip: přepiš celý tuple na novou hodnotu.
# 	3.	Přidej třetího člověka („Eliška“, 27) do listu
# 	4.	Vypiš všechny jména pozpátku (musíš si vytáhnout první položky z každého tuple a otočit je)

# kontakty = [("Samuel", 34), ("Teo", 5)]
# kontakty = [("Samuel", 34), ("Teo", 6)]
# kontakty.append(("Eliska", 27))
# print(kontakty[0][0][::-1])
# print(kontakty[1][0][::-1])
# print(kontakty[2][0][::-1])

# EXERCISES 2:
# ----------------------------------------
# ÚLOHA: SPRÁVA PROJEKTŮ
# Zadání: Kombinace list, tuple, vnořený list, slicing
# ----------------------------------------

# 1. Vytvoř list `projekty`, který bude obsahovat tři položky (tuple).
#    Každý tuple bude mít tento formát:
#    (název_projektu, [jméno_vedoucího, status])
#    Např.:
#    ("Testování", ["Petr", "probíhá"])

#    Projekty:
#    - "Testování", vedoucí "Petr", status "probíhá"
#    - "Vývoj", vedoucí "Anna", status "plán"
#    - "Nasazení", vedoucí "Lukas", status "hotovo"

# 2. Změň status projektu "Vývoj" na "probíhá"

# 3. Přidej čtvrtý projekt:
#    - název: "Údržba"
#    - vedoucí: "Tom"
#    - status: "plán"

# 4. Vypiš všechna jména vedoucích pozpátku (např. "Anna" → "annA")

# 5. Vypiš první tři písmena názvu každého projektu (např. "Nasazení" → "Nas")

projekty = [
    ("Testování", ["Petr", "probíhá"]),
    ("Vývoj", ["Anna", "plán"]),
    ("Nasazení", ["Lukas", "hotovo"]),
]


    
projekty[1][1][1] = "probíhá"


print(projekty[1][0])
print(projekty)


# at mi vypise cele reseni
# nejrpve poplopate a pak pres for eache


# ----------------------------------------
# RESENI
# ----------------------------------------

# 1. Vytvoření seznamu projektů (list obsahující tuple s listem uvnitř)
projekty = [
    ("Testování", ["Petr", "probíhá"]),
    ("Vývoj", ["Anna", "plán"]),
    ("Nasazení", ["Lukas", "hotovo"]),
]

# 2. Změna statusu projektu "Vývoj" na "probíhá"
projekty[1][1][1] = "probíhá"

# 3. Přidání čtvrtého projektu
projekty.append(("Údržba", ["Tom", "plán"]))

# 4. Výpis všech jmen vedoucích pozpátku
print("Vedoucí pozpátku:")
for projekt in projekty:
    print(projekt[1][0][::-1])


# 5. Výpis prvních tří písmen názvů projektů
print("\nZkrácené názvy projektů:")
for projekt in projekty:
    print(projekt[0][:3])

# BONUS: snaha zmenit Tuple - nazev projektu
try:
    projekty[1][0] = "Probíhá"  # pokus o změnu názvu v tuple → chyba
except TypeError:
    print("❗ Nelze změnit název projektu – tuple je neměnitelný.")

# # ---------------------------------------------
# # REKAPITULACE: PRÁCE S VNITŘNÍ STRUKTUROU
# # Formát: list projektů, každý je tuple s listem uvnitř
# # ---------------------------------------------

# # Datová struktura:
# # projekty = [
# #     ("Testování", ["Petr", "probíhá"]),
# #     ("Vývoj", ["Anna", "plán"]),
# #     ("Nasazení", ["Lukas", "hotovo"])
# # ]

# # - každý prvek v `projekty` je jeden tuple
# # - každý tuple má dvě části:
# #     [0] → název projektu (řetězec)
# #     [1] → list: [vedoucí, status]

# # ---------------------
# # PŘÍSTUP K PRVKŮM:
# # ---------------------

# # projekty[1]
# # → celý tuple: ("Vývoj", ["Anna", "plán"])

# # projekty[1][0]
# # → název projektu: "Vývoj"

# # projekty[1][1]
# # → list: ["Anna", "plán"]

# # projekty[1][1][0]
# # → vedoucí: "Anna"

# # projekty[1][1][1]
# # → status: "plán"

# # ---------------------
# # UKÁZKOVÝ KÓD:
# # ---------------------

# projekty = [
#     ("Testování", ["Petr", "probíhá"]),
#     ("Vývoj", ["Anna", "plán"]),
#     ("Nasazení", ["Lukas", "hotovo"])
# ]

# # Výpis všech názvů projektů:
# for projekt in projekty:
#     print("Název:", projekt[0])

# # Výpis všech vedoucích:
# for projekt in projekty:
#     print("Vedoucí:", projekt[1][0])

# # Výpis všech statusů:
# for projekt in projekty:
#     print("Status:", projekt[1][1])

# # Změna statusu u projektu Vývoj:
# projekty[1][1][1] = "probíhá"
# print("Nový status Vývoj:", projekty[1][1][1])

# # Přidání nového projektu:
# projekty.append(("Údržba", ["Tom", "plán"]))
# print("Seznam projektů po přidání:")
# for projekt in projekty:
#     print(projekt)

# # ---------------------------------------------
# # Tip: Tohle je reálně velmi podobné tomu, jak se strukturuje JSON, API data nebo databázové výstupy.
