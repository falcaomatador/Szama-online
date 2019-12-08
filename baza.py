kurczaki = Dostawca("Kurczaki", "ul. Kurczacza 6, 00-666, Kurczaków", 50)
ziemniaki = Dostawca("Badyle ziemniaczane", "ul. Ziemniaczana 9, 00-292 Ziemniaków", 20)
buraki = Dostawca("Krwawy burak", "ul. Buraczana 3, 03-333 Buraków", 35)



class Menu:
    def __init__(self, dostawca, produkt, cena):
        self.dostawca = dostawca
        self.produkt = produkt
        self.cena = cena

nazwy_kurczaki = ['buffalo wings', 'bbq wings', 'full chicken bucket', 'onion rings', 'fries']
ceny_kurczaki = ['25', '25', '60', '15', '10']
produkty_kurczaki = []
for i in range(len(nazwy_kurczaki)):
    produkty_kurczaki.append(Menu('kurczaki', nazwy_kurczaki[i], ceny_kurczaki[i]))

nazwy_ziemniaki = ['belgijskie małe', 'belgijskie średnie', 'belgijskie duże', 'łódki', 'talarki']
ceny_ziemniaki = ['10', '15', '20', '17', '18']
produkty_ziemniaki = []
for i in range(len(nazwy_ziemniaki)):
    produkty_ziemniaki.append(Menu('kurczaki', nazwy_ziemniaki[i], ceny_ziemniaki[i]))


nazwy_buraki = ['sałatka buraczana', 'carpaccio z buraka', 'burger buraczany', 'sok z buraka', 'chipsy z buraka']
ceny_buraki = ['17', '23', '25', '12', '8']
produkty_buraki = []
for i in range(len(nazwy_buraki)):
    produkty_buraki.append(Menu('kurczaki', nazwy_buraki[i], ceny_buraki[i]))


