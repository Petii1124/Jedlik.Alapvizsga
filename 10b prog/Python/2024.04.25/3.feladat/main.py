from functions import *

beolvas('legmagasabb.txt')

print(f'3.2 feladat: Épületek száma: {epuletek_szama()} db')

print(f'3.3 feladat: Emeletek összege: {emeletek_osszege()}')

print('3.4 feladat: A legnagyobb épület adatai')

legamagasabb_e=legamagasabb()

print(f'\tNév: {legamagasabb_e.nev}')
print(f'\tVáros: {legamagasabb_e.varos}')
print(f'\tOrszág: {legamagasabb_e.orszag}')
print(f'\tMagasság: {legamagasabb_e.magassag} m')
print(f'\tEmeletek száma: {legamagasabb_e.emeletek}')
print(f'\tÉpítés éve: {legamagasabb_e.epult}')

if orszag_epulet('Olaszország'):
    print(f'3.5 feladat: Van olasz épület az adatok között!')
else: 
    print(f'3.5 feladat: Nincs olasz épület az adatok között!')