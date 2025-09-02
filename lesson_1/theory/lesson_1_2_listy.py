# TOPIC: LISTY -> List je proměnná, která může uchovávat více hodnot najednou – jako krabička s oddělenými přihrádkami.

ovoce = ["jablko", "banán", "hruška"]
# •	ovoce je list
# •	obsahuje tři hodnoty typu str
# •	hodnoty jsou oddělené čárkami a celý list je v hranatých závorkách 

# +------------------------------+-----------------------------+
# | Co umí list                 | Jak                        |
# +------------------------------+-----------------------------+
# | Uchovat více hodnot         | ["a", "b", "c"]             |
# | Indexovat (od 0)            | ovoce[0] → "jablko"         |
# | Měnit hodnoty               | ovoce[1] = "pomeranč"       |
# | Přidávat hodnoty            | ovoce.append("třešeň")      |
# | Mazat hodnoty               | del ovoce[2]                |
# +------------------------------+-----------------------------+

seznam = [10, 20, 30]
print(seznam[0])      # 10
seznam.append(40)     # přidá 40 na konec
print(seznam)         # [10, 20, 30, 40]
seznam[1] = 25        # přepíše hodnotu na indexu 1
print(seznam)         # [10, 25, 30, 40]


# EXERCISES:	
    # 1.	Vytvoř list s názvy 3 měst (např. ["Praha", "Brno", "Ostrava"])
	# 2.	Vypiš druhé město (pozor na indexy!)
	# 3.	Přidej nové město pomocí .append()
	# 4.	Změň první město na "Plzeň"
	# 5.	Smaž třetí město pomocí del
city =  ["Praha", "Brno", "Ostrava"]
print(city[1])  # Vypíše druhé město: Brno
city.append("Plzeň")  # Přidá nové město: Plzeň
print(city)  # Vypíše: ['Praha', 'Brno', 'Ostrava', 'Plzeň']
print(city[:])  # Vypíše první město: Praha
city[0] = "Plzeň"  # Změní první město na Plzeň
print(city)  # Vypíše: ['Plzeň', 'Brno', 'Ostrava', 'Plzeň']
del city[2]  # Smaže třetí město (Ostrava)
print(city)  # Vypíše: ['Plzeň', 'Brno', 'Plzeň']

