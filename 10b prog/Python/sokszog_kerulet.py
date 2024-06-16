#kerjuk be egy sokszog oldalai szamat
#kerjuk be egymas utan az oldalak hosszat
#irjuk ki a keruletet

oldalak_szama=int(input('Adja meg az oldalak szamat!: 1'))
kerulet=0

for i in range(oldalak_szama):
        oldal_hossza=int(input('Oldal hossza!: '))
        kerulet+=oldal_hossza

print(f'Kerület: {kerulet}')