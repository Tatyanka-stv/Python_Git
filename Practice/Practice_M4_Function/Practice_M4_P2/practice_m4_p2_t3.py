def count_elements(input_list):
    even_count = 0
    odd_count = 0
    positive_count = 0
    negative_count = 0

    for num in input_list:
        if num % 2 == 0:
            even_count = even_count + 1
        else:
            odd_count = odd_count + 1
        if num > 0:
            positive_count = positive_count + 1
        elif num < 0:
            negative_count = negative_count +1

    return even_count, odd_count, positive_count, negative_count

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
            even_count, odd_count, positive_count, negative_count = count_elements(random_list)
        else:    
            random_list = [random.randint(start_of_list, end_of_list) for _ in range(count_numbers_in_list)]
            even_count, odd_count, positive_count, negative_count = count_elements(random_list)
        print('Сформований випадковий список із завданими параметрами:\n', random_list)
        print("Кількість парних чисел: ", even_count)
        print("Кількість непарних чисел: ", odd_count)
        print("Кількість додатніх чисел: ", positive_count)
        print("Кількість від'ємних чисел: ", negative_count) 
     else:
         print('Кількість елементів не може бути відємною або дорівнювати 0.')
else:
    print('Ви ввели не ціле число.')