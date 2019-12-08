class Dostawca:
    def __init__(self, nazwa, adres, min_zam):
        self.nazwa = nazwa
        self.adres = adres
        self.min_zam = min_zam


class Menu:
    def __init__(self, dostawca, menu, produkt, cena):
        self.menu = menu
        self.produkt = produkt
        self.cena = cena