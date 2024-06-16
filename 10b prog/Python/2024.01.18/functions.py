versenyzok=['BASTIEN Steven', 'dos SANTOS Felipe', 'DUBLER Cedric', 'ERM Johannes', 'HELCELET Adam Sebastian', 'KAZMIREK Kai', 'LEPAGEPierce', 'MAYER Kevin', 'MOLONEY Ashley', 'ROE Martin', 'SCANTLING Garrett', 'SHKURENYOV Ilya', 'SYKORA Jiri', 'TILGA Karel', 'UIBOMaicel', 'URENA Jorge', 'VICTOR Lindon', 'WARNER Damian','WIESIOLEK Pawel', 'ZHUK Vitaliy', 'ZIEMEK Zachery']
pontok=[8236, 7880, 7008, 8213, 8004, 8126, 8604, 8726, 8649, 7863, 8611, 8413, 7943, 7018, 8037, 8322, 8414, 9018, 8176, 8131, 8435]

def versenyzok_szama()->int:
    print(f'A versenyen {len(versenyzok)} versenyző idult.')

def min8600()->int:
    db=0
    for pont in pontok:
        if pont >= 8600:
            db+=1
    return db

def pontok_atlaga()->float:
    osszeg=0
    for pont in pontok:
        osszeg+=pont
    return osszeg/ len(pontok)

def nyertes():
    nyertes=0
    for i in range(len(pontok)):
        if pontok[i]>pontok[nyertes]:
            nyertes=i
    return nyertes
    
def versenyzo_pont(nev:str)->int|bool:
    for i in range(len(versenyzok)):
        if versenyzok[i]==nev:
            return pontok[i]
    return False