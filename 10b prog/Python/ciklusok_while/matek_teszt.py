#keszitsunk programot, amely ki fodja kerdezni a metekot.
# 2 szam kulonbsege/osszege/szorzata
# A program akkor fejezodik be, ha a felhasznalo 5 feladatot kiszamol helyesen.
# Rossz válasz esetén ujrakerdezzuk ugyanazt
# vegen kiirjuk az eredmenyesseget szazalékban

from random import randint

kerdesek_szama=5 #csak it kell atirni

rossz_valaszok_szama=0

for i in range(kerdesek_szama): 
    szam1=randint(1,10)
    szam2=randint(1,10)
    muvelet=randint(0,2) # 0='+' 1='-' 2='*'
    helyes_valasz=False #kezdoertek a while ciklusban
    while helyes_valasz==False: 
         match muvelet:
            case 0: # +
                valasz=int(input(f'{szam1}+{szam2}='))
                if valasz==szam1+szam2:
                    print('JO valasz!')
                    helyes_valasz=True
                else:
                    print('Rossz valasz!')
                    rossz_valaszok_szama+=1
            case 1: # -
                valasz=int(input(f'{szam1}-{szam2}='))
                if valasz==szam1-szam2:
                    print('JO valasz!')
                    helyes_valasz=True
                else:
                    print('Rossz valasz!')
                    rossz_valaszok_szama+=1
            case 2: # *
                valasz=int(input(f'{szam1}*{szam2}='))
                if valasz==szam1*szam2:
                    print('JO valasz!')
                    helyes_valasz=True
                else:
                    print('Rossz valasz!')
                    rossz_valaszok_szama+=1
print(f'Eredmenyesseg: {kerdesek_szama/(kerdesek_szama+rossz_valaszok_szama)*100:.2f}%')

#kesobb: fuggveny hasznalata