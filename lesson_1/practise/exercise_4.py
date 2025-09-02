# ---------------------------------------------
# ÚLOHA: Evidence zaměstnanců – report
# ---------------------------------------------
# Máš seznam zaměstnanců firmy. Každá položka seznamu
# je tuple ve formátu:
# (jméno, [oddělení, pozice, stav])
#
# Příklad jedné položky:
# ("Petr", ["IT", "tester", "aktivní"])
#
# 1. Vytvoř list `zamestnanci` s těmito daty:
#    - "Petr", IT, tester, aktivní
#    - "Lucie", Marketing, manažer, neaktivní
#    - "Adam", IT, vývojář, aktivní
#    - "Anna", HR, recruiter, aktivní
#    - "David", Marketing, grafik, neaktivní
#
# 2. Vypiš všechny zaměstnance, kteří jsou "aktivní"
#    → formát: "<jméno> - <oddělení> - <pozice>"
#
# 3. Spočítej, kolik lidí pracuje v oddělení "IT"
#
# 4. Najdi a vypiš všechny, jejichž jméno začíná na písmeno "A"
#
# 5. Vypiš názvy všech pozic, které mají víc než 7 znaků
#
# 6. Změň stav "Lucie" na "aktivní"
#
# 7. Přidej nového zaměstnance: "Michal", IT, admin, aktivní
#
# 8. BONUS:
#    - vytvoř nový list `aktivni_IT`, který bude obsahovat
#      jen zaměstnance z IT oddělení, kteří jsou aktivní
#    - tento nový list vypiš stejným formátem jako v bodě 2
# ---------------------------------------------

# Tahle úloha tě donutí:
# 	•	číst a rozumět zadání po částech
# 	•	pracovat s kontextem dat (když máš pozice, stav, oddělení…)
# 	•	kombinovat podmínky a indexy
# 	•	přemýšlet, co měníš přímo v seznamu a co děláš v novém


#1
employer =[
    ("Petr", ["IT", "tester", "aktivní"]),
    ("Lucie", ["Marketing", "manažer", "neaktivní"]),
    ("Adam", ["IT", "vývojář", "aktivní"]),
    ("Anna", ["HR", "recruiter", "aktivní"]),
    ("David", ["Marketing", "grafik", "neaktivní"])
]

#2
for empl in employer:
    if empl[1][2] == "aktivní":
        print("<", empl[0], "> - <", empl[1][0], "> - <",  empl[1][1],">")

#3
count = 0
for empl in employer:
    if empl[1][0] == "IT":
        count +=1
print(count)
# proc tady neni vysledek promenne uzavren v podmince a dostane se do printu na uroven rovnou "for", myslel jsem ze ty jsou si rovny a print nenipodrazeny, jaktoze vidi na vysledny count? 

#4
for empl in employer:
    if empl[0].startswith("A"):
        print(empl[0])

#5
for pos in employer:
    if len(pos[1][1]) > 7:
        print(pos[1][1])

#6
employer[1][1][2] = "aktivní"
print(employer)
#tady is zase nepamatuju, kdy se to muze menit a kdy se to naopak nemeni, achjo, kdy jakoby nahradim cely ten item a kdy si to muzu vylistovat

#7
new_item =  ("Michal", ["IT", "admin", "neaktivní"]) 
employer.append(new_item)
print(employer)

#8
it = []
for item in employer: 
    if item[1][0] == "IT":
        it.append(item)
print(it)



