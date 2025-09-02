 # ---------------------------------------------
# CVIČENÍ – Zadání (bez řešení)
# ---------------------------------------------

# 1) Uživatelské jméno
jmeno = "Teodor"
# Úkol:
# - musí být dlouhé alespoň 6 znaků
# - musí začínat na písmeno "T"
# - vytiskni True/False podle toho, jestli splňuje obě podmínky
print(len(jmeno) >= 6 and jmeno.startswith("T"))
# pokud by tam bylo if, vytiskne se mi, co budu chtit
# nyni je prvni podminka True, druha taky True, takze se  vyhodnocuje True and True

# 2) Věk a občanství
vek = 20
obcan = False
# Úkol:
# - vstup povolen, pokud je vek >= 18 a zároveň obcan = True
# - vytiskni True/False
print("vstup povolen: ",vek >= 18 and obcan==True)

# 3) Heslo
heslo = "abc123"
# Úkol:
# - musí být delší než 5 znaků
# - musí obsahovat číslici
# - pokud splní obě podmínky, vytiskni "OK"
# - jinak vytiskni "SLABÉ"
print(heslo >= 5 and )

# 4) E-mail
email = "uzivatel@example.com"
# Úkol:
# - ověř, že v řetězci je znak "@"
# - ověř, že končí na ".com"
# - vytiskni True, pokud obě podmínky platí
print(email.endswith(".com") and "@" in email ) 

# # EXAMPLE: 

# print(10 > 3)
# print(10 == 10)
# print("Auto" != "auto")
# print(3 <= 3)

# print("to" in "python")
# print("Py".lower() in "python")   # True

# x = 7
# print(1 < x and x < 10)
# print(1 < x < 10)                 # totéž, kratší zápis

# print(not False)
# print((5 > 1) and ("a" < "b"))
# print((5 < 1) or ("a" > "b"))


# # vek a prukaz 
# vek = 17
# ma_prukaz = True
# # vytiskni True/False: může vstoupit, pokud je vek >= 18 A zároveň ma_prukaz
# print(vek >= 18 and ma_prukaz, ": muze vstoupit")

# # Retezec a clenstvi
# s = "Playwright Testing"
# # vytiskni, zda v řetězci je "test" (bez ohledu na velikost písmen)
# print("test" in s.lower())

# # Rozsah cisla 
# x = 12
# # vytiskni True/False: je x v intervalu 10 až 20 (včetně)?
# print(x in range(10,20))

# # vice podminek
# jmeno = "Samuel"
# delka_ok = len(jmeno) >= 5
# zacina_s = jmeno.startswith("S")
# # kombinuj pomocí and/or – vytiskni True/False podle toho, co uznáš za vhodné (např. obojí musí platit)

# # minitests s if
# heslo = "Tajne123"
# # vytiskni "OK" pokud delka hesla >= 6 A obsahuje číslici (zkus "0" in heslo nebo .isdigit() na jednotlivých znacích)
# # jinak vytiskni "SLABÉ"


# # ---------------------------------------------
# # CVIČENÍ: Operátory, funkce a metody
# # ---------------------------------------------

# # 1) Věk a průkaz
# vek = 17
# ma_prukaz = True
# # Úkol: vytiskni True/False – může vstoupit, pokud je vek >= 18 a zároveň má průkaz
# print(vek >= 18 and ma_prukaz, ": muze vstoupit")


# # 2) Řetězec a členství
# s = "Playwright Testing"
# # Úkol: vytiskni, zda v řetězci je "test" (bez ohledu na velikost písmen)
# # Nápověda: použij metodu lower() na řetězci
# print("test" in s.lower())


# # 3) Rozsah čísla
# x = 12
# # Úkol: vytiskni True/False – je x v intervalu 10 až 20 (včetně)?
# # TIP: range(10, 21), protože range končí exkluzivně
# print(x in range(10, 21))


# # 4) Více podmínek
# jmeno = "Samuel"
# delka_ok = len(jmeno) >= 5
# zacina_s = jmeno.startswith("S")   # metoda objektu string
# # Úkol: kombinuj pomocí and/or – vytiskni True/False podle toho, co uznáš za vhodné (např. obojí musí platit)
# print(delka_ok and zacina_s)


# # 5) Mini-test s if
# heslo = "Tajne123"
# # Úkol: vytiskni "OK" pokud:
# #  - délka hesla >= 6
# #  - obsahuje číslici
# # Jinak vytiskni "SLABÉ"

# ma_cislici = any(znak.isdigit() for znak in heslo)   # metoda isdigit() patří k objektu string
# if len(heslo) >= 6 and ma_cislici:
#     print("OK")
# else:
#     print("SLABÉ")