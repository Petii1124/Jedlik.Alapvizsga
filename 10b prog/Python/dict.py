szotar={'alma':'apple','szék':'chair','ajtó':'door','kék':'blue'}

print(szotar) #teljes szotar
print(szotar['kék'])

for s in szotar.keys():
    print(s)

for s in szotar.values():
    print(s)

for s in szotar.items():
    print(s)

#hozzaadas
szotar['piros']='red' #szogletesben a key = utan a value

#elem felulirasa
szotar['kék']='navy blue'

for key,value in szotar.items():
    print(f'{key.ljust(6)}- {value}')

#print(szotar['barna']) #keyError nincs ilyen a szotarban


#kereses
keresett=input('\nKeresett szó: ')
if keresett in szotar.keys():
    print(f'{keresett} - {szotar[keresett]}')
else: 
    print(f'A "{keresett}" nincs benne!')
    if input('Szeretné felvenni? (i/n): ')=='igen' or 'i':
        jelentes=input('Jelentese: ')
        szotar[keresett]=jelentes

print(szotar)