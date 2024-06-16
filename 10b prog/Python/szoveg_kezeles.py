mondat='Lorem ipsum dolor sit amet consectetur adipisicing elit. Pariatur numquam veritatis temporibus. Facilis nulla laborum quod voluptatibus quas molestiae dolorum iure nihil, ea voluptates, placeat voluptatum totam distinctio. Debitis, officiis?'

# milyen hosszu a mondat?

print(f'A mondat {len(mondat)} karakterbol all.')
print(f'A mondat {len(mondat.replace(" ",""))} karakterbol all szokoz nelkul.')

#szavak szama
db=0
for betu in mondat:
    if betu==" ":
        db+=1
print(f'A mondat {db+1} szobol all.')

#MASIK
szavak=mondat.split(' ')
print(f'A mondat {len(szavak)} szobol all.')

#hany olyan szo van ami legalabb 10 karakter

irasjelek='([{,.?!-_:;}]]'  #nem kivanatos karakterek torlese
for irasjel in irasjelek:
    mondat2=mondat.replace(irasjel,'')
szavak2=mondat2.split(' ')
db=0
for szo in szavak2:
    if len(szo)>=10:
        db+=1
print(f'A szovegben {db} db szo van, amely legalább 10 karakter hosszu.')

#kerjunk be egy karaktert , es mondjuk meg, hogy mennyi van belole
bekert_karakter=input('Karakter: ')
db=0
for betu in mondat:
    if betu==bekert_karakter:
        db+=1
print(f'A szovegben {db} db {bekert_karakter} karakter van.')

#melyik karakterbol mennyi van?
lehetseges_karakterek='qwertzuiopasdfghjklyxcvbnm'

karakterek_szama=[]
for lehetseges_karakterek in lehetseges_karakterek.upper():
    db=0
    for karakter in mondat:
        if karakter.upper()==lehetseges_karakterek:
            db+=1
    karakterek_szama.append(db)

print('Karekterek statisztika:')
for i in range(len(lehetseges_karakterek)):
    if karakterek_szama[i]>0:
        print(f'{lehetseges_karakterek[i]}:{karakterek_szama[i]}')
