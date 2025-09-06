# Podmínky v Pythonu: přehled a příklady

## Jednoduché `if`
Spustí se jen tehdy, když podmínka platí (`True`).

```python
vek = 20
if vek >= 18:
    print("Dospělý")
```

➡️ Pokud `vek` je `20` → vytiskne se `Dospělý`.  
Pokud by `vek` byl `15` → **neprovede se nic**.

---

## `if` + `else`
`else` se provede, když podmínka neplatí.

```python
heslo = "tajne"

if heslo == "tajne":
    print("Přístup povolen")
else:
    print("Přístup zamítnut")
```

➡️ Pokud `heslo` je `"tajne"`, vytiskne se `Přístup povolen`.  
Jinak se vždy provede `Přístup zamítnut`.

---

## `if` + `elif` + `else`
Pro více možností. Python vyhodnocuje podmínky **shora dolů** – jakmile jednu splní, zbytek přeskočí.

```python
znamka = 3

if znamka == 1:
    print("Výborně")
elif znamka == 2:
    print("Chvalitebně")
elif znamka == 3:
    print("Dobře")
else:
    print("Nedostatečně")
```

---

## Vnořené podmínky
Jedna podmínka může být uvnitř druhé.

```python
vek = 20
obcan = True

if vek >= 18:
    if obcan:
        print("Může volit")
```

➡️ Nejprve se zkontroluje věk, a teprve pokud platí, kontroluje se občanství.

Podmínky můžeš dávat do sebe. Každé další vnoření znamená **další odsazení**.

```python
vek = 20
obcan = True

if vek >= 18:
    print("Dospělý")
    if obcan:
        print("Může volit")
```

➡️ Pokud `vek = 20` a `obcan = True`, výstup bude:
```
Dospělý
Může volit
```

➡️ Pokud `vek = 20` a `obcan = False`, výstup bude:
```
Dospělý
```

➡️ Pokud `vek = 15`, **nic se nevypíše**.

---

## Odsazování (indentace)
Kód patřící pod podmínku musí být **odsazený** (typicky 4 mezery).

```python
vek = 20

if vek >= 18:
    print("Dospělý")       # ← tohle je uvnitř podmínky
    print("Může vstoupit") # ← taky uvnitř podmínky
print("Hotovo")            # ← už mimo podmínku
```

➡️ Pokud `vek = 20`, vytiskne se:
```
Dospělý
Může vstoupit
Hotovo
```

➡️ Pokud `vek = 15`, vytiskne se:
```
Hotovo
```

---

## TIP: Truthiness (pravdivost hodnot)
Podmínka nemusí být jen `True`/`False`. Python převádí hodnoty podle pravidel:

```python
if "text":      # neprázdný string → True
    print("ano")

if []:          # prázdný list → False
    print("ne") # tohle se neprovede
```

---

## Prázdný blok: `pass`
Když ještě nevíš, co v bloku bude, použij `pass` (placeholder).

```python
vek = 20
if vek >= 18:
    pass  # nedělá nic, ale Python to dovolí
```

> `pass` je speciální příkaz, který **nedělá nic**.  
> Používá se jako zástupka tam, kde Python očekává blok kódu, ale ty ho zatím nemáš.

**Špatně** – prázdný blok bez `pass` vyvolá chybu odsazení:
```python
vek = 20
if vek >= 18:
    # tady není žádný kód → chyba
```

**Správně:**
```python
vek = 20
if vek >= 18:
    pass  # Python je spokojený
```

---

## Praktické použití `pass`
Při psaní „kostry“ programu nebo jako úmyslně prázdná větev:

```python
def kontrola_vek(vek):
    if vek >= 18:
        pass   # TODO: doplním později
    else:
        print("Mladistvý")

heslo = "tajne"
if heslo == "tajne":
    print("Přístup povolen")
else:
    pass   # nic nedělám, ale je vidět, že větev je záměrně prázdná
```

> Pamatuj: **`pass` = „nedělej nic, jen pokračuj“**. Hodí se při návrhu programu nebo jako jasná indikace, že daná větev má zůstat prázdná.

---

## ✨ Shrnutí
- **`if`** → provede se, když je podmínka `True`.  
- **`elif`** → další větev (jen když ty předchozí nebyly pravda).  
- **`else`** → „všechno ostatní“, pokud žádná podmínka nebyla splněná.  
- Podmínky se vyhodnocují **postupně shora dolů**.  
- **Odsazení je povinné** – určuje, co pod podmínku opravdu patří.  
- **`pass`** nechá větev prázdnou, ale syntakticky správnou.

# 🐍 Python – `if` a `else` (vnořené podmínky)

## 1️⃣ Vnořený `if`

```python
if vek >= 18:                 # vnější podmínka
    if prijem >= 20000:       # vnitřní podmínka
        print("Schváleno")
    else:
        print("Zamítnuto")    # řeší nízký příjem
else:
    print("Zamítnuto")        # řeší nízký věk
```

- **První `else`** patří k **vnitřnímu `if`** (příjem).  
- **Druhý `else`** patří k **vnějšímu `if`** (věk).  

---

## 2️⃣ Proč tam jsou dva `else`

Každý `if` může mít vlastní `else`.  
- Vnitřní `else` → když je člověk dost starý, ale má malý příjem.  
- Vnější `else` → když není dost starý.

---

## 3️⃣ Co když tam nebude vnitřní `else`

```python
if vek >= 18:
    if prijem >= 20000:
        print("Schváleno")
else:
    print("Zamítnuto")
```

Výsledky:
- `vek >= 18` a `prijem >= 20000` → **Schváleno**  
- `vek >= 18` a `prijem < 20000` → **nevytiskne se nic**  
- `vek < 18` → **Zamítnuto**  

---

## 4️⃣ Co když tam nebude vnější `else`

```python
if vek >= 18:
    if prijem >= 20000:
        print("Schváleno")
    else:
        print("Zamítnuto")
```

Výsledky:
- `vek >= 18` → funguje normálně (schváleno/zamítnuto podle příjmu)  
- `vek < 18` → **nevytiskne se nic**  

---

## 5️⃣ Shrnutí

- Každý `if` může mít svoje `else`.  
- `else` tam **nemusí být vždy**.  
- Když chybí, Python prostě neudělá nic a skočí dál.  
- Dáváš `else` vždy, když chceš pokrýt i „druhou možnost“.  

💡 Typická chyba: dát dva samostatné `if` místo `if` + `else`. Pak se může stát, že se spustí víc větví, než bys čekal.
