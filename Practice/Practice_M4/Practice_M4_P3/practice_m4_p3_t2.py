import random

# Создаем список случайных целых чисел
random_numbers = [random.randint(-10, 10) for _ in range(20)]
print("Згенерований список випадкових чисел:\n", random_numbers,'\n')

print('Розвязання поставлених задач:\n')

#формуємо список парних чисел, список непарних чисел, список відємних чисел, список  додатніх чисел
list_evens = []
list_odds = []
list_negatives= []
list_positives= []

for number in random_numbers:
    if number % 2 == 0 and number != 0:
        list_evens.append(number)
    else:
        if number != 0:
            list_odds.append(number)

    if number < 0:
        list_negatives.append(number)  
    else:
        if number > 0:
            list_positives.append(number)          

print("Список парних чисел:\n", list_evens,'\n')

print("Список непарних чисел:\n", list_odds,'\n')

print("Список відємних чисел:\n", list_negatives,'\n')

print("Список додатніх чисел:\n", list_positives,'\n')