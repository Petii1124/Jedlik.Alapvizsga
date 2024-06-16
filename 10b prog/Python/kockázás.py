#3 dobokockaval dobunk, összeedjuk az ertekeket, ha az osszeg kisebb mint 10, akkor Anni nyert? kulonben Panni
#szimulaljuk le
# Kerjuk be, hogy hanyszor dobjunk?, majd mondjunk meg, hogy ki hanyszor nyert

from random import randint

anni_nyert=0

feldobasok_szama=int(input('Hany feldobas legyen?: '))

for i in range(feldobasok_szama):
    dobas1=randint(1,6)
    dobas2=randint(1,6)
    dobas3=randint(1,6)
    osszeg=dobas1+dobas2+dobas3
    if osszeg<10:
        print('Anni nyert!')
        anni_nyert+=1
    else:
        print('Panni nyert!')

print(f'A jatek soran {anni_nyert} alkalommal Anni, {feldobasok_szama-anni_nyert} alkalommal Panni nyert! ')
