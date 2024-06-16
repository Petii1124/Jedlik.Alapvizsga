#kerjuk be ket pont kordinatait
#mondjuk meg a ket pont tavolsagat
# p1(5,3) - p1(x1,y1)
# p2(-3,1) - p2(x2,y2)

from math import sqrt

x1=int(input('Az elso pont x kordinataja: '))
y1=int(input('Az elso pont y kordinataja: '))
x2=int(input('Az masodik pont x kordinataja: '))
y2=int(input('Az masodik pont y kordinataja: '))

tavolsag=sqrt((x1-x2)**2+(y1-y2)**2)

print(f'A ket pont tavolsaga: {tavolsag}')