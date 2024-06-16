from random import random,randint

elojott=0

for i in range(1,8):
    print(f'{i}. nap:')
    reggel=randint(-5,10)+random()
    delben=randint(5,25)+random()
    este=randint(0,15)+random()
    print(f'Reggel: {reggel:.2f}')
    print(f'Delben: {delben:.2f}')
    print(f'Ese: {este:.2f}')
    atlag=(reggel+delben+este)/3
    if atlag>10:
        print('Ma elojott a medve!')
        elojott+=1
    else:
        print('Ma nem jott elo a medve!')
print(f'A héten {elojott} alkalommal jott elo a medve.')