#Ez egy komment

'''
Több 
soros
komment
'''

#ctrl+k+c ctrl+k+u

print('Szia Erick!')
print('kutya "mondom"erick')

szam=25.9
print(szam)     #valtozo
print(type(szam))    #valtozo tipusa

a="alma"
b="fa"
print(a+b) #összefűzés

a=10
b=5
c=a+b
print(c)
print(a+b) #összeadás

print('c='+str(a+b)) #szambol szoveg str(a+b)
print(f'c={a+b}') #ugyanez
print(f'{a}+{b}={c}')
#----------------------------------------------------
#valtozok
'''
nem kezdodhet szammal
nem lehet benne szokoz
nem lehet benne specialis karakter CSAK 0-9 vagy A-Z vagy a-z vagy _
'''
péter1=12
péter_neve="péter"

'''
asd=12 - Tilos!
a=2 helyett a_oldal=2
felismerheto valtozonevek
'''
#--------------------------------------------------------
#alt+shift+ lefele nyil

#auto adatai (tipus,tulajdonos)
auto_tipus='Audi'
auto_tulaj='Jancsika' #snake case _ a szavak kozt

autoTipus='Audi'  #camel case masodik szo kezdoje nagy

AutoTipus='Audi'  #Pascal case

#---------------------------------------------------------
print('\t Tabulator', end='') #nem enterre vegzodik --> egy sorba a kovivel
print('\t\t Ket tabulator')
print('\n\nSoremeles\n\t Uj sor tabulatorral')

print('alma', 'korte', 'barack', 'szilva',sep='-',end='-') #sep utan - , ra ki lehet cserelni a szokozt
print('narancs')

