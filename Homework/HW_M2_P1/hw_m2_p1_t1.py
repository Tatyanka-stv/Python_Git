print('Введіть 3 числа: ')
a=float(input('Введіть перше число: '))
b=float(input('Введіть друге число: '))
c=float(input('Введіть третє число: '))
import math
print('Оберіть операцію:')
print('1: обраховуємо суму трьох чисел')
print('2: обраховуємо добуток трьох чисел')
n=float(input())
if n-math.trunc(abs(n))==0.0:
    n=int(n)
    if n==1:
         print('Сума трьох чисел дорівнює ',str(round(a+b+c, 2)))
    elif n==2:
         print('Добуток трьох чисел дорівнює ',str(round(a*b*c,2)))
    else:
         print('Ви ввели неправильну операцію')      
else:
     print('Ви ввели неправильну операцію') 
