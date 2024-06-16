from functions import *

print('3. feladat: CB-Rádió')
beolvas('cb.txt')

print(f'3.2 feladat: Bejegyzések száma: {bejegyzesek_szama()} db')

print(f'3.3 feladat: Sanyihoz tartozó bejegyzések: {nev_bejegyzes("Sanyi")} db')

print(f'3.4 feladat: A legtöbb adás:')
for adas in cbAdasok:
    if adas.darab==maxAdasDB():
        print(f'\tIdő: {adas.ora}:{adas.perc} Darab: {adas.darab} Név: {adas.nev}')

filebairas('cb2.txt')