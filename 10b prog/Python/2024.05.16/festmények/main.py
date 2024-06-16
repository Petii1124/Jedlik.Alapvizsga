from functions import *

beolvasas('paintings.txt')

print(f'3.3 feladat: A fájlban tárolt festmények száma: {festmenyek_szama()}')
print(f'3.4 feladat: A Pablo Picasso képek száma: {darab_kereses("Pablo Picasso")} darab.')
legdragabb=legdragabb_kep()
print(f'3.5 feladat: A legdrágább kép festője: {legdragabb.festo}, a kép címe: {legdragabb.festmeny}, becsült értéke: {legdragabb.becsult_ertek} dollár.')

if nagyobb_e():
    print(f'3.6 feladat: Van olyan fesmény, amelynek a becsült értéke nem haladja meg az eredeti árát.')
else:
    print(f'3.6 feladat: Nincs olyan fesmény, amelynek a becsült értéke nem haladja meg az eredeti árát.')