file=open('gyumolcsok.txt','r',encoding='UTF8')

sor=file.readline()
sor=sor.strip()

kovi_sor=file.readline().strip()

print(sor)
print('teszt')
print(kovi_sor)
file.close()

gyum=[]
file=open('gyumolcsok.txt','r',encoding='UTF8')

for sor in file:
    gyum.append(sor.strip())
file.close()

print(gyum)
print('-----------------------------------------------------------')

gyum.clear() #kiuritjuk a listat

#fejleces beolvasas
file=open('gyumolcsok_fejleccel.txt','r',encoding='UTF8')
file.readline() # ha nincs ra szukseg
#elso_sor=file.readline() #elrakjuk kesobbre

for sor in file:
    gyum.append(sor.strip())
file.close()

print(gyum)