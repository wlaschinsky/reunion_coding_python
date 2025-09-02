# 🐍 Python – Lekce 2 (část 1–2)

## 🔹 Úvod do rozhodování

### Proč to potřebujeme?
Programy zatím vykonávaly příkazy shora dolů bez rozhodování.  
Ale v praxi potřebujeme, aby program **sám rozhodoval podle situace**.  

📌 Příklady:
- Pokud je věk uživatele ≥ 18 → povolíme vstup.  
- Pokud heslo = `"tajne"` → přístup povolen, jinak zamítnut.  
- Pokud je seznam prázdný → vypíšeme „košík je prázdný“.  

👉 K tomu slouží **podmínky (`if`)** a hodnoty `True/False`.

---

### První ukázka kódu
```python
vek = 20

if vek >= 18:
    print("Můžeš vstoupit")
```

- pokud je `vek` 20 → vytiskne se text  
- pokud je `vek` 15 → nevytiskne se nic (podmínka nebyla splněna)

---

### Další ukázky
```python
vek = 15
if vek >= 18:
    print("Můžeš vstoupit")
print("Hotovo")
```

**Výstup:**
```
Hotovo
```

➡️ protože `if` se nesplní, ale příkaz `print("Hotovo")` je mimo blok podmínky → provede se vždy.

---

## 🔹 Datový typ `bool`

### Co je to `bool`?
- Speciální datový typ se dvěma hodnotami:  
  - `True` (pravda)  
  - `False` (nepravda)

```python
print(True)
print(False)
print(type(True))   # <class 'bool'>
```

---

### Převod na `bool`

Pomocí funkce `bool()` převedeme cokoliv na pravdu/nepravdu.  

📌 Pravidlo:
- „prázdné“ = `False`  
- „neprázdné“ = `True`

```python
# Čísla
print(bool(0))      # False
print(bool(42))     # True
print(bool(-3))     # True

# Řetězce
print(bool(""))     # False (prázdný string)
print(bool("x"))    # True (neprázdný string)

# Seznamy
print(bool([]))     # False (prázdný list)
print(bool([0]))    # True (list obsahuje prvek)
```

---

### Praktický příklad
```python
heslo = "tajne"

if bool(heslo):    # stejné jako if heslo:
    print("Heslo existuje")
```

- pokud `heslo = "tajne"` → `True` → vypíše se  
- pokud `heslo = ""` → `False` → nevypíše se


## 🔹 Přehled truthiness (co je True/False)

| Hodnota            | Výsledek `bool()` |
|---------------------|-------------------|
| `0`, `0.0`         | False             |
| Nenulová čísla     | True              |
| `""` (prázdný str) | False             |
| `"0"` (string!)    | True              |
| `" "` (mezera)     | True              |
| `[]`, `{}`, `()`   | False             |
| `[0]`              | True              |
| `None`             | False             |

---

## 🔹 Shrnutí – tipy

- `bool("0")` → True *(neprázdný string)*  
- `bool(0.0)` → False *(nula)*  
- `bool(" ")` → True *(mezera je pořád znak)*  
- `bool({})` → False *(prázdný dict)*  
- `bool(None)` → False *(hodnota None)*  


## Zlaté pravidlo (shrnutí)
	•	Čísla: jen 0 (a 0.0) je False, jinak True.
	•	Řetězce: jen "" je False, jinak True.
	•	Kontejnery: prázdný je False, neprázdný True.
	•	None je vždy False.


print(bool([0])) → True ❌
Pozor: u kontejnerů (list/tuple/dict/set) rozhoduje prázdnost, ne „hodnota uvnitř“.
[0] je neprázdný list → True.