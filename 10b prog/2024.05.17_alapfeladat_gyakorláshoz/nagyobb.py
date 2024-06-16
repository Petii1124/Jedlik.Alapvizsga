elso_szam=int(input('Adj meg egy számot! '))
masodik_szam=int(input('Adj meg egy másik számot! '))

if elso_szam>masodik_szam:
    print(f'A nagyobb érték {elso_szam}')     
elif masodik_szam>elso_szam:
    print(f'A nagyobb érték {masodik_szam}')  
else:
    print('A két szám egyenlő') 