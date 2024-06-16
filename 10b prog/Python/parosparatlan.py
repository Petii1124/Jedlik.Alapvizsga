print('Páros-páratlan meghatározása\n')
bekert_szam=input('Kérem adjon meg egy egész számot:')
bekert_szam=int(bekert_szam)

#kétágú elágazás
if bekert_szam%2==0:    # elostom 2-vel a számot
    print('A szám páros!')  # ha igaz akkor páros
else:   #különben ág - páratlan
    print('A szám páratlan!')