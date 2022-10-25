# ZADÁNÍ: https://kodim.cz/kurzy/python-data/zaklady-programovani/soubory/zapis-souboru

# CVIČENÍ 1

# Mzda nastavená přímo (pro jednoduchost), případně inputem od uživatele
mzda_hod = 200
# mzda_hod = int(input("Zadej hodinovou mzdu: "))

# Název souboru lze použít buď samostatně (pokud je ve stejné složce jako skript), nebo jako cesta k souboru
# ... "r" před cestou značí "raw" string, ve kterém python nevyhodnocuje speciální znaky začínající zpětným lomítkem (třeba "\n") - bez "r" by hodil chybu
nazev = "vykaz.txt"
# nazev = r"C:\Users\mapup\OneDrive\Dokumenty\Czechitas\2022-09-20_12-06 Python 1\Czechitas_Python1\Czechitas_Python1\vykaz.txt"

# Načteme řádky ze souboru do seznamu
with open(nazev, "r", encoding="utf-8") as file:
    lines = file.readlines()

hodiny = [int(line.rstrip()) for line in lines]
# print(hodiny)

vyplaty = [hodiny_mesic*mzda_hod for hodiny_mesic in hodiny]
# print(vyplaty)

# Příprava pro zápis do souboru: převod na string a přidání znaku nového řádku na každý řádek
vyplaty_zapis = [str(vyplata)+"\n" for vyplata in vyplaty]
# print(vyplaty_zapis)

# Zápis do souboru "vyplaty.txt"
# "w" (write) = otevíráme soubor pro zápis (přemaže jeho existující obsah)
# Alternativa: "a" (append) = zapisuje na konec souboru za existující obsah
with open("vyplaty.txt", "w", encoding="utf-8") as file:
    file.writelines(vyplaty_zapis)


# CVIČENÍ 2

import random

# Generování 10 náhodných hodů 12stěnnou kostkou...

# 1. způsob
# hody = []
# for i in range(10):
#     hody.append(random.randint(1,12))

# 2. způsob
hody = [random.randint(1,12) for i in range(10)]

# 3. způsob
# hody = random.sample(range(1,13),10)

# print(hody)

# Nejdřív převod na string, pak spojení prvků seznamu čárkou a mezerou
hody_zapis = [str(hod) for hod in hody]
with open("hody.txt", "w", encoding="utf-8") as file:
    # Metodou join spojíme prvky seznamu pomocí čárky a mezery
    file.writelines(", ".join(hody_zapis))