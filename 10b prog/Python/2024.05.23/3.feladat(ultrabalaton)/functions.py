from data import *

eredmeny:list[Versenyzo]=[]

def beolvasas(filenev:str):
    f=open(filenev, 'r', encoding='utf8')
    f.readline()
    for sor in f:
        eredmeny.append(Versenyzo(sor.strip()))
    f.close()

def versenyzok_szama():
    szama=len(eredmeny)
    return szama

def noi_sportolo():
    noi=0
    for v in eredmeny:
        if v.kategoria=='Noi' and v.teljesitett_tav==100:
            noi+=1
    return noi

def leghosszabb_nev():
    leghosszabb=eredmeny[0]
    for e in eredmeny:
        if len(e.neve)> len(leghosszabb.neve):
            e==leghosszabb
    return leghosszabb