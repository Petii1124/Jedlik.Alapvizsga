#kerjuk be egy szamtani sorozat elso elemet (a1), differenciajat (d)
# es eleminek szamat (n)
#irjuk ki a sorozat n db elemet vesszovel

a1=int(input('Kerem a sorozat elso elemet: '))
d=int(input('kerem a sorozat differenciajat: '))
n=int(input('Kerem a sorozat elemszamat: '))

#for i in range(n):
#   an=a1+i*d
#  print(an,end=',')   ha nem szamit hogy a vegen is vesszo

for i in range(n):
    an=a1+i*d
    if i==n-1:  #ha az utolso elem jon nincs vesszo
        print(an,end='')
    else:           #amig nem az utolso elem legyen vesszo
        print(an,end=',')