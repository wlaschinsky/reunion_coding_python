# ---------------------------------------------
# ÚLOHA: Rezervace letenky (komplexní)
# Cíl: procvičit input(), validace vstupů, podmínky a logické operátory
# Pravidla:
# - Každý krok kontroluj samostatně.
# - Pokud vstup neprojde, vypiš chybu a ukonči program.
# - Pokud vše projde, vypiš shrnutí rezervace.
# ---------------------------------------------

# 1) Jméno cestujícího
# - Načti jméno (string).
# - Pokud je prázdné → „Chybí jméno“.

from lesson_2.excercises.exercises_5 import vek


jmeno = input("Zadej jméno: ")
# TODO: validace jména
if not jmeno: 
    print("Chybí jméno")
    exit()

# 2) Věk cestujícího
# - Načti věk (uživatel zadá číslo).
# - Pokud není celé číslo → vypiš chybu.
# - Pokud je věk < 0 → „Neplatný věk“.
# - Pokud je věk < 18 → „Mladiství potřebují doprovod“.
# - Jinak → pokračuj dál.

vek_text = input("Zadej věk: ")
# TODO: převod na int a kontrola hodnoty

if not vek_text.isdigit():
    print("Musíš zadat celé číslo")
    exit()

vek = int(vek_text) 

if vek < 0:
    print("Neplatný věk")
    exit()
elif vek < 18:
    print("Mladiství potřebují doprovod")
    exit()
# nevim jak pokracovat dal, co napsat, nebo nechat? zadne else? potom co to ze vek je cele cislo? to zarusim tim prevedenim na int ne? 

# 3) Cílová destinace
# - Načti destinaci (string).
# - Pokud nezačíná velkým písmenem → „Destinace musí začínat velkým písmenem“.
# - Pokud je prázdná → „Musíš zadat destinaci“.

destinace = input("Zadej cílovou destinaci: ")

if not destinace:
    print("Musíš zadat destinaci")
    exit()
elif not destinace[0].isupper():
    print("Destinace musí začínat velkým písmenem")
    exit()
          
# TODO: validace destinace


# 4) Pojištění
# - Načti odpověď (ano/ne).
# - Pokud je jiná než „ano“ nebo „ne“ → „Neplatná odpověď“.

pojisteni = input("Chceš cestovní pojištění (ano/ne)? ")
# TODO: kontrola pojištění
if pojisteni not in ["ano", "ne"]:
    print("Neplatná odpověď")
    exit()

# 5) Výsledek
# - Pokud všechny kontroly projdou, vypiš shrnutí:
#   Rezervace úspěšná pro: <jméno>, <věk> let, destinace: <destinace>, pojištění: <ano/ne>.
print("Rezervace úspěšná pro:", jmeno, "-", vek, "let, destinace:", destinace, ", pojištění:", pojisteni)

# TODO: finální výstup