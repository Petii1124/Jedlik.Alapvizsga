#egy szam osztoinak meghatarozasa
#kerjunk be egy szamot és irjuk ki az osztoit egymas melle szokozzel
#pl. 15 osztoi: 1 3 5 15

szam=int(input('Szam: '))
print(f'{szam} osztoi:',end='')
for i in range(1,szam+1):
    if szam%i==0:
        print(i,end=' ')





#szam=int(input('Szam: '))
#print(f'{szam} osztoi:',end='')
#for i in range(1,int(szam/2)+1):
#    if szam%i==0:
#        print(i,end=' ')