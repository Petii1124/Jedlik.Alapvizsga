from tanulok import *

tanulok_feltolt(10)
tanulo_kiir()
print(f'\nAz osztaly{o_atlag():.2f}')
print(f'{atlag_felett()} ember van az atlag felett.')

legjobb=legjobb()
print(f'A legjobb tanulo: {legjobb.vezeteknev} {legjobb.keresztnev} {legjobb.atlag()}')