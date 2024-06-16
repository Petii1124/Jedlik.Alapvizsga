#adott szám szamjegyeinek forditott sorrendben kiirasa(barmilyen string)

szam=input('Kerek egy szamot: ') #jelenleg string

print(szam) #kiirjuk
print('A szamjegyek szama:', len(szam)) # string hossza (karakterek szama)

forditva=''

for i in range(len(szam)-1,-1,-1):
    forditva+=szam[i]
print(f'A szám forditva: {forditva}')
