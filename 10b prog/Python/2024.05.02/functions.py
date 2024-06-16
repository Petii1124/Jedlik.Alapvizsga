from data import *

versenyzok:list[versenyzo]=[]

def beolvasas(filenev:str):
    f=open(filenev, 'r', encoding='utf8')
    for sor in f:
        versenyzok.append(versenyzo(sor.strip()))
    f.close()

def versenyzok_szama():
    return len(versenyzok)

def kategoria_letszam(kategoria:str):
    letszam=0
    for versenyzo in versenyzok:
        if versenyzo.kategoria==kategoria:
            letszam+=1
    return letszam

def atlag_eletkor(ev:int)->float:
    osszeg=0
    for v in versenyzok:
        eletkor=ev-v.szul_ev
        osszeg+=eletkor
        atlag=osszeg/len(versenyzok)
    return atlag

def kategoria_rajtszamok(kategoria:str):
    kategoria_lista=[]
    for versenyzo in versenyzok:
        if versenyzo.kategoria==kategoria:
            kategoria_lista.append(versenyzo.rajtszam)
    return kategoria_lista