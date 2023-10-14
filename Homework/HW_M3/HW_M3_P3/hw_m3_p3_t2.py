print('Підрахунок цілих чисел від 100 до 999, у яких є 2 однакові цифри:')
count_numbers_with_two_same_digits = 0
import math
for number in range(100, 1000):
     a = int(number/100)
     b = int((number - a * 100)/10)
     c = number-a*100-b*10
     if a==b or a==c or b==c:
         print(number, end=' ')
         count_numbers_with_two_same_digits =  count_numbers_with_two_same_digits +  1

print('Кількість чисел з двумя одинаковыми цифрами: ', count_numbers_with_two_same_digits)         