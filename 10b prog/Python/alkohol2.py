ma_ev=2023
ma_honap=9
ma_nap=14

szuletesi_datum=input('Születési dátum(éééé.hh.nn): ')
(szuletesi_ev,szuletesi_honap,szuletesi_nap)=szuletesi_datum.split('.')  # . karakter mentén szétdarabol

szuletesi_ev=int(szuletesi_ev)
szuletesi_honap=int(szuletesi_honap)
szuletesi_nap=int(szuletesi_nap)

#Logikai változók lehetséges értékei:
    #False - hamis
    #True - igaz

elmult_18=False #kezdetben azt állítom, hogy nem igaz az hogy elmúlt 18 éves

#2005.09.14
if ma_ev-szuletesi_ev>18:
    elmult_18=True  #a feltétel igaz, ezért átbillentjük igazra
elif ma_ev-szuletesi_ev==18:
    if ma_honap>szuletesi_honap:
        elmult_18=True
    elif ma_honap==szuletesi_honap:
        if ma_nap>szuletesi_nap:
            elmult_18=True

if elmult_18:   #elmult_18==True
    print('Vehet alkoholt!')
else:
    print('Nem vehet alkoholt!')