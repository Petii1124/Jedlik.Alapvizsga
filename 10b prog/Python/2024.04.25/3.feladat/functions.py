from data import *

epuletek:list[Épület]=[]

def beolvas(filenev:str):
    f=open(filenev, 'r', encoding='utf8')
    f.readline()
    for sor in f:
        epuletek.append(Épület(sor.strip()))
    f.close()

def epuletek_szama():
    return len(epuletek)

def emeletek_osszege():
    osszeg=0
    for e in epuletek:
        osszeg += e.emeletek
    return osszeg

def legamagasabb():
    legnagyobb=epuletek[0]
    for e in epuletek:
        if e.magassag>legnagyobb.magassag:
            legnagyobb=e
    return legnagyobb

def orszag_epulet(orszag:str):
    for e in epuletek:
        if e.orszag==orszag:
            return True
        
    return False
