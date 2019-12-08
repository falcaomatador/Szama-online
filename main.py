# import dostawca
from baza import utworz_produkty
from baza import utworz_dostawcow


def menu_dostawcy(dostawca):
    print(f'Witamy w')
    print('Nasze menu:')
    prod = utworz_produkty()
    for i, p in enumerate(prod):
        print(i+1, p)


def dostawcy_wszyscy():
    dostawcy = utworz_dostawcow()
    for i, dostawca in enumerate(dostawcy):
        print(i+1, dostawca)


def main():
    baza_dostawcow = {}
    print('Witaj w sklepie z jedzeniem! Wybierz swojego dostawcę:')
    dostawcy_wszyscy()
    dost = int(input('Numer dostawcy: '))

    menu_dostawcy(dost)






if __name__ == '__main__':
    main()
