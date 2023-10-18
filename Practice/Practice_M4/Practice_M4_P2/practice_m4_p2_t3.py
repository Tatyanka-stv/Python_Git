numbers = [] #формуємо для роботи порожній список
while True:
    user_number = input('Введіть ціле число (або "'"q"'" для завершення ввода): ')
    if user_number.lower() == 'q':
        break
    try:
        number = int(user_number)
        numbers.append(number)
    except ValueError:
        print('Введене число не є цілим! Введіть ціле число.')

if not numbers: #перевіряємо чи список порожній
    print('Список порожній.')
else:
    #total_sum, average = sum_and_average_of_numbers(numbers)
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    print('Сума усіх чисел: ', total_sum)
    print('Середнє арифметичне значення усіх чисел: ', round(average, 2))