# 🐍 Přehled základních funkcí v Pythonu

## 📌 Přehled funkcí

| Funkce        | K čemu slouží                                        | Příklad                                      |
|---------------|------------------------------------------------------|----------------------------------------------|
| `type()`      | Vrátí typ hodnoty                                    | `type(3.14)` → `<class 'float'>`             |
| `len()`       | Délka sekvence (str, list, tuple, ...)               | `len("Python")` → `6`                        |
| `int()`       | Převod na celé číslo                                 | `int("42")` → `42`                           |
| `float()`     | Převod na desetinné číslo                            | `float("3.5")` → `3.5`                       |
| `str()`       | Převod na řetězec                                    | `str(123)` → `"123"`                         |
| `round()`     | Zaokrouhlení (volitelně na n desetinných míst)       | `round(3.1415, 2)` → `3.14`                  |
| `abs()`       | Absolutní hodnota                                    | `abs(-7)` → `7`                              |
| `min()`/`max()`| Minimum / maximum v iterovatelném objektu           | `max([3,8,2])` → `8`                          |
| `sum()`       | Součet čísel                                         | `sum([1,2,3])` → `6`                          |
| `sorted()`    | Vrátí seřazenou kopii                                | `sorted([3,1,2])` → `[1,2,3]`                |
| `enumerate()` | Číslované procházení v `for` cyklu                   | `enumerate(["a","b"])` → `(0,"a"), (1,"b")`  |
| `range()`     | Generátor posloupnosti čísel                         | `range(3)` → `0, 1, 2`                       |

---

## 💡 Tipy

- Průměr čísel: `avg = sum(hodnoty) / len(hodnoty)`  
  *(pozor na prázdný seznam → `ZeroDivisionError`)*
- Seřazení beze změny původního listu: `nova = sorted(puvodni)`
- Zaokrouhlení na dvě desetinná místa: `round(x, 2)`
- Součet části seznamu: `sum(ceny[:3])` *(slicing!)*

---

## 🧠 Funkce vs. Metody

| Příklad         | Co to je                 | Poznámka                                |
|-----------------|--------------------------|-----------------------------------------|
| `len(x)`        | vestavěná **funkce**     | Funguje globálně                        |
| `x.upper()`     | **metoda** typu `str`    | Metoda objektu                          |
| `sorted(x)`     | vestavěná **funkce**     | Vrací novou kopii                       |
| `x.append(y)`   | **metoda** typu `list`   | Mění přímo objekt (list)                |
| `enumerate(x)`  | vestavěná **funkce**     | Vrací index + hodnotu                   |

---

## 🔍 Nápověda a zkoumání objektů

```python
from inspect import Parameter

text = "Samuel"
print(type(text))      # <class 'str'>
print(dir(text))       # výpis metod dostupných pro str
help(str.upper)        # nápověda ke konkrétní metodě
```

---

## 🧩 Metoda vs. Funkce – polopatě

- **Funkce** je „obecná“ – voláš ji jako `funkce(hodnota)`
  - např. `len("Python")`, `abs(-7)`, `round(...)`, `sorted(...)`
- **Metoda** „patří objektu“ – voláš ji jako `objekt.metoda(...)`
  - např. `"ahoj".upper()`, `["a"].append("b")`, `"text".replace("t","T")`

💡 Pomůcka:
- `len(x)` = ptám se Pythonu
- `x.upper()` = říkám objektu `x`, ať něco udělá

---

## 🔀 Rozdíl: `sorted()` vs. `.sort()`

|              | `sorted()`                 | `.sort()`                         |
|--------------|----------------------------|------------------------------------|
| Typ          | Funkce                     | Metoda objektu `list`             |
| Mění původní?| ❌ Ne                      | ✅ Ano                             |
| Vrací co?    | Nový seřazený list         | `None`                            |
| Parametry    | `key=`, `reverse=`         | `key=`, `reverse=`                |

### 🧪 Příklady

```python
cisla = [3, 1, 4, 2]
nove = sorted(cisla)
print("Původní:", cisla)   # [3, 1, 4, 2]
print("Nový:", nove)       # [1, 2, 3, 4]

cisla.sort()
print("Po sort():", cisla) # [1, 2, 3, 4]

jmena = ["Adam", "petr", "anna"]
print(sorted(jmena, key=str.lower))  # ['Adam', 'anna', 'petr']
print(sorted(jmena, reverse=True))   # ['petr', 'anna', 'Adam']

jmena.sort(key=str.lower)
print(jmena)  # ['Adam', 'anna', 'petr']
```

---

## 🔹 Funkce `any()`

Vrátí `True`, pokud **alespoň jedna** hodnota je pravdivá.

👉 Polopatě: „Je tam *něco pravdivého*?“

### 🧪 Příklady

```python
any([False, False, True])    # True
any([0, 0, 5])               # True (5 je nenulové číslo → True)
any(["", "", "Python"])      # True (neprázdný string → True)

# Kontrola hesla na číslici
heslo = "abc123"
ma_cislici = False
for znak in heslo:
    if znak.isdigit():
        ma_cislici = True
        break

print(ma_cislici)  # True
```

---

## 🔹 Funkce `all()`

Vrátí `True`, pokud **všechny** hodnoty jsou pravdivé.

👉 Polopatě: „Jsou *všechny* pravdivé?“

### 🧪 Příklady

```python
all([True, True, True])      # True
all([1, 2, 3, 4])            # True (všechna čísla nenulová)
all(["Python", "Test", "Ahoj"])   # True

cisla2 = [1, 0, 3, 4]
print(all(cisla2))  # False (je tam 0 → False)

slova2 = ["Python", "", "Ahoj"]
print(all(slova2))  # False (prázdný string → False)

# Kontrola hesla – všechny znaky jsou číslice?
heslo = "12345"
cislo_heslo = True
for znak in heslo:
    if not znak.isdigit():
        cislo_heslo = False
        break

print(cislo_heslo)  # True
```

---

## 🧠 Shrnutí `any()` vs. `all()`

| Funkce  | Vrací `True`, když...                | Příklad                       |
|---------|--------------------------------------|-------------------------------|
| `any()` | Alespoň **jedna** hodnota je `True` | `any([0, "", "x"])` → `True` |
| `all()` | **Všechny** hodnoty jsou `True`     | `all([1, "ok", True])` → `True` |

```python
# Pro trénink:
values = [1, 2, 0]
print(any(values))  # True
print(all(values))  # False
```