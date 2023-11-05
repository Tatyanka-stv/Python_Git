def find_number_in_list(input_list, number_to_find):
    indixes = []
    count = 0
    for i in range(len(input_list)):
        if input_list[i] == number_to_find:
            indixes.append(i)
            count = count + 1
    return count, indixes 

try:
    import random
    
    start_of_list = int(input('Введіть першу межу діапазона чисел: '))
    end_of_list = int(input('Введіть другу межу діапазона чисел: '))
    count_numbers_in_list = int(input('Введіть бажану кількість чисел у діапазоні: '))
    
    if count_numbers_in_list > 0: 
        number_to_find = int(input('Введіть шукане число: '))
        if start_of_list > end_of_list:
            random_list = [random.randint(end_of_list, start_of_list) for _ in range(count_numbers_in_list)]
            count, indixes = find_number_in_list(random_list, number_to_find)
        else:    
            random_list = [random.randint(start_of_list, end_of_list) for _ in range(count_numbers_in_list)]
            count, indixes = find_number_in_list(random_list, number_to_find)
        print('Сформований випадковий список із завданими параметрами:\n', random_list)
        print("Кількість шуканих чисел:\n ", count)
        if indixes == []:
            print(' Число '+ str(number_to_find)+' відсутнє у списку.')
        else:    
            print(' Число '+ str(number_to_find)+' знаходиться на позиціях ', indixes, ' у списку.')
    else:
         print('Кількість елементів не може бути відємною або дорівнювати 0.')
except:
    print('Ви ввели не ціле число.')