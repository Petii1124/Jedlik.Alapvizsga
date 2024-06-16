from functions import *

beolvasas('helsinki.txt')

print(f'3. feladat:\nPomtszerző helyezések száma: {len(eredmenyek)} ')

print('\n4. feladat: ')
print(f'Arany: {helyezesek_szama(1)}')
print(f'Ezust: {helyezesek_szama(2)}')
print(f'Bronz: {helyezesek_szama(3)}')
print(f'Osszesen: {helyezesek_szama(1)+helyezesek_szama(2)+helyezesek_szama(3)}')

print(f'\n5. feladat:\nOlimpiai pontok szama: {osszpont()}')

print('\n6. feladat: ')
torna=sportag_ermek('torna')
uszas=sportag_ermek('uszas')
if uszas>torna:
    print('Uszas sportagban szereztek tobb ermet')
elif uszas<torna:
    print('Torna spotagban szereztek tobb ermet')
else:
    print('Egyenlő volt az ermek szama')

file_iras('helsinki2.txt')

legtobb=max_letszam()
print('\n8. feladat: ')
print(f'Helyezes: {legtobb.helyezes}')
print(f'Spotag: {legtobb.sportag}')
print(f'Versenyszam: {legtobb.versenyszam}')
print(f'Sportolok szama: {legtobb.letszam}')