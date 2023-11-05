def remove_number_from_list(input_list, number_to_remove):
    count_removed_numbers = input_list.count(number_to_remove)  
    list_with_removed_numbers = [number for number in input_list if number != number_to_remove] 
    return list_with_removed_numbers, count_removed_numbers

import random
import math

start_of_list = float(input('Введіть першу межу діапазона чисел: '))
end_of_list = float(input('Введіть другу межу діапазона чисел: '))
count_numbers_in_list = float(input('Введіть бажану кількість чисел у діапазоні: '))
number_to_remove = float(input('Введіть число, яке потрібно видалити у діапазоні: '))


if (abs(start_of_list) - math.trunc(abs(start_of_list)) == 0) and (abs(end_of_list) - math.trunc(abs(end_of_list)) == 0) and (abs(count_numbers_in_list) - math.trunc(abs(count_numbers_in_list)) == 0) and (abs(number_to_remove) - math.trunc(abs(number_to_remove)) == 0):
     start_of_list = int(start_of_list)
     end_of_list = int(end_of_list)
     count_numbers_in_list = int(count_numbers_in_list)
     number_to_remove = int(number_to_remove)
     if count_numbers_in_list > 0: 
        if start_of_list > end_of_list:
            random_list = [random.randint(end_of_list, start_of_list) for _ in range(count_numbers_in_list)]
            list_with_removed_numbers, result = remove_number_from_list(random_list, number_to_remove)
        else:    
            random_list = [random.randint(start_of_list, end_of_list) for _ in range(count_numbers_in_list)]
            list_with_removed_numbers, result = remove_number_from_list(random_list, number_to_remove)
        print('Сформований випадковий список із завданими параметрами:\n', random_list)
        print('Список після видалення завданого числа:\n', list_with_removed_numbers)
        print('Кількість видалених чисел у списку:', result)
     else:
         print('Кількість елементів не може бути відємною або дорівнювати 0.')
else:
    print('Ви ввели не ціле число.')