#kerjunk be egy szamot es irjuk ki a faktorialisat!
# n! =1*2*3*4*..*(n-1)*n
# 5!= 1*2*3*4*5=120

n=int(input('n = '))
faktorialis=1 #kezdoertek

print(f'{n}! =1',end='') #kiiras eleje
for i in range(2,n+1):
    faktorialis*=i  #fak=fak*i
    print(f'*{i}',end='')#kiiras kozepe

print(f'={faktorialis}')#kiiras vege