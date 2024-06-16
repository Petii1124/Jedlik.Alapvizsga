# eddif 4 adathoz 4 valtozo kellett
    #a=12
    #b=34
    #c=-1
    #d=2

# Lista kozos nev alatt, sorszammal indexelve tarol elemeket

lista=[] #ures lista

szamok=[11,24,66,78] 
szinek=['zold','kek','piros','sarga']

#lista eleminek elerese
print(szamok) #teljes lista
print(*szinek,sep=', ') #teljes lista osszes eleme

#lista elemszama:
print('Elemszam:',len(szamok))


#a lsita elemeit o-tol kezdve indexeljuk
    #az elso elem indexe a 0, az utolso elem indexe n-1
print(szamok[0]) # a lista elso eleme
print(szamok[-1]) # a lista utolso eleme
print("utolso v2:",szamok[len(szamok)-1]) # a lista utolso eleme

#a lista vegigjarasa, ha az index is kell:
for i in range(len(szinek)):
    print(f'{i+1}.{szinek[i]}')#egymas ala a szinek lista elemeit szamozva

#lista vegigjarasa, ha az index nem kell
for szin in szinek:
    print(szin,end=' ')

# a 3-mal oszthato elemek szama a listabol
db=0
for szam in szamok:
    if szam%3==0:
        db+=1
print(f'\n{db} db 3-mal sozthato van a listaban')

#random elemekkel feltoltott lista
from random import randint

ujszamok=[]
for i in range(10):
    ujszamok.append(randint(-100,100)) # append elem hozzaadasa a listahoz
print(*ujszamok)

#reszlista kiirasa:
#listaveve [tol:ig] tol-inclusive ig-exclusive
print(ujszamok[1:4]) #1-4ig reszlista de a 4-es indexu nincs benne
print(ujszamok[3: ])# 3. indexutol a vegeig
print(ujszamok[:4])# 4. indexuig de az nincs benne
print(ujszamok[-3: ])#az utolso 3 elem