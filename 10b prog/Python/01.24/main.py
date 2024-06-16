from auto import auto

# az_en_autom=auto #egy darab peldany jon letre
# az_en_autom.rendszam='PAR-094'
# az_en_autom.szin='Piros'                       #ctrl k c osszes komment
# az_en_autom.tipus='Audi'
# az_en_autom.teljesitmeny=707
# az_en_autom.gyorsulas=2.9

# romio_autoja=auto
# romio_autoja.rendszam='SHARKZ-03'
# romio_autoja.szin='fehér'
# romio_autoja.tipus='LADA Niva'
# romio_autoja.teljesitmeny=180

# print(romio_autoja.tipus)


autok:list[auto]=[]

egy_auto=auto('Audi','PPP-111','fekete',562,4.24)
autok.append(egy_auto)

autok.append(auto('BMW','KAS-561','kek',470))
autok.append(auto('Merci','STR-964','fekete',633))
autok.append(auto('Dodge','ASD-311','feher',808))

for i in range(len(autok)):
    print(f'{i+1}. {autok[i].tipus.ljust(10)} {autok[i].rendszam.ljust(10)} {autok[i].szin.ljust(6)} {autok[i].teljesitmeny}le ')