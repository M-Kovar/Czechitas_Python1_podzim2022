# ZADÁNÍ: https://kodim.cz/kurzy/uvod-do-progr-2/uvod-do-programovani-2/slovniky/excs

# CVIČENÍ 1

vysvedceni = {
    "matematika": 1, 
    "český jazyk": 3,
    "fyzika": 1
    }

print(vysvedceni)
# ------

# CVIČENÍ 2

sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}
# print(sales)

sales["Noc, která mě zabila"] = 0
# print(sales)

# Preferovaný zápis:
sales["Vrah zavolá v deset"] += 100
# ... je ekvivalentní tomuto zápisu:
# sales["Vrah zavolá v deset"] = sales["Vrah zavolá v deset"] + 100

print(sales)

# ------

# CVIČENÍ 3

tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}
# print(tombola)

cislo_uzivatele = int(input('Zadej sve cislo listku: '))

# Varianta 1:
# if cislo_uzivatele in tombola:
#     vyhra = tombola[cislo_uzivatele]
#     tombola.pop(cislo_uzivatele)
# else:
#     vyhra = 'Bohužel nevyhráváš nic.'

# Varianta 2:
# (pokud metoda get nenajde záznam podle cislo_uzivatele, vrátí druhý argument, tedy 'Bohužel nevyhráváš nic.')
# vyhra = tombola.get(cislo_uzivatele, 'Bohužel nevyhráváš nic.')
# tombola.pop(cislo_uzivatele)

# Varianta 3 (preferovaná, protože je nejjednodušší):
# (metoda pop ze slovníku odstraní záznam podle cislo_uzivatele a navíc vrátí jeho hodnotu do proměnné vyhra)
vyhra = tombola.pop(cislo_uzivatele, 'Bohužel nevyhráváš nic.')

print(f"Výhra: {vyhra}")
# print(tombola)

# ------

# CVIČENÍ 4 (BONUS)

passwords = {
    "Jiří": "tajne-heslo", 
    "Natálie": "jeste-tajnejsi-heslo", 
    "Klára": "nejtajnejsi-heslo"
    }

jmeno = input("Zadej své jméno: ")

if jmeno in passwords:
    heslo = input("Zadej heslo: ")
    if heslo == passwords[jmeno]:
        print("Smíš vstoupit.")
    else:
        print("Špatné heslo.")
    # Alternativní jednořádkový zápis této vnořené podmínky (ukázka "syntactic sugar" v Pythonu):
    # print("Smíš vstoupit.") if heslo == passwords[jmeno] else print("Špatné heslo.")
else:
    print("Nejsi na seznamu.")