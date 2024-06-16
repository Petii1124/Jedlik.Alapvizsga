#dobjunk 1 db dobokockaval valahanyszor
#mondjuk meg hany 6-os dobas volt
#melyikbol mennyi volt --> statisztika

from random import randint

n=20 #dobasok

egyesek_szama=0
kettesek_szama=0
harmasok_szama=0
negyesek_szama=0
otosok_szama=0
hatosok_szama=0

for i in range(n):
    dobas=randint(1,6)
    print(dobas,end=' ')
    #   if dobas==1:
    #       egyesek_szama+=1
    #   elif dobas==2:
    #        kettesek_szama+=1
    #    elif dobas==3:
    #       harmasok_szama+=1
    #   elif dobas==4:
    #       negyesek_szama+=1
    #   elif dobas==5:
    #       otosok_szama+=1
    #    else dobas==6:
    #        hatosok_szama+=1
    match dobas:
        case 1: egyesek_szama+=1
        case 2: kettesek_szama+=1
        case 3: harmasok_szama+=1
        case 4: negyesek_szama+=1
        case 5: otosok_szama+=1
        case 6: hatosok_szama+=1


print(f'\n\nEgyes dobasok szama: {egyesek_szama}')
print(f'Kettes dobasok szama: {kettesek_szama}')
print(f'Harmas dobasok szama: {harmasok_szama}')
print(f'Negyesek dobasok szama: {negyesek_szama}')
print(f'Otosok dobasok szama: {otosok_szama}')
print(f'Hatos dobasok szama: {hatosok_szama}')