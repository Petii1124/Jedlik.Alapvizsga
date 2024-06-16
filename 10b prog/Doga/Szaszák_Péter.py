# NÉV: Szaszák Péter

# 1. Feladat
# Kérjen be a felhasználótól 2 számot (a,b)!
# A második számot úgy kérje be, amíg mindenképpen
# legyen legalább 100-zal nagyobb az első számnál. (ellenőrzés)
# Generáljon ezen az intervallumon 10 db egész számot! (a-b)
# Számolja meg és írja ki, hogy a generált számok között 
# hány darab olyan szám van, amely 7-tel osztható.
#----------------------------------------------------------

from random import randint

a=int(input("Írja be az első számot!: "))

while b>= a+100:
    b=int(input("Írja be a második számot, ami legalább 100-zal nagyobb az elsőnél!: "))

    print("Legalább 100-zal legyen nagyobb a második szám!")

#2. feladat

# Kérje be 3 felhasználó nevét és életkorát.
# Az életkort addig kérje, amíg nem megfelelő értéket kap. (18-99) (ellenőrzés)
# Határozza meg, hogy ki a legidősebb!

legidosebb=''
legidosebb_kora=0


for i in range(3):
    kor=-1
    nev=input("Név: ")
    while kor<18 or kor>99:
        kor=int(input("Kora: "))
    if kor>legidosebb_kora:
        legidosebb_kora=kor
        legidosebb=nev
print(f'{legidosebb} a legidosebb {legidosebb_kora} éves')
