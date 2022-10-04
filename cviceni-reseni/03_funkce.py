# ZADÁNÍ: https://kodim.cz/kurzy/uvod-do-progr-2/uvod-do-programovani-2/funkce/excs

# ---
# Nesouvisející tip:
# "Dlouhá" čísla lze pro přehlednost rozdělovat podtržítky (chová se jako standardní číslo)
x = 1_000_000
y = 0.000_000_001
# print(x)
# print(y)  # Vypíše se ve "vědeckém" formátu jako 1e-06, ale hodnota je stále 0.000000001
# ---


# CVIČENÍ 1

# Definování funkce (musí být vždy před/nad jejím voláním)
def mult(a, b):
    return a*b

cislo1 = 2
cislo2 = 3
# ... proměnné vstupující do funkce se mohou jmenovat libovolně (nemusí být a,b)
vysledek = mult(cislo1, cislo1)
# print(vysledek)


# CVIČENÍ 2

def total_price(persons, breakfast=False):
    cena_osoba = 850
    cena_snidane = 125

    # 1. varianta:
    # if breakfast:
    #     celkem = persons*(cena_osoba + cena_snidane)
    # else:
    #     celkem = persons*cena_osoba

    # 2. varianta:
    celkem = cena_osoba*persons
    if breakfast:
        celkem += cena_snidane*persons
      
    return celkem

# Nepovinný argument můžeme zadat různými způsoby...
# print(total_price(2))
# print(total_price(2, False))
# print(total_price(2, True))
# print(total_price(2, breakfast=True))


# CVIČENÍ 3 (BONUS)

def mesic_narozeni(rodne_cislo):
    # Měsíc získáme jako třetí a čtvrtý znak (indexování od nuly)
    # ... Indexuje se jako [2:4], jelikož horní hranici (4) Python nezahrnuje, bere tedy jen indexy 2 a 3
    cislo_mesice = int(str(rodne_cislo)[2:4])
    if cislo_mesice > 12:
        cislo_mesice -= 50
    return cislo_mesice

# print(f'9207054439 -> {mesic_narozeni(9207054439)}')
# print(f'9555125899 -> {mesic_narozeni(9555125899)}')


# CVIČENÍ 4 (BONUS)

import random

vybrana_rada = int(input('Na kterou řadu sázíš? (1-3): '))
vsazeno = int(input('Kolik sázíš?: '))

def ruleta(cislo_rady, sazka):
    rady = [
        range(1, 37, 3),  # 1, 4, 7, ...
        range(2, 37, 3),  # 2, 5, 8, ...
        range(3, 37, 3),  # 3, 6, 9, ...
        ]
    hozeno = random.randint(0, 36)
    # print(f"Hozeno: {hozeno}")
    # Ukázka jednořádkového zápisu if (elegantní, ale pro přehlednost by se možná vyplatilo rozepsat na víc řádků):
    return 2 * sazka if hozeno in rady[cislo_rady - 1] else 0  # "- 1" kvůli indexování od nuly

vyhra = ruleta(vybrana_rada, vsazeno)
# print(f"Vyhráváš {vyhra}")