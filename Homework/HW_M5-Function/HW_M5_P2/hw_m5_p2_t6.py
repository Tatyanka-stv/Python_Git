def raise_number_to_power(input_list, power):
    result_list = [x ** power for x in input_list]
    return result_list

import random
import math

start_of_list = float(input('Введіть першу межу діапазона чисел: '))
end_of_list = float(input('Введіть другу межу діапазона чисел: '))
count_numbers_in_list = float(input('Введіть бажану кількість чисел у діапазоні: '))
exponent = float(input('Введіть ступінь, до якої треба піднести число: '))


if (abs(start_of_list) - math.trunc(abs(start_of_list)) == 0) and (abs(end_of_list) - math.trunc(abs(end_of_list)) == 0) and (abs(count_numbers_in_list) - math.trunc(abs(count_numbers_in_list)) == 0) and (abs(exponent) - math.trunc(abs(exponent)) == 0):
     start_of_list = int(start_of_list)
     end_of_list = int(end_of_list)
     count_numbers_in_list = int(count_numbers_in_list)
     exponent = int(exponent)
     if count_numbers_in_list > 0:
        if start_of_list > end_of_list:
            random_list = [random.randint(end_of_list, start_of_list) for _ in range(count_numbers_in_list)]
            result = raise_number_to_power(random_list, exponent)
        else:    
            random_list = [random.randint(start_of_list, end_of_list) for _ in range(count_numbers_in_list)]
            result = raise_number_to_power(random_list, exponent)
        print('Початковий список елементів: \n', random_list)
        print('Сформований випадковий список із елементами, піднесеними у ступінь '+str(exponent)+' : \n', result)
       
     else:
         print('Кількість елементів не може бути відємною або дорівнювати 0.')
else:
    print('Ви ввели не ціле число.')