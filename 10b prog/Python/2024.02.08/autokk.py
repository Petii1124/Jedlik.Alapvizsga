from auto import auto

autok:list[auto]=[]

def auto_betolt(fajlnev:str):
    file=open(fajlnev,'r',encoding='UTF8')
    for sor in file:
        autok.append(auto(sor.strip()))
    file.close()    

def kiiras(autolitsa:list[auto]):
    for a in autolitsa:
        print(f'{a.rendszam.ljust(10)} {a.marka.ljust(10)} {a.tipus.ljust(10)} {str(a.teljesitmeny)}le {a.szin.ljust(10)}')

def szin_listazas(szin:str)->list[auto]:
    autok_uj=[]
    for a in autok:
        if a.szin.upper()==szin.upper():
            autok_uj.append(a)
    return autok_uj

def auto_hozzaad(fajlnev:str):
    print('Adja meg az új autó adatait!\n')
    rendszam=input('Rendszám: ')
    marka=input('Márka: ')
    tipus=input('Tipus: ')
    teljesitmeny=input('Teljesitmeny: ')
    szin=input('Szin: ')
    #eltaroljuk a memoriaban
    uj_auto=auto(rendszam+';'+marka+';'+tipus+';'+teljesitmeny+';'+szin)
    autok.append(uj_auto)

    file=open(fajlnev,'a',encoding='UTF8')
    file.write(rendszam+';'+marka+';'+tipus+';'+teljesitmeny+';'+szin)

def legerosebb_auto()->auto:
    legerosebb=autok[0]
    for a in autok[1:]:
        if a.teljesitmeny>legerosebb.teljesitmeny:
            legerosebb=a
    return legerosebb
