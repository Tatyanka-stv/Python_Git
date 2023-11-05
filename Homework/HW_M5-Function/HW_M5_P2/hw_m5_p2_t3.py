def is_prime(number): #перевіряємо чи є число простим
    import math
    number = abs(number) #число зі списку може бути відємним
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def count_of_prime_numbers(numbers): #підраховуємо кількість простих чисел
    prime_count = 0
    for num in numbers:
        if is_prime(num):
            prime_count = prime_count + 1
    return prime_count

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
            result = count_of_prime_numbers(random_list)
        else:    
            random_list = [random.randint(start_of_list, end_of_list) for _ in range(count_numbers_in_list)]
            result = count_of_prime_numbers(random_list)
        print('Сформований випадковий список із завданими параметрами:\n', random_list)
        print('Кількість простих чисел у списку:', result)
     else:
         print('Кількість елементів не може бути відємною або дорівнювати 0.')
else:
    print('Ви ввели не ціле число.')