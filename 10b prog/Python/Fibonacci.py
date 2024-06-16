# 0 1 1 2 3 5 8 13 21
#0. eleme a 0
#1. eleme az 1
# tovabbi elemeket az elozo 2 elem osszege
#aktualis elem= elozo+ elozo elotti
#Kérjuk be ,hogy hány elem legyen benne(n), és írjuk ki az első n elemet!

n=int(input('Hany elemu legyen?: '))

elozo_elotti=0
elozo=1

if n>=2:
    print('0 1 ',end=' ')
elif n==1:
    print('0')

for i in range(n-2): #mert feljebb kiirtuk az elso kettot
    aktualis=elozo_elotti+elozo
    print(aktualis,end=' ')
    elozo_elotti=elozo
    elozo=aktualis