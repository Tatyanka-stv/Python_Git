def count_digits(number):
    number_as_string = list(number)
    
    count = 0
    for symbol in number_as_string:
        if symbol.isdigit():
            count = count +1
        else:
            print('Введений рядок не є числом')
            break    
    
    if count == len(number_as_string):
        print('Кількість цифр у числі '+str(number)+' дорівнює '+str(count))

number = input('Введіть число: ')
count_digits(number)