bejutott=False

while bejutott==False:
    felhasznalonev=input('Adja meg a felhasználónevét!: ')
    jelszo=input('Adja meg a jelszavát!: ')
    if felhasznalonev=='Petii1124' and jelszo=='kaka123':
        print('Belépés engedélyezve.')
        bejutott=True
    else:
        print('Belépés megtagadva.')
