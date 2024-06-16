print('Abszolút érték\n')

szam=float(input('Szám= '))
#összehasonlító operátorok:
    # < - kisebb
    # <= - kisebb egyenlő
    # > - nagyobb
    # >= - nagyobb egyenlő
    # != - nem egyenlő

if szam>=0:
    print(f'A szám abszolút értéke: {szam}')    #mivel pozitív, így kiírjuk önmagát
else:
    #print(f'A szám abszolút értéke: {szam*-1}')
    print(f'A szám abszolút értéke: {-szam}')