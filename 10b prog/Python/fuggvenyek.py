# mire hasznaljuk a fuggvenyeket?
#olyan kis programegysegek, amelyeket valtozatos bemeneti adatokkal szeretnenk vegrehajtani, akar sokszor
#cel az ujrahasznosithatosag!!!
# mit kell tudni a fugvenyekrol?
# - mit csinal a fugg? (a neve utaljon a megvalositott feladatra)
# - mi a parameterlistaja(neve után zárojelben felsorolt valtozok)
# - formális paraméterei (neve után zárojelben megadott valtozonevek, esetleg tipusai)
# - aktualis parameterlista (a fuggveny hivasakor a fgv.-nek adott konkret ertek {ez lehet valtozo is})
# - mit ad vissza eredmenyul (return kulcsszo utani ertek)
# a fgv. csak a meghivasakor fut le. Letrehozasakor csak letrejon, de nem hajtodik vegre!

def osszeg(a:float,b:float)->float:#tipus megadasa
    #print(a+b) #nem kiirni szeretnenk
    osszeg=a+b #fvg magja
    return osszeg
    print("Ani a return utan van, azt nem fogjuk latni")


print(osszeg(10,30)) #10, 30 aktualis parameterek