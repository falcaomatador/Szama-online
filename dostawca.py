class Dostawca:
    def __init__(self, id, nazwa, min_zam):
        self.id = id
        self.nazwa = nazwa
        self.min_zam = min_zam

    def __str__(self):
        return self.nazwa


class Menu:
    def __init__(self, dostawca, produkt, cena):
        self.produkt = produkt
        self.cena = cena
        self. dostawca = dostawca

    def __str__(self):
        return f'{self.produkt}, {self.cena} zł'
