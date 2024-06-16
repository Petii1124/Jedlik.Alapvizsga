#megszamolja, egy bizonyos feltetelnek megfelelo elemek darabszamat a listaban

from random import randint

szamok=[]

elemszam=randint(10,40)

for i in range(elemszam):
    szamok.append(randint(-100,100))

print(szamok)
#megszamlalas tetele

#hany darab paros szam van a listaban?
db=0

for szam in szamok:
    if szam%2==0:  # ha paros a szam
        db+=1

print(f'A listaban {db} paros szam van.')



#hany darab negativ szam van a listaban?
db=0

for szam in szamok:
    if szam<0:  # ha paros a szam
        db+=1

print(f'A listaban {db} negativ szam van.')