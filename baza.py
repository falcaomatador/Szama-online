from dostawca import Dostawca
from dostawca import Menu


produkty = ['pizza', 'kanapka']
ceny = [5, 10]


def utworz_produkty():
    prod = []
    for i in range(len(produkty)):
        prod.append(Menu(i+1, produkty[i], ceny[i]))
    return prod

dostawca_nazwy = ['kfc', 'mcd']
dostawca_min = [50, 10]

def utworz_dostawcow():
    dost = []
    for i in range(len(dostawca_nazwy)):
        dost.append(Dostawca(i+1, dostawca_nazwy[i], dostawca_min[i]))
    return dost









