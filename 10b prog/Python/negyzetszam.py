# kerjunk be egy szamot es mondjuk meg hogy negyzetszam-e

from math import sqrt

szam=int(input('Kerek egy szamot: '))
gyok=sqrt(szam)

if gyok==round(gyok):
    print('Negyzetszam!')
else:
    print('Nem negyzetszam!')