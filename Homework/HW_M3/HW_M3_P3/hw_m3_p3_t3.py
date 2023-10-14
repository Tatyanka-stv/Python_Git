print('Підрахунок цілих чисел від 100 до 9999, у яких всі цифри різні:')
count_numbers_with_all_differ_digits = 0
count_numbers_1 = 0
count_numbers_2 = 0
import math
for number in range(100, 1000):
    a=int(number/100)
    b=int((number-a*100)/10)
    c=int(number-a*100-b*10)
    if a!=b:
        if a!=c and b!=c:
            print(number, end=' ')
            count_numbers_1=count_numbers_1+1
print('\n')
for number in range(1000, 10000):
    a=int(number/1000)
    b=int((number-a*1000)/100)
    c=int((number-a*1000-b*100)/10)
    d=int(number-a*1000-b*100-c*10)
    if (a!=b and a!=c and b!=c and b!=d and a!=d and c!=d):
        print(number, end=' ')
        count_numbers_2 = count_numbers_2+1


count_numbers_with_all_differ_digits=count_numbers_1+count_numbers_2
print('\n')
print('Кількість чисел від 100 до 9999, у яких всі цифри різні: ', count_numbers_with_all_differ_digits)       