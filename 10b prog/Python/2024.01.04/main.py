from korcsolya import *

for i in range(10):
    print(f'{i+1}. versenyzo pontszama: ',end='')
    pontok=versenyzo_pontjai()
    osszpontszam=sum(pontok) #pontok osszege
    print(*pontok)
    print(f'\tKiesik: {min(pontok)} és {max(pontok)}')
    osszpontszam-=max(pontok)-min(pontok)
    versenyzok_osszpont.append(osszpontszam)
    print(f'\tAtlag pontszam: {osszpontszam/5}')
    
print(f'Nyertes a  {gyoztes_sorszam()}. versenyzo')