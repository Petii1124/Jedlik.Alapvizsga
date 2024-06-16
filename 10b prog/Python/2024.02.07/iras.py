zoldseg=input('Adja meg a zoldseget: ')
#file=open('zoldsegek.txt','w',encoding='UTF8')
#file.write(zoldseg)
file=open('zoldsegek.txt','a',encoding='UTF8')
file.write(zoldseg+'\n')

zoldsegek=['hagyma','zeller','hagyma','karfiol']
for z in zoldsegek:
    file.write(z+'\n')

file.close()