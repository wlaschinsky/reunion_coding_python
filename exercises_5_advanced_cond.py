# ---------------------------------------------
# CVIČENÍ: Kombinované podmínky (and, or, not)
# ---------------------------------------------

# 1) Věk a občanství
from pickle import NEWOBJ


vek = 20
obcan = True
# Úkol:
# - vytiskni "Může volit", pokud je vek >= 18 a zároveň obcan = True
if vek >= 18 and obcan:
    print("Muze volit")

# 2) Speciální přístup
jmeno = "Petr"
# Úkol:
# - vytiskni "Speciální přístup", pokud je jmeno "Anna" nebo "Petr"
if jmeno == "Anna" or jmeno == "Petr":
    print("Speciílní přístup")

# NEBO: 

if jmeno in ("Anna", "Petr"):
    print("Speciální přístup")
    
# 3) Heslo
heslo = ""
# Úkol:
# - pokud je heslo prázdné → "Heslo chybí"
# - jinak → "Heslo zadáno"
if not heslo: 
    print("Heslo chybí")
else:
    print("Heslo zadáno")

# 4) Interval
x = 7
# Úkol:
# - vytiskni True/False podle toho, zda je x v intervalu 1 až 10 (včetně)
if 1 <= x <= 10:
    print("True")
else: 
    print("False")
# NEBO:
print(1 <= x <= 10)

# 5) Kombinace více podmínek
vek = 16
student = True
# Úkol:
# - vytiskni "Sleva", pokud je vek < 18 nebo pokud je student = True
# - jinak vytiskni "Bez slevy"
if student or vek <18:
    print("Sleva")
else: 
    print("Beze slevy")

# 6) Negace
email = "uzivatel@example.com"
# Úkol:
# - vytiskni "Neplatný email", pokud NEobsahuje "@"
#   (použij not a operátor in)
if "@" not in email:
    print("Neplatný email")