a=float(input('Введіть будь-яке ціле число: '))
b=float(input('Введіть будь-яке ціле число: '))
print('Оберіть потрібну операцію:')
print('1: підрахунок суми двох чисел ')
print('2: підрахунок різниці двох чисел ')
print('3: підрахунок середнього арифметичного двох чисел ')
c=int(input())
if c==1:
    print('Сума чисел дорівнює ',a+b)
elif c==2:
    print('Різниця двох чисел дорівнює ', a-b)
elif c==3:
    print('Середнє арифметичне дорівнює ', (a+b)/2)
else:
    print('Ви ввели неправильний номер операції')
 
print('task done')