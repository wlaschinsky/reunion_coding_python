# 🐍 Python – Lekce 2 (část 3) – Operátory

## 3.1 Porovnávací operátory

Vrací vždy hodnotu typu `bool` (`True`/`False`):

- `==` rovnost  
- `!=` nerovnost  
- `<`, `<=` menší (nebo rovno)  
- `>`, `>=` větší (nebo rovno)

```python
print(5 == 5)      # True
print(5 != 3)      # True
print(2 < 2)       # False
print(2 <= 2)      # True
print("a" < "b")   # True  (řetězce se porovnávají podle pořadí znaků)
print("A" < "a")   # True  (velká písmena mají „menší“ kód než malá)

print("python" == "Python")          # False
print("python".lower() == "Python".lower())  # True  (normalizace)

x = 5
print(1 < x < 10)  # True  (čitelné a běžné v Pythonu)
```

---

## 3.2 Logické operátory

- `and` – vše musí být True  
- `or` – stačí alespoň jedno True  
- `not` – negace (obrácení)

```python
vek = 20
obcan = True
print(vek >= 18 and obcan)     # True  (oba podvýrazy True)

student = False
print(vek >= 18 or student)    # True  (aspoň jeden True)

print(not (vek >= 18))         # False  (negace)
```

### Krátké vyhodnocování (short-circuit)

Python se zastaví hned, jak zná výsledek:

- u `and` stačí jedno False → zbytek neřeší  
- u `or` stačí jedno True → zbytek neřeší  

To se hodí u kontrol typu: „nejdřív ověř, že něco existuje, a teprve potom s tím pracuj“.

---

## 3.3 Členství a identita (rychlý úvod)

### Členství: `in`, `not in`
Slouží ke kontrole, jestli je prvek uvnitř kolekce nebo řetězce.

```python
print("py" in "python")        # True
print(3 in [1,2,3])            # True
print("x" not in "python")     # True
```

### Identita: `is`, `is not`
Porovnává, zda jde o tentýž objekt v paměti (ne jen stejnou hodnotu).

👉 Začátečníkům stačí: pro rovnost hodnot používej `==`, ne `is`.

```python
a = [1,2]
b = [1,2]
print(a == b)  # True  (stejné hodnoty)
print(a is b)  # False (jiný objekt)
```

	•	== ➝ porovnává hodnoty (obsah).
	•	is ➝ porovnává identitu objektů v paměti (jestli je to ten samý objekt).

    a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)   # True  → seznamy mají stejný obsah
print(a is b)   # False → jsou to dva různé objekty v paměti

c = a
print(a is c)   # True  → c je jen jiný „štítek“ pro stejný objekt