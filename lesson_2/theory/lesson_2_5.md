# 🐍 `input()` v Pythonu

## 🔹 Co dělá
- `input("text")` → vypíše text (tzv. *prompt*) a zastaví program.
- Čeká, až uživatel něco napíše a zmáčkne Enter.
- To, co napíšeš, se vrátí jako řetězec (`str`).

```python
jmeno = input("Zadej jméno: ")
print("Ahoj,", jmeno)
```

```
Zadej jméno: Samuel
Ahoj, Samuel
```

## 🔹 Důležitá vlastnost

`input()` vždy vrací string, i když napíšeš číslo!

```python
vek = input("Zadej věk: ")
print(vek, type(vek))   # např. "25" <class 'str'>
```

## 🔹 Převod na číslo

Pokud potřebuješ číslo (např. porovnání věku), musíš převést:

```python
vek = int(input("Zadej věk: "))  # převedeno na int
if vek >= 18:
    print("Dospělý")
else:
    print("Mladistvý")
```

Podobně pro desetinná čísla:

```python
cislo = float(input("Zadej desetinné číslo: "))
```

## 🔹 Typické chyby a na co si dát pozor

### 1. Zapomeneš převést na číslo

```python
vek = input("Zadej věk: ")
if vek >= 18:     # ❌ Chyba! porovnáváš string a int
    print("OK")
```
➡️ Python vyhodí `TypeError`.

---

### 2. Uživatel zadá neplatný vstup

```python
vek = int(input("Zadej věk: "))  # napíšu "abc"
```
➡️ Spadne s `ValueError`. (řeší se později pomocí `try/except`).

---

### 3. Mezery a prázdný vstup

```python
heslo = input("Zadej heslo: ")
if not heslo:
    print("Heslo chybí")
```
➡️ Pokud uživatel jen stiskne Enter, je to prázdný string `""`.

---

### 4. `input()` vždy vrátí vše, co napíšeš

```python
text = input("Napiš něco: ")
print("Zadal jsi:", text)
```
➡️ Když napíšeš `123abc`, program vezme celý řetězec `"123abc"`.

---

### 5. Chyba v pořadí převodu

❌ Špatně:
```python
int_vek = input(int("Zadej věk: "))  # TypeError
```

✔️ Správně:
```python
vek = int(input("Zadej věk: "))
```

## ✨ Shrnutí

- `input()` → vždy vrací `string`.
- Pro čísla musíš použít `int()` nebo `float()`.
- Dávej pozor na prázdný vstup nebo nečíselný text.
- Při zadání může být i mezera, čísla, písmena — všechno se bere jako text.