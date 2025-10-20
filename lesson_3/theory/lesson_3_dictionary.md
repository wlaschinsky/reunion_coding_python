
# 🐍 List vs Tuple vs Slovník v Pythonu

## 📋 LIST `[]`
- **Měnitelný (mutable)**.
- Přístup přes **index**.
- Lze **přidávat** (`append`, `insert`) a **mazat** (`del`, `remove`).
- Udržuje pořadí, může mít **duplicity**.

### 🔍 Příklad:
```python
ovoce = ["jablko", "banán", "hruška"]
ovoce[1] = "pomeranč"      # změna
ovoce.append("třešeň")     # přidání
del ovoce[0]               # odstranění
print(ovoce)               # ['pomeranč', 'hruška', 'třešeň']
```

---

## 🔐 TUPLE `()`
- **Neměnitelný (immutable)**.
- Přístup přes **index**.
- Nelze **přidávat**, **mazat** ani **měnit hodnoty**.
- Vhodný pro **fixní data**.

### 🔍 Příklad:
```python
barvy = ("červená", "modrá", "zelená")
print(barvy[0])             # červená
# barvy[0] = "žlutá"        ❌ chyba
```

> 💡 **Výjimka**: tuple může obsahovat list → ten se měnit dá.

```python
data = (1, [2, 3], 4)
data[1].append(5)
print(data)  # (1, [2, 3, 5], 4)
```

---

# 🧾 Slovníky (`dict`) – základní princip

## 🔹 Co je slovník
Slovník v Pythonu je **kolekce dat ve formátu klíč → hodnota**.  
Představ si ho jako tabulku nebo kartotéku – **každý klíč** (např. `"jméno"`) má svou **hodnotu** (např. `"Samuel"`).

### 💬 Příklad:
```python
uzivatel = {
    "jmeno": "Samuel",
    "vek": 29,
    "mesto": "Brno"
}
```

`uzivatel` je slovník.  
Klíče: `"jmeno"`, `"vek"`, `"mesto"`  
Hodnoty: `"Samuel"`, `29`, `"Brno"`

---

## 🔹 Vlastnosti slovníku
- Měnitelný (**mutable**) – lze přidávat, měnit, mazat hodnoty.  
- Klíče musí být **unikátní** (nemohou se opakovat).  
- Klíče musí být **neměnitelné** (např. string, int, tuple).  
- Hodnoty mohou být **libovolné** (čísla, texty, listy, jiné slovníky).  
- Pořadí klíčů je zachováno (od Pythonu 3.7+).

---

## 🔹 Vytvoření slovníku
```python
# 1️⃣ běžně pomocí složených závorek
osoba = {"jmeno": "Anna", "vek": 25}

# 2️⃣ prázdný slovník
data = {}

# 3️⃣ pomocí funkce dict()
student = dict(jmeno="Eva", vek=22)
```

---

## 🔹 Přístup k hodnotám
```python
print(osoba["jmeno"])  # Anna
```
❗Pokud se pokusíš přistoupit ke klíči, který neexistuje:
```python
print(osoba["mesto"])  # ❌ KeyError
```

Bezpečnější varianta:
```python
print(osoba.get("mesto"))  # ✅ None (program nespadne)
```

---

## 🔹 Přidání nového klíče
```python
osoba["mesto"] = "Praha"
print(osoba)
# {'jmeno': 'Anna', 'vek': 25, 'mesto': 'Praha'}
```

---

## 🔹 Změna hodnoty
```python
osoba["vek"] = 26
print(osoba)
# {'jmeno': 'Anna', 'vek': 26, 'mesto': 'Praha'}
```

---

## 🔹 Mazání klíče
```python
del osoba["mesto"]
print(osoba)
# {'jmeno': 'Anna', 'vek': 26}
```
Pokud smažeš neexistující klíč:
```python
del osoba["adresa"]  # ❌ KeyError
```

---

## 🔹 Další způsoby mazání
```python
# odstraní a zároveň vrátí hodnotu
hodnota = osoba.pop("vek")
print(hodnota)   # 26

# odstraní všechny položky
osoba.clear()
print(osoba)  # {}
```

---

## 🔹 Průchod slovníkem
```python
for klic in osoba:
    print(klic, osoba[klic])
```

Nebo více elegantně:
```python
for klic, hodnota in osoba.items():
    print(f"{klic}: {hodnota}")
```

---

## 🔹 Vnořený slovník
```python
student = {
    "jmeno": "Eva",
    "rocnik": 2,
    "predmety": {
        "matematika": 1,
        "anglictina": 2
    }
}

print(student["predmety"]["anglictina"])  # 2
```

---

## 🔹 Užitečné metody slovníku
| Metoda | Popis | Příklad |
|--------|--------|----------|
| `.keys()` | Vrátí všechny klíče | `osoba.keys()` |
| `.values()` | Vrátí všechny hodnoty | `osoba.values()` |
| `.items()` | Vrátí klíče i hodnoty jako dvojice | `osoba.items()` |
| `.update()` | Sloučí dva slovníky | `osoba.update({"vek": 30})` |
| `.get()` | Bezpečný přístup ke klíči | `osoba.get("mesto", "Neznámé")` |
| `.pop()` | Odstraní a vrátí hodnotu | `osoba.pop("vek")` |
| `.clear()` | Vyprázdní slovník | `osoba.clear()` |

---

## 💡 Shrnutí
- Slovník ukládá dvojice klíč–hodnota.  
- Klíče jsou unikátní a neměnitelné.  
- Hodnoty lze měnit, přidávat i mazat.  
- Na rozdíl od listu se přistupuje **přes klíč, ne přes index**.  
- Vnořené slovníky umožňují ukládat komplexní data.