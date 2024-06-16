import random   #véletlen szám generálásához szükséges

for i in range(20): #20 db szám
    print(random.randint(1,10),end=' ') #generál 1 db 1-10 közötti (határokat beleértve) egész számot majd kiírjuk

x=random.random()   #valós szám DE 0<=x<1
print(f'\n{x}')

y=random.randrange(0,101,2) #random páros szám 0-100 között
print(y)