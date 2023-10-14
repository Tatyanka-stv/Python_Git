a=int(input('Input start number: '))
b=int(input('Input end number: '))
if a>b:
    a,b=b,a
s=0
n=0
print('Формуємо ряд чисел: ')
for i in range(a,b+1,1):
    s=s+i
    n=n+1
    print(i,end=' ')
print(' ')    
avg=s/n
print('Сума усіх чисел ряду дорівнює ',s)
print('Середнє арифметичне значення усіх чисел ряду дорівнює ', avg)  