class Dostawca:
    def __init__(self, nazwa, adres, min_zam):
        self.nazwa = nazwa
        self.adres = adres
        self.min_zam = min_zam

class Menu:
    def __init__(self, dostawca, produkt, cena):
        self.produkt = produkt
        self.cena = cena
        self. dostawca = dostawca

class Produkt:
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena

        def __str__(self):
            return f'{self.nazwa}, {self.cena} zł'