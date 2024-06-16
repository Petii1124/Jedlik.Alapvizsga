from tanulo import *
from random import randint,choice

tanulok:list[tanulo]=[] 
vezeteknevek = ['Kiss', 'Kovács', 'Szabó', 'Horváth', 'Fazekas', 'Török', 'Magyar']
keresztnevek = ['Márk', 'Bálint', 'Eszter', 'Judit', 'Elemér', 'Péter', 'Pál', 'Miksa', 'Töhötöm']

def uj_tanulo()->tanulo:
    vezeteknev=choice(vezeteknevek)
    keresztnev=choice(keresztnevek)
    szuletesi_ev=randint(2003,2010)
    szuletesi_ho=randint(1,12)
    szuletesi_nap=randint(1,28) # ne kelljen vizsgalni a honapot

    szuletesi_datum=datetime(szuletesi_ev, szuletesi_ho, szuletesi_nap)

    jegyek=[]
    for i in range(randint(0,5)):
        jegyek.append(randint(1,5))
    return tanulo(vezeteknev, keresztnev, szuletesi_datum, jegyek)

def tanulok_feltolt(letszam:int)-> None:
    for i in range(letszam):
        tanulok.append(uj_tanulo())

def tanulo_kiir()->None:
    for t in tanulok:
        print(f'{t.vezeteknev} {t.keresztnev} ({t.szuletes.strftime("%Y.%m.%d.")})')
        print('\tJegyei:', *t.jegyek)
        print(f'\tÁtlaga: {t.atlag():.2f}')

def o_atlag()->float:
    osszeg=0
    db=0
    for t in tanulok:
        if t.atlag()>0:
            osszeg+=t.atlag()
            db+=1
    return osszeg/db

def atlag_felett()->int:
    db=0
    for t in tanulok:
        if t.atlag()>o_atlag():
            db+=1
    return db

def legjobb()->tanulo:
    legjobb=tanulok[0]
    for t in tanulok:
        if t.atlag()>legjobb.atlag():
            legjobb==t
    return legjobb