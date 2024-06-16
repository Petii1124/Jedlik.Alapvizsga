from functions import *

feltolt(10,0,100)

kiir()

print(f'\nElemek osszege: {osszeg()}')

print(f'Elemek atlaga: {atlag():.2f}')

bekertszam=int(input('\nKerek egy szamot: '))
if keres(bekertszam):
    print('A keresett szam benne van a listaban')
else:
    print('A keresett szam nincs benne a listaban.')