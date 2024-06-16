print('LNKO kivonásos algoritmussal')
a = int(input('a = '))
b = int(input('b = '))

if a > b:
    kisebb=b
    nagyobb=a
else:
    kisebb=a
    nagyobb=b

while nagyobb != kisebb:
    nagyobb-=kisebb
    if nagyobb<kisebb:
        nagyobb,kisebb=kisebb,nagyobb #megcsereli a 3 valtozot

print(f'LNKO({a},{b}) = {nagyobb}')