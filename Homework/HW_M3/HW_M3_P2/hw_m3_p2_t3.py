print('Розяснення до задачі:')
print('Відбувається введення чисел доки не введемо число 7')
while True:
    input_number = float(input('Введіть число: '))
    if input_number == 7:
        print("Good bye!")
        break
    elif input_number > 0:
        print('Number is positive')
    elif input_number < 0:
        print('Number is negative')
    else:
        print('Number is equal to zero')