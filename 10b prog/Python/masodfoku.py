#kerjuk be egy masodfoku egyenlet egyutthatoit (a,b,c).
#irjuk ki a gyokeit a valos szamok halmazan.

from math import sqrt #negyzetgyok

a=float(input('a='))
b=float(input('b='))
c=float(input('c='))

d=b**2-4*a*c #diszkrimináns

if d>=0:
    x1=(-b+sqrt(d))/(2*a)
    x2=(-b-sqrt(d))/(2*a)
    print(f'x1={x1}')
    print(f'x2={x2}')
else:
    print('Nincs megoldas a valos szamok halmazan!')