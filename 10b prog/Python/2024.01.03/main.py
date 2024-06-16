from nevsor import *

#hany ember van a csoportban?
print(f'A csoportban {letszam()} tanulo van')

#ki a leghosszabb nevu?

print(f'A leghoszabb nev: ')
for nev in nevek:
    if len(nev)==leghosszabb():
        print(f'\t\t{nev}')

#atlagos nevhossz
print(f'Az atlagos nevhossz {atlag_hossza():.2f} karakter.')

# van e az osztalyban keresett nevu tanulo?
keresttnev=input("Keresett nev:")