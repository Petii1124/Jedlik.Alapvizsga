from data import *

eredmenyek:list[eredmeny]=[]

def beolvasas(filenev):
    f=open(filenev,'r',encoding='UTF8')
    for sor in f:
        eredmenyek.append(eredmeny(sor))
    f.close()

def helyezesek_szama(helyezes)->int:
    db=0
    for e in eredmenyek:
        if e.helyezes==helyezes:
            db+=1
    return db

def osszpont()->int:
    osszeg=0
    for e in eredmenyek:
        osszeg+=e.pont()
    return osszeg

def sportag_ermek(sportag)->int:
    db=0
    for e in eredmenyek:
        if e.sportag==sportag and e.helyezes<=3:
            db+=1
    return db

def file_iras(filenev):
    f=open(filenev,'w',encoding='UTF8')
    for e in eredmenyek:
        if e.sportag=='kajakkenu':
            f.write(f'{e.helyezes} {e.letszam} {e.pont2()} kajak-kenu {e.versenyszam}\n')
        else:
            f.write(f'{e.helyezes} {e.letszam} {e.pont2()} {e.sportag} {e.versenyszam}\n')
    f.close()

def max_letszam()->eredmeny:
    legtobb=eredmeny[0]
    for e in eredmenyek[1:]:
        if e.letszam>legtobb.letszam:
            legtobb=e
    return legtobb