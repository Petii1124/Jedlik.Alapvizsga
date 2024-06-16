from versenyzo import versenyzo

versenyzok:list[versenyzo]=[]

versenyzok.append(versenyzo('Kis Jancsi',7.56,8.12,6.45))
versenyzok.append(versenyzo('Nagy Tamás',6.66,7.12,6.89))
versenyzok.append(versenyzo('Horváth Laci',8.01,8.87,7.32))
versenyzok.append(versenyzo('Németh Gábor',9.07,6.74,8.45))

print('      Név         1.     2.     3.   legnagyobb')
print('________________________________________________')

for v in versenyzok:
    print(f'{v.nev.ljust(15)}| {v.elso} | {v.masodik} | {v.harmadik} | +{v.legnagyobb_ugras()}')
    print('________________________________________________')

#hany olyan versenyzo van aki 6.5 felett van minden ugrasa
    
hatesfel_felett=0
for v in versenyzok:
    if v.elso>6.5 and v.masodik>6.5 and v.harmadik>6.5:
        hatesfel_felett+=1
print(f'\n{hatesfel_felett} versenyzonek van mind a harom ugrasa 6.5m felett!')

# ki nyerte a versenyt es mekkora ugrassal?

gyoztes_indexe=0
for i in range(1,len(versenyzok)):
    if versenyzok[i].legnagyobb_ugras()>versenyzok[gyoztes_indexe].legnagyobb_ugras():
        gyoztes_indexe=i

print(f'Győztes: {versenyzok[gyoztes_indexe].nev} ({versenyzok[gyoztes_indexe].legnagyobb_ugras()}m)')

#keresett versenyzo legnagyobb ugrasa.

keresett_nev=input(str('Adja meg a nevét: '))

for v in versenyzok:
    if keresett_nev.upper()==v.nev.upper():
        print(f'{keresett_nev} legnagyobb ugrása: {v.legnagyobb_ugras()}m')
        break
else:   
    print('A keresett személy nem indult!')