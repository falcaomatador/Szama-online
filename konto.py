class Konto:
    def __init__(self, nazwa, haslo):
        self.nazwa = nazwa
        self.haslo = haslo
    def haslo_ok:
        pass


class Koszyk(Konto):
    def __init__(self):
        super().__init__(nazwa, haslo)
        self.lista_produktow = {}
    def __str__(self):
        return f"Twój koszyk: {self.lista_produktow}"
    def usun_zakupy(self):
        self.lista_produktow.clear()
    def oblicz_wartosc(self):
        suma = 0
        for produkt, ilosc in self.produkty.items():
            suma += produkt.cena * ilosc
        return f"Wartość zakupów wynosi {suma} zł."
    def dodaj(self, produkt):
        if produkt not in self.lista_produktow:
            self.lista_produktow[produkt] = 1
        else:
            self.lista_produktow[produkt] += 1

