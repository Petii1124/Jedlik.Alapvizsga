from functions import *

versenyzok_szama()
print(f'{min8600()} ember ért el 8600 pontot.')
print(f'A versenyzok altal elért pontok átlaga: {pontok_atlaga()}')

print(f'A verseny gyoztese: {versenyzok[nyertes()]} {pontok[nyertes()]} pontos erdemennyel.')

nev=input('Versenyzo neve: ')
if versenyzo_pont(nev)!=False:
    print(f'\t A versenyzo pontszama: {versenyzo_pont(nev)}')
else:
    print('\t A versenyzo nem indult!')