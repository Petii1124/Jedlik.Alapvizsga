#Kérjük be egy kúp alapjának sugarát és magasságát
#Írjuk ki a kúp felszínét és térfogatát

from math import sqrt,pow,pi
#sqrt - négyzetgyök
#pow - hatványozás
#pi - pi (kb.: 3,14)

r=float(input('Adja meg a kúp alapjának sugarát!: '))
h=float(input('Adja meg a kúp magasságát!: '))

a=sqrt(pow(r,2)+pow(h,2))   #alkotó - négyzetgyök(r négyzet+h négyzet)
#a=sqrt(r**2+h**2)

A=round(r**2*pi+r*pi*a) #alap területe+palást területe
                        #round(mit, hány tizedes pontossággal)

V=r**2*pi*h/3

print(f'Felszín: {A}')
print(f'Térfogat: {V:.2f}') #:.2f - 2 tizedes pontossággal írjuk ki!