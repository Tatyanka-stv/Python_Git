def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

def calculate_factorials(input_list):
    factorial_list = [factorial(num) for num in input_list]
    return factorial_list

try:
    import random
    
    start_of_list = int(input('Введіть першу межу діапазона чисел: '))
    end_of_list = int(input('Введіть другу межу діапазона чисел: '))
    
    if start_of_list >=0 and end_of_list>=0:
        count_numbers_in_list = int(input('Введіть бажану кількість чисел у діапазоні: '))
    
        if count_numbers_in_list > 0: 
            if start_of_list > end_of_list:
                random_list = [random.randint(end_of_list, start_of_list) for _ in range(count_numbers_in_list)]
                result = calculate_factorials(random_list)
            else:    
                random_list = [random.randint(start_of_list, end_of_list) for _ in range(count_numbers_in_list)]
                result = calculate_factorials(random_list)
            print('Сформований випадковий список із завданими параметрами:\n', random_list)
            print(f'Факторіали списку дорівнюють: \n',result)
        else:
            print('Кількість елементів не може бути відємною або дорівнювати 0.')
    else:
        print('Межі не можуть бути відємними.')        
except:
    print('Ви ввели не ціле число.')