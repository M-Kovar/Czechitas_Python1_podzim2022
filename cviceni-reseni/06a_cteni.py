# ZADÁNÍ: https://kodim.cz/kurzy/python-data/zaklady-programovani/soubory/cteni-souboru

# CVIČENÍ 1

# Mzda nastavená přímo (pro jednoduchost), případně inputem od uživatele
mzda_hod = 200
# mzda_hod = int(input("Zadej hodinovou mzdu: "))

# Název souboru lze použít buď samostatně (pokud je ve stejné složce jako skript), nebo jako cesta k souboru
# ... "r" před cestou značí "raw" string, ve kterém python nevyhodnocuje speciální znaky začínající zpětným lomítkem (třeba "\n") - bez "r" by hodil chybu
nazev = "vykaz.txt"
# nazev = r"C:\Users\mapup\OneDrive\Dokumenty\Czechitas\2022-09-20_12-06 Python 1\Czechitas_Python1\Czechitas_Python1\vykaz.txt"

# Načteme řádky ze souboru do seznamu
# "r" (read) = otevíráme soubor jen pro čtení
with open(nazev, "r", encoding="utf-8") as file:
    lines = file.readlines()
# print(lines)

# Odstraníme znaky nových řádků zprava pomocí rstrip() a převedeme na int
hodiny = [int(line.rstrip()) for line in lines]
# print(hodiny)

# Výplata za rok
celkem_rok = sum(hodiny)*mzda_hod
# print(celkem_rok)

# Průměrná výplata měsíc
vyplata_mesic_prumer = celkem_rok/12
# print(vyplata_mesic_prumer)


# CVIČENÍ 2

filepath = "praha.txt"
# filepath = r"C:\Users\mapup\OneDrive\Dokumenty\Czechitas\2022-09-20_12-06 Python 1\Czechitas_Python1\Czechitas_Python1\praha.txt"

with open(filepath, "r", encoding="utf-8") as file:
    lines = file.readlines()
# print(lines)

# rstrip() nejdřív odstraní "\n" zprava
# split(" ") pak rozdělí každý řádek na slova (dělicím znakem je mezera)
radky = [line.rstrip().split(" ") for line in lines]
# print(radky)

# Výpis počtu slov pro každý řádek
for radek in radky:
    print(len(radek))

# Součet počtu slov
celkem = sum([len(radek) for radek in radky])
# print(celkem)