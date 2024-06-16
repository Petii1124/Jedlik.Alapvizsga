#irjuk ki a 10*10-es szorzotablat

for i in range(1,11): #i=1,2,3,...
    for j in range(1,11):
        print(f'{i*j:3d}',end=' ') #:3d  3 decimalis helyen irjuk ki
    print() #soremeles
