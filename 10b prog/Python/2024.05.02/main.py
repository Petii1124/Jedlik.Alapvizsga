from functions import *

beolvasas('Eredmenyek.txt')

print(f'2. feladat: A versenyt {versenyzok_szama()} versenyző fejezte be.')
print(f'3. feladat: Versenyzők száma az "elit junior" kategóriában: {kategoria_letszam("elit junior")} fő')
print(f'4. feladat: Átlagéletkor: {atlag_eletkor(2014):.1f} év.')
bekert_kategoria=input('5. feladat: Kérek egy kategóriát: ')
if len(kategoria_rajtszamok(bekert_kategoria))==0:
    print(f'\tRajtszám(ok): Nincs ilyen kategória!')
else:
    print('\tRajtszámok:', end='')
    for rajtszam in kategoria_rajtszamok(bekert_kategoria):
        print(rajtszam, end='')