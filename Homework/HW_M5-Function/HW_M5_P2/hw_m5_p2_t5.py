def merge_lists(list1, list2):
    merged_list = list1 + list2
    return merged_list

import random
import math

print('Формуємо перший список:')
start_of_list1 = float(input('Введіть першу межу діапазона чисел: '))
end_of_list1 = float(input('Введіть другу межу діапазона чисел: '))
count_numbers_in_list1 = float(input('Введіть бажану кількість чисел у діапазоні: '))

print('Формкуємо другий список:')
start_of_list2 = float(input('Введіть першу межу діапазона чисел: '))
end_of_list2 = float(input('Введіть другу межу діапазона чисел: '))
count_numbers_in_list2 = float(input('Введіть бажану кількість чисел у діапазоні: '))


if (abs(start_of_list1) - math.trunc(abs(start_of_list1)) == 0) and (abs(end_of_list1) - math.trunc(abs(end_of_list1)) == 0) and (abs(count_numbers_in_list1) - math.trunc(abs(count_numbers_in_list1)) == 0) and (abs(start_of_list2) - math.trunc(abs(start_of_list2)) == 0) and (abs(end_of_list2) - math.trunc(abs(end_of_list2)) == 0) and (abs(count_numbers_in_list2) - math.trunc(abs(count_numbers_in_list2)) == 0):
     start_of_list1 = int(start_of_list1)
     end_of_list1 = int(end_of_list1)
     count_numbers_in_list1 = int(count_numbers_in_list1)

     start_of_list2 = int(start_of_list2)
     end_of_list2 = int(end_of_list2)
     count_numbers_in_list2 = int(count_numbers_in_list2)
     
     if (count_numbers_in_list1 > 0) and (count_numbers_in_list2 > 0): 
        
        if start_of_list1 > end_of_list1:
            random_list1 = [random.randint(end_of_list1, start_of_list1) for _ in range(count_numbers_in_list1)]
        else:    
            random_list1 = [random.randint(start_of_list1, end_of_list1) for _ in range(count_numbers_in_list1)]
           
        print('Сформований випадковий список  №1 із завданими параметрами:\n', random_list1)
        print()
        
        
        if start_of_list2 > end_of_list2:
            random_list2 = [random.randint(end_of_list2, start_of_list2) for _ in range(count_numbers_in_list2)]
           
        else:    
            random_list2 = [random.randint(start_of_list2, end_of_list2) for _ in range(count_numbers_in_list2)]
            
        print('Сформований випадковий список  №2 із завданими параметрами:\n', random_list2)
        print()
        
       
        result = merge_lists(random_list1, random_list2)     
        print('Список після обєднання 2х вихідних списків:\n', result)
        
     else:
         print('Кількість елементів не може бути відємною або дорівнювати 0.')
else:
    print('Ви ввели не ціле число.')