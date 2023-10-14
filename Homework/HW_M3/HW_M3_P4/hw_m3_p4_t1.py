'''функция is_prime проверяет, является ли число простым, 
перебирая делители от 2 до квадратного корня из числа. 
Если число делится нацело хотя бы на один из делителей, оно не является простым.'''

def is_prime(num):
    if num < 2:
        return False # Числа меньше 2 не являются простыми
    # Проверка делителей от 2 до квадратного корня из числа
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False # Число делится нацело, не является простым
    return True  # Если не найдены делители, число простое

start_num = float(input('Введіть перше число: '))
end_num = float(input('Введіть друге число: '))
import math
if abs(start_num)-int(abs(start_num))==0 and abs(end_num)-int(abs(end_num))==0:
     start_num=int(start_num)
     end_num=int(end_num)
     if (start_num <= 0 and end_num <=0) or (start_num>=0 and end_num<=0) or (start_num<=0 and end_num>=0):
         print('Числа введені невірно.')
     if (start_num>=0 and start_num<=1) and (end_num>=0 and end_num<=1):
             print('Введені числа 0 або 1 не є простими числами.') 
     if start_num==end_num:
         print('Вивести числа неможливо, так як перше число дорівнює другому числу. Діапазон не формується.')
     if start_num>end_num:
         print('Числа введені невірно, так як перше число більше за  друге число.')
     if start_num>=2 and end_num>start_num:
         # Выводим простые числа в указанном диапазоне
         print("Прості числа в діапазоні від", start_num, "до", end_num, ":")
         for num in range(start_num, end_num + 1):
             if is_prime(num):
                 print(num, end=' ')
else:
    print('Числа введені невірно. Вони є дійсними.')