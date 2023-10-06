print('Введіть діаметр кола: ')
d=float(input())
import math
if d>0:
    print('Оберіть операцію:')
    print('1: обраховуємо площу круга')
    print('2: обраховуємо периметр кола')
    n=float(input())
    import math
    if n-math.trunc(abs(n))==0.0:
        n=int(n)
        if n==1:
            d=math.pi*(d**2)/4
            print('Площа круга дорівнює ',round(d,2)) 
        elif n==2:
            d=math.pi*d
            print('Периметр кола дорівнює ',round(d,2))
        else:
           print('Ви ввели неправильну операцію')      
    else:
        print('Ви ввели неправильну операцію') 
else:
    print('Ви ввели неправильне число')