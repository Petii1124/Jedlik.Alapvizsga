from random import randint

ivott=False  #kezdes elott nem ivott
osszes=0

for i in range(1,31):
    if ivott==False: #ha elozo nam nem ivott
        mai_fozet=randint(1,5)
        osszes+=mai_fozet
        if randint(1,5)==5:
            ivott=True
            osszes-=1# megisszak
        print(f'{i}. nap:{mai_fozet} liter. Eddigi termes osszesen: {osszes} liter. ',end='')
        if ivott:
            print('Ma ivott Pista bacsi a haverokkal.',end='')
        print()# soremelesre hasznaljuk
    else: #ha elozo nao ivott
        print('Pista bacsi nem foz, mert masnapos!')
        ivott=False