# 🐍 Python – Vestavěné funkce a metody

## 📖 Přehled

| Funkce      | Popis                                         | Příklad                              |
|-------------|-----------------------------------------------|--------------------------------------|
| `type()`    | Vrátí typ hodnoty                            | `type(3.14)` → `<class 'float'>`     |
| `len()`     | Délka sekvence (str, list, tuple, ...)       | `len("Python")` → `6`                |
| `int()`     | Převod na celé číslo                         | `int("42")` → `42`                   |
| `float()`   | Převod na desetinné číslo                    | `float("3.5")` → `3.5`               |
| `str()`     | Převod na řetězec                            | `str(123)` → `"123"`                 |
| `round()`   | Zaokrouhlení (volitelně na n desetinných)    | `round(3.1415, 2)` → `3.14`          |
| `abs()`     | Absolutní hodnota                            | `abs(-7)` → `7`                      |
| `min()/max()` | Minimum/maximum v iterovatelném objektu    | `max([3,8,2])` → `8`                 |
| `sum()`     | Součet čísel                                 | `sum([1,2,3])` → `6`                 |
| `sorted()`  | Vrátí seřazenou kopii                        | `sorted([3,1,2])` → `[1,2,3]`        |
| `enumerate()`| Číslované procházení v for-cyklu            | `enumerate(["a","b"])` → `(0,"a")..` |
| `range()`   | Generátor posloupnosti čísel                 | `range(3)` → `0,1,2`                 |

---

## 🔹 Funkce vs. Metody

- **Funkce**: volám jako `funkce(hodnota)`
  - `len("Python")` → `6`
  - `abs(-7)` → `7`
  - `sorted([3,1,2])` → `[1,2,3]`

- **Metody**: patří konkrétnímu objektu, volají se `objekt.metoda(...)`
  - `"ahoj".upper()` → `"AHOJ"`
  - `["a","b"].append("c")` → `["a","b","c"]`

💡 Pomůcka:  
- `len(x)` = „zeptám se Pythonu“ (globální funkce)  
- `x.upper()` = „řeknu objektu x, ať se sám změní“ (metoda)

---

## 🔹 Příklady použití

### Základní funkce

```python
print(type(3.14))       # <class 'float'>
print(len("Python"))    # 6
print(int("42"))        # 42
print(float("3.5"))     # 3.5
print(str(123))         # "123"
print(round(3.1415, 2)) # 3.14
print(abs(-7))          # 7
print(min([3, 8, 2]))   # 2
print(max([3, 8, 2]))   # 8
print(sum([1, 2, 3]))   # 6
print(sorted([3, 1, 2]))# [1, 2, 3]
```

---

### Metody řetězce a seznamu

```python
text = "Samuel"
print(text.upper())     # "SAMUEL"
print(text.lower())     # "samuel"
print(text.replace("S","Z"))  # "Zamuel"

cisla = [3,1,2]
cisla.append(4)
print(cisla)            # [3,1,2,4]
```

---

### `sorted()` vs `.sort()`

- `sorted()` → funkce, vrací **nový seřazený list**
- `.sort()` → metoda listu, **mění původní list** a vrací `None`

```python
cisla = [3, 1, 4, 2]
nove = sorted(cisla)
print("Původní:", cisla)   # [3,1,4,2]
print("Nový:", nove)       # [1,2,3,4]

cisla = [3, 1, 4, 2]
vysledek = cisla.sort()
print("Výsledek sort():", vysledek)  # None
print("List po sort():", cisla)      # [1,2,3,4]

jmena = ["Adam", "petr", "anna"]
print(sorted(jmena, key=str.lower))  # ['Adam','anna','petr']
print(sorted(jmena, reverse=True))   # ['petr','anna','Adam']

jmena.sort(key=str.lower)
print(jmena)  # ['Adam','anna','petr']
```

---

### `enumerate()` a `range()`

```python
projekty = ["Login", "Checkout", "Dashboard"]
for i, projekt in enumerate(projekty, start=1):
    print("#" + str(i) + ":", projekt)

for cislo in range(3):
    print(cislo)  # 0,1,2
```

---

## 🔹 Nápověda a introspekce

```python
text = "Samuel"
print(dir(text))         # seznam metod objektu
help(str.upper)          # nápověda pro metodu upper()
```




# 🔹 Funkce vs. Metoda
# 	•	Funkce → volá se jako funkce(hodnota)
# – např. len("Python"), abs(-7), bool(0).
# – funkce je „globální nástroj“, kterému předáváš objekt jako argument.
# 	•	Metoda → volá se jako objekt.metoda()
# – např. "Python".lower(), "Ahoj".replace("A","B"), [1,2].append(3).
# – metoda „patří“ k objektu. Říkáš: „objekte, udělej na sobě tuto operaci“.

# 	•	s.lower() ✅ správně (metoda stringu)
# 	•	lower(s) ❌ špatně (není to globální funkce)
# 	•	s.lower ❌ špatně (bez závorek vrací jen odkaz na metodu, nespustí ji)