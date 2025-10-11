
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

## 🧾 SLOVNÍK `{key: value}`
- **Měnitelný (mutable)**.
- Přístup přes **klíče** místo indexů.
- Klíče musí být **unikátní** a **neměnitelné** (např. `string`, `číslo`, `tuple`).
- Hodnota může být **libovolná**.

### 🔍 Příklad:
```python
student = {"jmeno": "Eva", "vek": 20}
student["vek"] = 21              # změna hodnoty
student["obor"] = "Informatika" # přidání nové dvojice
del student["jmeno"]             # smazání klíče
print(student)                   # {'vek': 21, 'obor': 'Informatika'}
```

### 🎯 Přístup k hodnotám:
```python
print(student["vek"])            # 21
```

### ✅ Ověření existence klíče:
```python
print("vek" in student)          # True
print("jmeno" in student)        # False
```
