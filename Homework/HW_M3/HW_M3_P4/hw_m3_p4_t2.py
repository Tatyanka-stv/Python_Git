def pad_string_with_spaces(input_string, desired_length): #функцыя, которая будет добавлять пробелы до указанной длины строки
    # Проверяем текущую длину строки
    current_length = len(input_string)
    
    # Если строка уже достаточно длинная, возвращаем её без изменений
    if current_length >= desired_length:
        return input_string
    
    # Иначе добавляем пробелы до нужной длины
    padding_spaces = ' ' * (desired_length - current_length)
    padded_string = input_string + padding_spaces
    return padded_string


print('Виводимо таблицю множення:')
for i in range(1, 11):
    for j in range(1, 11):
        original_string = str(j)+'*'+str(i)+'='+str(i * j)
        desired_length = 12 
        #длина строки которая должна быть с учетом дополненных пробелов, берем максимальную строку которая может сформироваться: єто 10*10=100, в ней 9 символом и добавляем еще 3 символа для будущих пробелов
        padded_string = pad_string_with_spaces(original_string, desired_length)
        print(padded_string,end=' ')
    print(end='\n')    