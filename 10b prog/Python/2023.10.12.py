# 1. Feladat
# Kérjen be a felhasználótól 3 számot (a,b,n)!
# A második számot addig kérje be, amíg mindenképpen
# legyen legalább 100-zal nagyobb az 'b' a 'a'-nél. (ellenőrzés)
# Generáljon ezen az intervallumon n db egész számot! (a-b)
# Számolja meg és írja ki, hogy a generált számok között 
# hány darab olyan szám van, amely négyzetszám.

from random import randint
from math import sqrt

db=0
a=int(input('Szam1: '))
b=True
while b<a+100:
    b=int(input('Szam2: '))
n=int(input('Hany darab?: '))

for i in range(n):
    generalt=randint(a,b)
    print(generalt,end=' ')
    gyok=sqrt(generalt)

    if gyok==round(gyok):
        db+=1
print(f'\n{db} darab negyzetszam van!')
#----------------------------------------------------------
#2. feladat

# Kérje be 3 felhasználó nevét és magasságát (cm), testsúlyát (kg).
# Az magasság és súly adatokat addig kérje be, 
# amíg nem megfelelő értéket kap. (100-220cm/40-200 kg) (ellenőrzés)
# Határozza meg, ki a legmagasabb, és ki a legnehezebb!

legmagasabb=''
legmagasabb_magassaga=0
legnehezebb=''
legnehezebb_sulya=0

for i in range(3):
    nev=input('Név: ')
    magassag=0
    while magassag<100 or magassag>220:
        magassag=int(input('Magassag: '))
    suly=0
    while suly<40 or suly>220:
        suly=int(input('Testsuly: '))
    if magassag>legmagasabb_magassaga:
        legmagasabb=nev
        legmagasabb_magassaga=magassag
    if suly>legnehezebb_sulya:
        legnehezebb=nev
        legnehezebb_sulya=suly
    
print(f'\nLegmagasabb: {legmagasabb}, {legmagasabb_magassaga} centivel és\nLegnehezebb: {legnehezebb}, {legnehezebb_sulya} kiloval!')