class Dostawca:
    def __init__(self, nazwa, adres, min_zam):
        self.nazwa = nazwa
        self.adres = adres
        self.min_zam = min_zam


class Menu(Dostawca):
    def __init__(self, menu, produkt, cena):
        super().__init__(menu, produkt, cena)