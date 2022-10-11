# ZADÁNÍ: https://kodim.cz/kurzy/uvod-do-progr-2/uvod-do-programovani-2/tridy/excs

# CVIČENÍ 1

# Definice třídy Balik
class Balik:

    # Inicializace instance (objektu) třídy Balik
    # Automaticky se volá při zakládání objektu, např. pomocí Balik('Petr - Praha 10', 10)
    def __init__(self, adresa, hmotnost):
        self.adresa = adresa
        self.hmotnost = hmotnost
        self.doruceno = False   # Pro každý balík "automaticky" nastavujeme na False

    # Metoda pro "reprezentaci" třídy v uživatelsky přívětivém formátu
    # Automaticky ji např. volá print()
    def __str__(self):
        # "vypis" je lokální proměnná jen v této metodě, tzn. není to atribut třídy (proto nepíšeme jako "self.vypis")
        if self.doruceno:
            vypis = "dorucen"
        else:
            vypis = "nedorucen"
        # Vrací string
        return f"Balik na adresu {self.adresa} o hmotnosti {self.hmotnost} - {vypis}"

    # Metoda pro aktualizaci stavu doručení
    def doruc(self):
        self.doruceno = True

    # Metoda pro změnu adresy (jen pro ukázku - není v zadání)
    def zmen_adresu(self, nova_adresa):
        self.adresa = nova_adresa


# Založíme si nový objekt třídy Balik a uložíme ho do proměnné balik1
balik1 = Balik('Petr - Praha 10', 10)
# Podíváme se na informace o balíku (print zavolá metodu __str__ v Balik)
print(balik1)
# Zavoláme metodu .doruc(), která změní stav doruceno na True
balik1.doruc()
# Znovu se podíváme na informace o balíku - teď už by měl být doručen
print(balik1)

# Založíme si další balík (nezávislý na prvním balíku) a vypíšeme o něm informace
balik2 = Balik('Andrea - Plzeň', 20)
print(balik2)
# Zkusíme změnit adresu
balik2.zmen_adresu("Rudolf - Brno")
print(balik2)


# CVIČENÍ 2

class Kniha:
    def __init__(self, nazev, pocet_stran, cena):
        self.nazev = nazev
        self.pocet_stran = pocet_stran
        self.cena = cena
        # Metoda nic nevrací (jen ukládá atributy "do" objektu), takže není potřeba return
        # (... podobně u ostatních metod)

    def sleva(self, procent):
        # Zlevňujeme o x %, tzn. pokud procent = 20, bude nová cena 80 %(0.8) ceny původní
        self.cena *= 1 - (procent / 100)

    def __str__(self):
        return f'{self.nazev}, {self.pocet_stran} stran - {self.cena} Kč'

# Založíme knihu Motýlek o 300 stranách s cenou 100 Kč
k = Kniha('Motýlek', 300, 100)
print(k)
# Zlevníme o 20 procent a vypíšeme znovu informace - cena bude nižší
k.sleva(20)
print(k)


# CVIČENÍ 3

class Zamestnanec:
    def __init__(self, jmeno, pozice, zkusebni_doba):
        self.jmeno = jmeno
        self.pozice = pozice
        self.zkusebni_doba = zkusebni_doba

    def __str__(self):
        vypis = f"{self.jmeno} pracuje na pozici {self.pozice}. "
        # Pokud je ve zkušebce, připojíme to do výpisu
        if self.zkusebni_doba:
            vypis += "Je ve zkušební době."
        return vypis
        # Jednořádková Alternativa založená na zkráceném zápisu if/else:
        # return f"{self.jmeno} pracuje na pozici {self.pozice}." \
        #        f"{' Je ve zkušební době.' if self.zkusebni_doba else ''}"

# Založíme jednoho zaměstnance
z1 = Zamestnanec('Karel', 'dělník', False)
print(z1)

# Založíme druhého zaměstnance
# Zde ukázka, že argumenty můžeme zadávat i v libovolném pořadí, pokud napíšeme jejich název
# ... náhodné pořadí asi není moc užitečné, ale pojmenovávat argumenty ano (v případě jejich většího počtu zvyšuje přehlednost)
z2 = Zamestnanec(pozice='brigádník', jmeno='Josef', zkusebni_doba=True)
print(z2)