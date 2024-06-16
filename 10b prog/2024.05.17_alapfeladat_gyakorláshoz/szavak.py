elso_szo=input('Adj meg egy szót! ')
masodik_szo=input('Adj meg egy másik szót! ')

if len(elso_szo)>len(masodik_szo):
    print(f'A hosszabb szó: {elso_szo}')
elif len(elso_szo)<len(masodik_szo):
    print(f'A hosszabb szó: {masodik_szo}')
else:
    print('A két szó egyforma hosszú')