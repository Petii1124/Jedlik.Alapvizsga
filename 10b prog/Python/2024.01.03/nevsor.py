nevek=['Magdics Áron','Melecky Ambrus','Nagy Péter','Nagy Rómeó','Németh Bence','Novák Maja','Papp Bence Csanád','Pram Bertalan','Sághi Szilárd','Sári Balázs','Simon Kristóf','Steingart Erik','Szabó Zsombor','Szaszák Péter','Szeiber Péter','Tóth Benedek','Vanyus Domonkos']

def letszam()->int:
    return len(nevek)

def leghosszabb()->int:
    hossz=0
    for nev in nevek:
        if len(nev)>hossz:
            hossz=len(nev)
    return hossz

def atlag_hossza()->float:
    osszeg=0
    for nev in nevek:
        osszeg+=len(nev)
    return osszeg /len(nevek)

def keresett(keresett:str)->bool:
    for nev in nevek:
        if nev==keresett:
            return True
    return False