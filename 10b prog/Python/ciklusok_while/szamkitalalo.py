#generaljunk egy 1 és 100 koze eso szamot
#A jatekos talalja majd ki
#segitseg: tipp kisebb vagy nagyobb a keresett szam 

from random import randint
titkos_szam=randint(1,100)
# print(titkos_szam) #teszteles miatt

tipp=-1 # a jatekos tippje
tippek_szama=0 # kezdetben 0, majd noveljuk

while tipp!=titkos_szam: #addig megy amig el nem talalja
    tipp_txt=input('Tipp (1-100): ')
    tippek_szama+=1
    if tipp_txt.isnumeric(): #csak akkor vizsgaljuk meg, ha pozitiv egesz szam
        tipp=int(tipp_txt)
        if tipp>titkos_szam: #ha tul nagy a tipp
            print('Kisebb!!')
        elif tipp<titkos_szam: #ha a tipp tul kicsi
            print('Nagyobb!!')
print(f'Talált, {tippek_szama} tippre volt szukseg.')