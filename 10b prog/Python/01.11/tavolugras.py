# 12 versenyzo van
#mindenki 6ot ugrik
# 7-8.5m kozott
# 30% esely hogy ervenytelen


#1. versenyzo ugrasai: x.y x.y ervenytelen x.y ...
#1. versenyzo legnagyobb ugrasa: 8.5

from random import randint

def ugrasok()->list[float]:
    ugras=[]
    for i in range(6):
        egy_ugras=randint(700,850)/100
        if randint(1,10)<=3:
            egy_ugras=0
        ugras.append(egy_ugras)
    return ugras

def egy_eredmeny(rajtszam:int,ugras:list)->None:
    print(f'{rajtszam}. versenyzo ugrasai:',end=' ')
    for u in ugras:
        if u==0:
            print('ervénytelen',end=' ')
        else:
            print(u,end=' ')
    print(f'\n\t{rajtszam}. versenyzo legnagyobb ugrasa {legnagyobb_ugrasa(ugras)} méter')

def legnagyobb_ugrasa(ugras:list)->float:
    legnagyobb=0
    for u in ugras:
        if u>legnagyobb:
            legnagyobb=u
    return legnagyobb
    
