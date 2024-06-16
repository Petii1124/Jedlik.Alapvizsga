# a lista legkisebb vagy legnagyobb elemet adja vissza
from random import randint

szamok=[]

elemszam=randint(10,40)

for i in range(elemszam):
    szamok.append(randint(-100,100))
print(szamok)

#maximum kivalsztas tetele:

#melyik a legnagyobb  szam?
# print(max(szamok)) # csak szamos listaknal min es max

legnagyobb=szamok[0]#ha talalunk nagyobbat, akkor majd atirjuk

for i in range(1,len(szamok)):
    if szamok[i]>legnagyobb:
        legnagyobb=szamok[i]
print(f'Legnagyobb elem: {legnagyobb}')

#hanyadik a legnagyobb szam a listaban?

legnagyobb_indexe=0
for i in range(1,len(szamok)):
    if szamok[i]>szamok[legnagyobb_indexe]:
        legnagyobb_indexe=i
print(f'A legnagyobb szam a(z) {szamok[legnagyobb_indexe]}, a sorszama {legnagyobb_indexe+1}')

# hanyadik a legnagyobb paratlan szam?

legnagyobb_indexe=len(szamok)#olyan elem amit biztos, hogy felulirunk
for i in range(len(szamok)):
    if szamok[i]%2==1: # ha paratlan
        if legnagyobb_indexe==len(szamok) or szamok[i]>szamok[legnagyobb_indexe]:
            legnagyobb_indexe=i
print(f'A legnagyobb paratlan szam: {szamok[legnagyobb_indexe]}')