from functions import *

beolvas('nobel.csv')

print(F'3. feladat: {tipus_nev_alapjan("Arthur B. McDonald")}')

print(f'4. feladat: ',end='')
if dijazott_ev_es_tipus_alapjan(2017,"irodalmi")==False:
    print('Hibás adat!')
else:
    print(f'{dijazott_ev_es_tipus_alapjan(2017,"irodalmi").teljesnev}')

print('5. feladat: ')
szervezetek_adott_ev_utan(1990,'béke')

print('6. feladat: ')
nev_kereses('Curie')

print('7. feladat: ')
statisztika()

print('8. feladat: orvosi.txt')
fileba_iras_tipus('orvosi')
print('\t    fizikai.txt')
fileba_iras_tipus('fizikai')