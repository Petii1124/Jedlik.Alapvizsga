def tokeletes_szamok(szam:int):
    osszeg=0
    for oszto in range(1,szam//2+1):
        if szam%oszto==0:
            osszeg+=oszto
    return osszeg==szam

print('2. feladat: Tökéletes számok\nKérek két természetes számot:')
tol=int(input('tól = '))
ig=int(input('ig = '))
print(f'Tökéletes számok {tol} és {ig} között:')

db=0
for i in range(tol,ig):
    if tokeletes_szamok(i):
        if db>0:
            print('; ',end='')
        print(i,end='')
        db+=1
   
if db==0:
    print('A megadott tartományban nincsen tökéletes szám!')    