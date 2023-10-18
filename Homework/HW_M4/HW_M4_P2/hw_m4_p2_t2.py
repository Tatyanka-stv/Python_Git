import random

# Створюємо список випадкових цілих чисел від 10 до 10
random_numbers = [random.randint(-10, 10) for _ in range(20)]

min_number = min(random_numbers)
max_number = max(random_numbers)

count_of_negative_numbers = 0
for number in random_numbers: 
    if number < 0:
        count_of_negative_numbers = count_of_negative_numbers + 1

count_of_positive_numbers = 0
for number in random_numbers: 
    if number > 0:
        count_of_positive_numbers = count_of_positive_numbers + 1

count_zero = 0
for number in random_numbers: 
    if number == 0:
        count_zero = count_zero + 1

print('Список випадкових цілих чисел:', random_numbers)
print('Мінімальний елемент зі списку:', min_number)
print('Максимальний елемент зі списку:', max_number)
print('Кількість відємних елементів у списку: ', count_of_negative_numbers)
print('Кількість додатніх елементів у списку: ', count_of_positive_numbers)
print('Кількість нулів: ', count_zero)