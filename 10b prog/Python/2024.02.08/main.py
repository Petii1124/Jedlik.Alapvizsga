from autokk import *
from os import *

auto_betolt('autok.txt')

while True:
    system('cls') #kepernyo torlese
    print('0- kilépés')
    print('1- Új autó adatai')
    print('2- Adatok listázása')
    print('3- Legerősebb')
    print('4- Adott színű autók listázása')
    valasztas=input('Választása: ')

    match valasztas:
        case '0':
            print('Köszi, hogy itt voltál')
            break
        case '1':
            system('cls')
            print('Új autó adatainak megadása\n')
            auto_hozzaad('autok.txt')
            input('Vissza...')
        case '2':
            system('cls')
            print('Nyilvántartásban lévő autók\n')
            kiiras(autok)
            input('Vissza...')
        case '3':
            system('cls')
            print('Legerősebb autó\n')
            legerosebb=legerosebb_auto()
            print(f'Rendszám: {legerosebb.rendszam}')
            print(f'Tipus: {legerosebb.tipus}')
            print(f'Marka: {legerosebb.marka}')
            print(f'Teljesitmeny: {legerosebb.teljesitmeny}le')
            print(f'szin: {legerosebb.szin}')
            input('Vissza...')
        case '4':
            system('cls')
            print('Adott szinű autók\n')
            szin=input('Milyen színű autót keres?: ')
            print(f'\n{szin} szinű autók: \n')
            kiiras(szin_listazas(szin))
            input('Vissza...')