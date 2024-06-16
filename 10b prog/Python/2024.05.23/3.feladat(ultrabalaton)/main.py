from functions import *

beolvasas('ub2017egyeni.txt')

print(f'3.2 feladat: Futók száma: {versenyzok_szama()}')
print(f'3.3 feladat: Célba érkező női sportolók: {noi_sportolo()} fő')

leghosszabb=leghosszabb_nev()
print(f'3.4 feladat: A leghosszabb nevű futó\nNév: {leghosszabb.neve}\nRajtszám: {leghosszabb.rajtszam}\nEredmény: {leghosszabb.ido}')