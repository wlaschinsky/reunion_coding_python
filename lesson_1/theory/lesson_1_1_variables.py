# TOPIC: PROMENNE

# +-------------------------------+-------------------------------------------+
# | Co je povoleno               | Co je zakázáno                            |
# +-------------------------------+-------------------------------------------+
# | Malá a velká písmena         | Začínat číslicí                          |
# | Číslice (ale ne na začátku)  | Používat mezery nebo speciální znaky    |
# | Podtržítka (_)               | Přepisovat klíčová slova (např. `int`)  |
# +-------------------------------+-------------------------------------------+

jmeno = "Teo"
vek = 5
print(jmeno, vek)  # Teo 5

jmeno = "Eliška"
print("Ahoj,", jmeno)  # Ahoj, Eliška

# bud oddelit promenne mezerou nebo +
# +-------------------+-----------------------------+
# | Mezera            | +                           |
# +-------------------+-----------------------------+
# | print("Ahoj,", jmeno) | print("Ahoj " + jmeno) |
# +-------------------+-----------------------------+           
                       
name = "Karel"
age = 33
print("Jmenuji se", name, "a je mi", age, "let")
print("Jmenuji se " + name + " a je mi " + age + " let")

# +----------------------------+----------------------------------------------+
# | Zápis                     | Funguje?                                     |
# +----------------------------+----------------------------------------------+
# | print("text", cislo)      | ✅ ano – čárka převádí automaticky           |
# | print("text" + str(cislo))| ✅ ano – ručně převedeš číslo na text        |
# | print("text" + cislo)     | ❌ chyba – Python neumí sčítat text + číslo  |
# +----------------------------+----------------------------------------------+


num = 33
print("Odpoved na vsechno je", num)
print("Odpoved na vsechno je " + num)   # ❌ chyba – Python neumí sčítat text + číslo
print("Odpoved na vsechno je " + str(num))  # ✅ ano – ručně převedeš číslo na text

