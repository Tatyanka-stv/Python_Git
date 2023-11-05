def find_minimum(numbers):
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num 
    return min_num

import random
import math

start_of_list = float(input('Введіть першу межу діапазона чисел: '))
end_of_list = float(input('Введіть другу межу діапазона чисел: '))
count_numbers_in_list = float(input('Введіть бажану кількість чисел у діапазоні: '))


if (abs(start_of_list) - math.trunc(abs(start_of_list)) == 0) and (abs(end_of_list) - math.trunc(abs(end_of_list)) == 0) and (abs(count_numbers_in_list) - math.trunc(abs(count_numbers_in_list)) == 0):
     start_of_list = int(start_of_list)
     end_of_list = int(end_of_list)
     count_numbers_in_list = int(count_numbers_in_list)
     if count_numbers_in_list > 0:
        if start_of_list > end_of_list:
            random_list = [random.randint(end_of_list, start_of_list) for _ in range(count_numbers_in_list)]
            result = find_minimum(random_list)
        else:    
            random_list = [random.randint(start_of_list, end_of_list) for _ in range(count_numbers_in_list)]
            result = find_minimum(random_list)
        print('Сформований випадковий список із завданими параметрами:\n', random_list)
        print('Мінімальний елемент випадкового списку:', result)
     else:
         print('Кількість елементів не може бути відємною або дорівнювати 0.')
else:
    print('Ви ввели не ціле число.')