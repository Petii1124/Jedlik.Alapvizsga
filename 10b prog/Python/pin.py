#generaljunk egy negyjegyu PIN kodot
#kerjuk be a felhasznalotol
#max 3 probalkozas a hibas probalkozas utan 
# irjuk ki hogy még hany eselye van, ha elfogyott akkor irjuk ki hogy "Zarolas!"
# ha a PIN helyett egy mesterkodot adott meg (123456), akkor kiirjuk a PIN-t

from random import randint

#v1:
#generalunk egy 4 jegyu szamot, problema hogy nem kezdodhet 0-val
#pin=randint(1000,9999)

#v2:
#pin=''# a pin string tipusu
# for i in range(4):
#     szamjegy=randint(0,9)
#     pin+=str(szamjegy) # string tipusuva alakitottuk
# print(pin)

#v3:
pin=str(randint(0,9999))
#jo_pin=pin.zfill(4) #balrol vezeto 0-val tolti fel megadott hosszra
jo_pin=pin.rjust(4,'0') # balrol tolti fel megadott hosszara megadott karakterrel van ljust ami a masik iranybol

#print(jo_pin)

mestrerkod='123456'
megadott_pin=''
probalkozasok_szama=3 #max mennyi 

while jo_pin!=megadott_pin and probalkozasok_szama>0:
    megadott_pin=input('Adja meg a PIN kodjat: ')
    probalkozasok_szama-=1
    if megadott_pin==mestrerkod:
        
        #v1
        #print(f'Mesterkodot adott meg. PIN: {jo_pin}')
    
        #v2
        print(f'Mesterkodot adott meg!')
        uj_pin=input('Adja meg az uj PIN kodjat: ')    
        uj_pin2=input('Adja meg az uj PIN kodjat megegyszer: ')
        if uj_pin==uj_pin2:
            jo_pin=uj_pin
            print('PIN kodjat sikeresen megvaltoztatta!')
            probalkozasok_szama=3
    elif jo_pin!=megadott_pin:
        print(f'Hibás PIN! {probalkozasok_szama} probalkozas maradt!')

if jo_pin==megadott_pin:
    print('Sikeres azonositas!')
else:
    print('Kartyajat zaroltuk!')
