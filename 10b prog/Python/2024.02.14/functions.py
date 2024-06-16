from dijazott import *

dijazottak:list[dijazott]=[]

def beolvas(filenev):
    file=open(filenev, 'r', encoding='UTF8')
    file.readline()
    for sor in file:
        dijazottak.append(dijazott(sor.strip()))
    file.close()

def tipus_nev_alapjan(nev:str)->str:
    for d in dijazottak:
        if d.teljesnev.upper()==nev.upper():
            return d.tipus
    return "Nincs ilyen dijazott!!!"

def dijazott_ev_es_tipus_alapjan(ev:int,tipus:str)->dijazott|bool:
    for d in dijazottak:
        if d.ev==ev and d.tipus==tipus:
            return d
    return False     

def szervezetek_adott_ev_utan(ev:int,tipus:str):
    for d in dijazottak:
        if d.ev>=ev and d.tipus==tipus and d.vezeteknev=="":
            print(f'\t{d.ev}: {d.keresztnev}')

def nev_kereses(nev:str):
    for d in dijazottak:
        if nev.upper() in d.vezeteknev.upper():
            print(f'\t{d.ev}: {d.teljesnev}({d.tipus})')

def fileba_iras_tipus(tipus:str):
    dijazottak2=dijazottak.copy()
    dijazottak2.reverse()  #lista megforditasa
    file=open(tipus+'.txt','w',encoding='UTF8')
    file.write('Év:Dijazott\n')  #ha kell cimsor
    for d in dijazottak2:
        if d.tipus==tipus:
            file.write(f'{d.ev}:{d.teljesnev}\n')
    file.close()

def statisztika():
    stat={}
    for d in dijazottak:
        if d.tipus in stat.keys():
            stat[d.tipus]+=1
        else:
            stat[d.tipus]=1
    for key, value in stat.items():
        print(f'\t{str(key).ljust(26)}{value:4d} db')