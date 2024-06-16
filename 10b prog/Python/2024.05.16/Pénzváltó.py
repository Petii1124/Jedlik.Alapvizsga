penznem=input('Eurót (EUR) vagy forintot (HUF) akarsz váltani? ')

if penznem.upper()=='EUR':
    osszeg=int(input('Hány eurót akarsz beváltani? '))
    print(f'{osszeg} euróért {osszeg*365} forintot kapsz.')
elif penznem.upper()=='HUF':
    osszeg=int(input('Hány forintot akarsz beváltani? '))
    print(f'{osszeg} fortintért {osszeg/365:.2f} eurót kapsz.')