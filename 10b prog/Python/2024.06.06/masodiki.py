import datetime

def number_input(szoveg,maximum):
    szam=0
    while szam<=0 or szam>maximum:
        try:
            szam=int(input(szoveg))
        except:
            print('Nem megfelelo szam!')
    return szam

def eltelt_napok(ev,honap,nap,ev2,honap2,nap2):
    date1=datetime.date(ev,honap,nap)
    date2=datetime.date(ev2,honap2,nap2)
    diff=date2-date1
    return diff

ev=number_input('Kérem a datum elso evet: ',2024)
honap=number_input('Kérem a datum elso honapjat: ',12)
nap=number_input('Kérem a datum elso napjat: ',31)

ev2=number_input('Kérem a datum masodik evet: ',2024)
honap2=number_input('Kérem a datum masodik honapjat: ',12)
nap2=number_input('Kérem a datum masodik napjat: ',31)

print(f'{ev}.{honap}.{nap} és {ev2}.{honap2}.{nap2} között {eltelt_napok(ev,honap,nap,ev2,honap2,nap2).days} nap volt')