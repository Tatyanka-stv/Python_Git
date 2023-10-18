# Получаем строку от пользователя
user_string = input("Введите строку: ")

num_letters = 0
num_digits = 0
other_symbols = 0

for char in user_string:
    if char.isalpha():  # Проверка, является ли символ буквой
        num_letters = num_letters + 1
    else:
        if char.isdigit():  # Проверка, является ли символ цифрой
            num_digits = num_digits + 1
        else:     
            other_symbols = other_symbols + 1

# Выводим результат
print('Кількість букв: ', num_letters)
print('Кількість цифр: ', num_digits)
print('Кількість інших символів:', other_symbols)