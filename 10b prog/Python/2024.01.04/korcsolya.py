from random import randint

versenyzok_osszpont=[] #osszes versenyzo

def random_pont()->float:
    #return randint(0,9)+randint(0,4)/4
    return randint(0,40)/4

def versenyzo_pontjai()->list[float]:
    pontszamok=[]
    for i in range(7):
        pontszamok.append(random_pont())
    return pontszamok

def gyoztes_sorszam()->int:
    max_sorszam=0
    max_pont=0
    for i in range(len(versenyzok_osszpont)):
        if versenyzok_osszpont[i]>max_pont:
            max_pont=versenyzok_osszpont[i]
            max_sorszam=i
    return max_sorszam+1
        