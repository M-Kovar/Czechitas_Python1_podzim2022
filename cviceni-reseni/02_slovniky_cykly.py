# ZADÁNÍ: https://kodim.cz/kurzy/uvod-do-progr-2/uvod-do-programovani-2/slovniky-a-cykly/excs

# CVIČENÍ 1

school_report = {
    "Český jazyk": 1,
    "Anglický jazyk": 1,
    "Matematika": 1,
    "Přírodopis": 2,
    "Dějepis": 1,
    "Fyzika": 2,
    "Hudební výchova": 4,
    "Výtvarná výchova": 2,
    "Tělesná výchova": 3,
    "Chemie": 4,
}

# Varianta 1:
soucet_znamek = 0
pocet_znamek = 0
for predmet in school_report:
    znamka = school_report[predmet]
    soucet_znamek += znamka
    pocet_znamek += 1
    if znamka == 1:
        print(predmet)

prumer_znamek = soucet_znamek / pocet_znamek
# print(prumer_znamek)

# Varianta 2 pro počítání průměru:
prumer_znamek = sum(school_report.values()) / len(school_report)
# print(prumer_znamek)

# Varianta 3 pro počítání průměru:
# Importujeme modul statistics - balíček statistických funkcí, ze kterého využijeme mean()
# "import" se obvykle píše hned na začátek souboru. Pro přehlednost jsem ho ale dal sem:
import statistics
# Na hodnoty z vysvědčení zavoláme metodu mean() z modulu statistics počítající průměr
prumer_znamek = statistics.mean(school_report.values())
# print(prumer_znamek)

# Bonus - kolik je na vysvědčení jedniček?:
hledana_znamka = 1
# 1. Funkcí list převedeme values (typ "dict_values") na seznam
# 2. Funkce count() spočítá výskyty zadaného prvku v seznamu
pocet_jednicek = list(school_report.values()).count(hledana_znamka)
# print(pocet_jednicek)


# CVIČENÍ 2

# Seznam slovníků
books = [
    {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
    {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
    {"title": "Past", "pages": 390, "rating": 4},
    {"title": "Popel popelu", "pages": 411, "rating": 10},
    {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
    {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
    {"title": "Zločinný steh", "pages": 542, "rating": 8},
    {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
    {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
]

pocet_stran = 0
pocet_nad_osm = 0
# Procházíme books a do proměnných "sbíráme" počet stran a počet knih s ratingem 8+
for book in books:
    pocet_stran += book["pages"]
    if book["rating"] >= 8:
        pocet_nad_osm += 1

# print(pocet_stran)
# print(pocet_nad_osm)

# Nepovinný bonus - řešení "pocet_stran" pomocí list comprehension:
# (toto budeme probírat v druhé půlce kurzu)
# ...for...in... vytvoří seznam počtu stránek, který se pak sečte pomocí sum()
pocet_stran = sum(book["pages"] for book in books)
# print(pocet_stran)


# CVIČENÍ 3 (BONUS)

spzetky = {
    "4A2 3000": "František Novák",
    "6P5 4747": "Jana Pilná",
    "3B7 3652": "Jaroslav Sečkár",
    "1P5 5269": "Marta Nováková",
    "37E 1252": "Martina Matušková",
    "2A5 2241": "Jan Král"
    }

print('Lidé z Plzeňského kraje:')
for spz, jmeno in spzetky.items():
    if spz[1] == 'P':
        print(f'- {jmeno}')