from random import randint

szamok=[]

def feltolt(n:int,min:int,max:int)->None:
    """
    Feltolti a listat 'n darab min es max kozotti ertekkel
    """
    for i in range(n):
        szamok.append(randint(min,max))


def kiir()->None:
    for szam in szamok:
        print(szam,end=' ')


def osszeg()->int:
    osszeg=0
    for szam in szamok:
        osszeg+=szam
    return osszeg


def atlag()->float:
    return osszeg()/len(szamok)


def keres(sz:int)->bool:
    for szam in szamok:
        if szam==sz:
            return True
    return False