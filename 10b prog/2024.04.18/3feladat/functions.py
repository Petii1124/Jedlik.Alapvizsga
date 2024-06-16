from data import *

cbAdasok:list[CBadás]=[]

def beolvas(filenev:str):
    f=open(filenev,'r',encoding='UTF8')
    f.readline()
    for sor in f:
        cbAdasok.append(CBadás(sor.strip()))
    f.close()

def bejegyzesek_szama():
    return len(cbAdasok)

def nev_bejegyzes(nev:str):
    db=0
    for adas in cbAdasok:
        if adas.nev==nev:
            db+=1
    return db

def maxAdasDB():
    max=0
    for adas in cbAdasok:
        if adas.darab>max:
            max=adas.darab
    return max
    
def filebairas(filenev:str):
    f=open(filenev,'w',encoding='UTF8')
    f.write('Kezdes;Nev;AdasDb\n')
    for adas in cbAdasok:
        f.write(f'{adas.ora*60+adas.perc};Aó{adas.nev};{adas.darab}\n')
    f.close()