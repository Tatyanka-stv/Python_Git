# даємо запит на ввод числа
input_digits = int(input('Введіть ціле число: '))

# вказуємо цифри для видалення
digits_to_remove = '36'

# перетворюємо введене число у рядок для подальшої роботи
number_str = str(input_digits)

 # формуємо новий рядок, перевіряючи посимвольно, що кожен символ не входить у символи видалення (тобто 3 і 6)
result_str = ''.join(char for char in number_str if char not in digits_to_remove)

# перетворюємо рядок знову у число
result_number = int(result_str)

# виводимо результат
print('Результат післе видалення цифр 3 та  6:', result_number)