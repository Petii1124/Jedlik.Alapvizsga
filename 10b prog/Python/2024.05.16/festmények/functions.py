from data import *

festmenyek:list[festmeny]=[]

def beolvasas(filenev:str):
    f=open(filenev, 'r', encoding='utf8')
    f.readline()
    for sor in f:
        festmenyek.append(festmeny(sor.strip()))
    f.close()

def festmenyek_szama():
    osszeg=len(festmenyek)
    return osszeg

def darab_kereses(festo:str):
    db=0
    for festmeny in festmenyek:
        if festo==festmeny.festo:
            db+=1
    return db

def legdragabb_kep()->festmeny:
    legdragabb=festmenyek[0]
    for festmeny in festmenyek[1:]:
        if festmeny.becsult_ertek>legdragabb.becsult_ertek:
            legdragabb=festmeny
    return legdragabb
    
def nagyobb_e():
    for festmeny in festmenyek:
        if festmeny.becsult_ertek>festmeny.eredeti_ar:
            return True
        else:
            return False