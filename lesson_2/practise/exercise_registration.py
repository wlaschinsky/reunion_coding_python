# ---------------------------------------------
# ÚLOHA: Registrace uživatele (komplexní)
# ---------------------------------------------
# Pravidla:
# - Kontroly prováděj po sobě. Pokud některá neprojde, program skončí výpisem chyby.
# - Když všechny kontroly projdou, na konci vypiš potvrzení registrace.
# - Používej jen to, co je v lekci 2 (input, podmínky, len, isdigit, atd.)
# ---------------------------------------------

# 1) Jméno
jmeno = input("Zadej jméno: ")
if not jmeno:   # prázdný string → False
    print("Chybí jméno.")
    exit()

# kontrola, zda jméno obsahuje jen písmena
if not jmeno.isalpha():
    print("Jméno musí obsahovat jen písmena.")
    exit()

# 2) Věk
vek_text = input("Zadej věk: ")

try:
    vek = int(vek_text)
except ValueError:
    print("Věk musí být číslo.")
    exit()

if vek < 0:
    print("Věk nemůže být záporný.")
    exit()
elif vek < 18:
    print("Registrace je povolena od 18 let.")
    exit()

# 3) E-mail
email = input("Zadej e-mail: ")
if "@" not in email or not email.endswith(".com"):
    print("E-mail musí obsahovat '@' a končit na '.com'.")
    exit()

# 4) Heslo
heslo = input("Zadej heslo: ")

# délka hesla
if len(heslo) < 6:
    print("Heslo musí mít alespoň 6 znaků.")
    exit()

# obsahuje číslici?
ma_cislici = False
for znak in heslo:
    if znak.isdigit():
        ma_cislici = True
        break

if not ma_cislici:
    print("Heslo musí obsahovat alespoň jednu číslici.")
    exit()

# 5) Výsledek
print("Registrace úspěšná pro:", jmeno, ",", email)


# # ---------------------------------------------
# # ÚLOHA: Registrace uživatele (komplexní)
# # Cíl: spojit input(), převody, práci s textem a podmínky
# # Pravidla:
# # - Kontroly prováděj po sobě. Pokud některá neprojde, program skončí výpisem chyby.
# # - Když všechny kontroly projdou, na konci vypiš potvrzení registrace.
# # - Volitelně můžeš ošetřit nečíselný vstup pomocí try/except.
# # ---------------------------------------------

# # 1) Jméno
# # - Načti jméno (string).
# # - Pokud je prázdné, vypiš chybovou hlášku a skonči.

# jmeno = input("Zadej jméno: ")
# if not jmeno: 
#     print("chybí jméno") # problem, co kdyz to bude jen num a ja chci jen alphabetical?
#     exit() # to nefunguje, kdyz to jen odentruju, tak to ujede dal, kdyz napisu honotu, skonci to

# # 2) Věk
# # - Načti věk (uživatel zadá číslo).
# # - Převeď na celé číslo (int).
# # - Pokud je věk záporný, vypiš chybu a skonči.
# # - Pokud je < 18, vypiš, že registrace je povolena od 18 let, a skonči.

# vek_text = input("Zadej věk: ")
# vek_num = int(vek_text)
# # TODO: validace hodnoty - nechapu co se ma validovat? 


# # 3) E-mail
# # - Načti email (string).
# # - Musí obsahovat znak '@' a končit na '.com'.
# # - Pokud podmínky nesplní, vypiš chybu a skonči.

# email = input("Zadej e-mail: ")
# # TODO: kontrola členství a koncovky

# if "@" not in email and not email.endswith(".com"):
#     print("nesplnene podminky")
#     exit()

# # 4) Heslo
# # - Načti heslo (string).
# # - Musí mít délku alespoň 6 znaků.
# # - Musí obsahovat aspoň jednu číslici.
# # - Pokud ne, vypiš konkrétní důvod a skonči.

# heslo = input("Zadej heslo: ")
# heslo_lenght = len(heslo)
# ma_cislici = 
# # TODO: kontrola délky
# if heslo_lenght <= 6 and not contains ma_cislici:
#     print("heslo nesplnuje podminky")
#     exit()
# # TODO: kontrola „obsahuje číslici“ (zvaž průchod znaky nebo jiný přístup)


# # 5) Výsledek
# # - Pokud všechny kontroly výše prošly, vypiš potvrzení registrace ve formátu:
# #   "Registrace úspěšná pro: <jméno>, <email>"

# print( "Registrace úspěšná pro: jmeno, email")
# # TODO: finální výstup


# # ---------------------------------------------
# # Poznámky pro tebe (nepovinné, můžeš smazat):
# # - Nepoužívej složité konstrukce, drž se toho, co máš v lekci 2.
# # - Chybný nečíselný věk můžeš (ale nemusíš) ošetřit try/except:
# #
# #   raw = input("Zadej věk: ")
# #   try:
# #       vek = int(raw)
# #   except ValueError:
# #       print("Zadal jsi nečíselnou hodnotu.")
# #       exit()
# #
# # - U hesla si nejdřív vytvoř proměnné typu:
# #       delka_ok = ...
# #       ma_cislici = ...
# #   a pak je vyhodnoť v podmínkách.
# # - Buď konkrétní v chybových hláškách (uživatel ví, co opravit).
# # ---------------------------------------------
