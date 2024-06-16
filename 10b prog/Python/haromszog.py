import math #math osztály importálása a matematikai fgv-ek használatához

a_oldal=int(input('a= '))
b_oldal=int(input('b= '))
c_oldal=int(input('c= '))

#Logikai operátorok:
    #ÉS - and   - minden felvételnek teljesülnie kell
    #VAGY - or  - legalább 1 feltételnek teljesülnie kell
    #TAGADÁS - not

if ((a_oldal+b_oldal)>c_oldal) and ((a_oldal+c_oldal)>b_oldal) and ((b_oldal+c_oldal)>a_oldal):
    kerulet=a_oldal+b_oldal+c_oldal
    print(f'Kerület: {kerulet}')
    s=kerulet/2
    terulet=math.sqrt(s*(s-a_oldal)*(s-b_oldal)*(s-c_oldal))
    print=(f'Terület')
    print('Megszerkeszthető!')
else:
    print('Nem megszerkeszthető!')
