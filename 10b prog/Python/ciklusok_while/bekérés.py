# ellenorzott bekérés (még nem tokeletes)
#kerjunk be egy számot 10 és 100 kozott. a bekerest ismeteljuk addig, amig nem jo erteket ad meg!

szam=-1 # olyan kezdoertek, amely eloszor teljesiti a while feltételét

while szam<10 or szam>100:
    #szam=int(input('Kerek egy szamot 10 es 100 kozott: '))
    input_txt=input('Kerek egy szamot 10 es 100 kozott: ')
    if input_txt.isnumeric(): # csak szamjegyeket fogad el, nincs elojel,tizedes pont!! 0 vagy pozitiv egesz
        szam=int(input_txt)
    else:
        print('Egsz szamot adjon meg!!')

#kesobb
    #float_input sajat fuggveny
    #int_input  sajat fuggveny negativ is