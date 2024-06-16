# döntsük el vehet-e alkoholt vagy nem

ma_ev=2023
ma_honap=9
ma_nap=14

szuletesi_ev=int(input('Születési éve: '))

if ma_ev-szuletesi_ev<18:
    print('Nem vehet alkoholt!')
elif ma_ev-szuletesi_ev>18:
    print('Vehet alkoholt!')
else:
    szuletesi_honap=int(input('Születési hónapja: '))
    if ma_honap<szuletesi_honap:
        print('Vehet alkoholt!')
    elif ma_honap-szuletesi_honap>9:
        print('Vehet alkoholt!')
    else:
        szuletesi_nap=int(input('Születési napja: '))
        if ma_nap<szuletesi_nap:
            print('Vehet alkoholt!')
        elif ma_nap-szuletesi_nap>14:
            print('Nem vehet alkoholt!')
        else:
            if ma_nap==szuletesi_nap:
                print('Vehet alkoholt! Boldog születésnapot!')