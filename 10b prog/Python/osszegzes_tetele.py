#egy lista bizonyos feltetelenek megfelelo elemet adja ossze
from random import randint

szamok=[]

elemszam=randint(10,40)

for i in range(elemszam):
    szamok.append(randint(-100,100))
print(szamok)

#osszegzes tetele

#mennyi a pozitiv szamok osszege?

osszeg=0
for szam in szamok:
    if szam>0:
        osszeg+=szam
print(f'A pozitiv szamok osszege: {osszeg}')

#mennyi a paros szamok atlaga?

osszeg=0
db=0
for szam in szamok:
    if szam%2==0:
        db+=1
        osszeg+=szam

if db>0:
    print(f'A paros szamok atlaga: {osszeg/db}')
else:
    print(f'Nincs a feltetelnek megfelelo elem.')