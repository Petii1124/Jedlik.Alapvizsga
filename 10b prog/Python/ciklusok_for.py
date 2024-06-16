# novekményes ciklus - for

for i in range(10):
    print('VAC ban')
print('Ez már nincs benne a ciklusban!')
    #létrehoz egy i változót
    #10 --> 0-9-ig vesz fel értékeket   # range(0,10)
    #alsó határ (0) benne van   #felső határ (10) már nincs benne!!!

for i in range(10,20):
    print(i)
     #10-19 vesz fel értéket

for i in range(100,201,2):
    #100-200-if kettesével megyünk a ciklusváltozón
    print(i,end=' ')

print() #csak azért, hogy a következő feladat új sorba kerüljön
for i in range(200,180):
    print(i,end=' ')

for i in range(2200,2180,2):
    print(i)
    #range üres tartományt ad --> a ciklus magja (a ciklusban lévő utasítás(ok)) egyszer sem fut le

# KÉSŐBB: for ciklus a lista vagy fájl elemein/sorain is végig tud menni
