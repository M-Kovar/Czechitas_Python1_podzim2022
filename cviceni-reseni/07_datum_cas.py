# Jupyter
# markdown  Jednoduché formátování textu (jako v githubu)
# LaTeX     Rovnice, např. $P(A \mid B) = \frac{P(B \mid A)P(A)}{P(B)}$
# funkce?   Nápověda k funkci, např. print?

# ZADÁNÍ: https://kodim.cz/kurzy/python-data-1/bonusy/datum/datum

# Užitečné funkce/metody
# datetime.now()            Aktuální datum a čas
# datetime.day              Číslo dne objektu datetime (podobně year, month, hour, minute, second, microsecond)
# datetime.weekday()        Den v týdnu (pořadí číslované od 0=pondělí)
# datetime.isoweekday()     Den v týdnu (pořadí číslované od 1=pondělí)
# datetime.isoformat()      Výpis v ISO formátu ('1969-07-16T14:32:00')
# datetime.fromisoformat()  Zadání data v ISO formátu
# datetime.strptime()       Zadání data podle vlastního formátu
# datetime.strftime()       Výpis ve vlastním formátu (%d den, %m měsíc, %Y rok, %H hodina, %M minuta, %S sekunda)


# import datetime   # Importuje obsah do proměnné datetime, metody pak voláme jako datetime.metoda()
from datetime import datetime, timedelta, date   # Importuje obsah přímo mezi naše proměnné (pozor na proměnné se shodným názvem), metody voláme jako metoda()


# CVIČENÍ 1
apollo_start = datetime(1969, 7, 16, 14, 32)
apollo_start_US_format = apollo_start.strftime("%m/%d/%Y")
print(apollo_start)
print(apollo_start_US_format)


# CVIČENÍ 2
start = datetime(2020, 2, 10, 5, 3)
# print(start)
start_den = start.weekday()
# print(start_den)
cas_od_startu = datetime.now() - start
print(cas_od_startu)
start_den = start.isoweekday()
# start_den = start.strftime("%A")
print(f"Den startu Solar Orbiteru: {start_den}")
print(f"Čas uplynulý od startu Solar Orbiteru: {cas_od_startu}")


# CVIČENÍ 3
cas_objednavky = datetime(2020, 11, 13, 19, 47)
doba_prevzeti = timedelta(minutes=8, seconds=35)
doba_priprava = timedelta(minutes=30)
doba_doprava = timedelta(minutes=25, seconds=30)
doba_celkove = doba_prevzeti + doba_priprava + doba_doprava
print(f"Celková doba doručení objednávky: {doba_celkove}")

cas_doruceni = cas_objednavky + doba_celkove
print(f"Vytvoření objednávky: {cas_objednavky}")
print(f"Doručení objednávky: {cas_doruceni}")