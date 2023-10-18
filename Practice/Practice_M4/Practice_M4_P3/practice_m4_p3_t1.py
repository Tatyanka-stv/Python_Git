import random

# Создаем список случайных целых чисел
random_numbers = [random.randint(-10, 10) for _ in range(20)]
print("Згенерований список випадкових чисел:\n", random_numbers,'\n')

print('Розвязання поставлених задач:\n')
sum_negatives = 0 #сума відємних чисел
sum_evens = 0 #сума парних чисел
sum_odds = 0 #сума непарних чисел
number_with_index_multiple_of_3 = 1  # Произведение элементов с индексами кратными 3
product_between_min_and_max = 1 #добуток максимуму та мінімуму
sum_between_first_and_last_positive = 0

min_num = min(random_numbers)
max_num = max(random_numbers)
index_of_min_number = random_numbers.index(min(random_numbers)) #знайшли індекс мінімального елементу
index_of_max_number = random_numbers.index(max(random_numbers)) #знайшли індекс максимального елементу

list_negatives= []
list_evens = []
list_odds = []
list_numbers_between_min_and_max = []
list_numbers_between_first_and_last_positive = []
list_number_with_index_multiple_of_3 = []

for number in random_numbers:
    if number < 0:
        sum_negatives = sum_negatives + number
        list_negatives.append(number)

    if number % 2 == 0 and number != 0:
        sum_evens = sum_evens + number
        list_evens.append(number)
    else:
        if number != 0:
            sum_odds = sum_odds + number
            list_odds.append(number)
  
#формуємо список елементів з індексам,и кратними 3
for i in range(1,len(random_numbers)+1,1):
    if i % 3 == 0:
       number_with_index_multiple_of_3 = number_with_index_multiple_of_3 * random_numbers[i]
       list_number_with_index_multiple_of_3.append(random_numbers[i])
    else:
        continue  

#формуємо список елементів, які знаходяться між мініальним та максимальним елементом, враховуючи що макс. елемент може стоять або переде або за мін. елементов, або поряд один з іншим
if index_of_min_number < index_of_max_number:
    for i in range(index_of_min_number+1, index_of_max_number,1):
        product_between_min_and_max =  product_between_min_and_max * random_numbers[i]
        list_numbers_between_min_and_max.append(random_numbers[i])
else:
    if index_of_min_number > index_of_max_number:
        for i in range(index_of_max_number+1, index_of_min_number,1):
            product_between_min_and_max =  product_between_min_and_max * random_numbers[i]
            list_numbers_between_min_and_max.append(random_numbers[i])
    else:
        print('Добуток елементів, які знаходяться між мінімальним та максимальним елементами списку дорівнює 0, оскільки максимальний та мінімальний елементи списку стоять поряд та між ними немає шнших елементів списку.')            
    

#знаходимо індекс першого додатнього числа
index_first_positive_number = None 
index_last_positive_number = None

#знаходимо індекс першого додатнього числа
for i in range(0,len(random_numbers)+1,1):
    if random_numbers[i] > 0:
        index_first_positive_number = i
        break

#знаходимо індекс останього додатнього числа: просто йдемо з кінця спичку та знаходимо перше додатнє число з кінця списку
for i in range(len(random_numbers)-1,-1,-1):
    if random_numbers[i] > 0:
        index_last_positive_number = i
        break   

#формуємо список єлеметів, які знаходяться між першим та останнім додатнім елементами списку
if index_first_positive_number < index_last_positive_number:
    for i in range(index_first_positive_number+1, index_last_positive_number,1):
        sum_between_first_and_last_positive = sum_between_first_and_last_positive + random_numbers[i]
        list_numbers_between_first_and_last_positive.append(random_numbers[i])
else:
    if index_first_positive_number == index_last_positive_number:
        print('Сума елементів, які знаходяться між першим та останнім додатніми елементами списку, дорівнює 0. Оскільки таких елементів немає.')



print("Список відємних чисел:\n", list_negatives)
print("Сума відємних чисел:", sum_negatives,'\n')

print("Список парних чисел:\n", list_evens)
print("Сума парних чисел:", sum_evens,'\n')

print("Список непарних чисел:\n", list_odds)
print("Сума непарних чисел:", sum_odds,'\n')

print("Список елементів з індексами, кратнми 3:\n", list_number_with_index_multiple_of_3)
print("Добуток елементів з індексами, кратними 3:", number_with_index_multiple_of_3,'\n')

print("Мінімальний елемент списку: ", min_num)
print("Максимальний елемент списку: ", max_num)
print("Список елементів, які знаходяться між мінімальним та максимальним елементами списку:\n", list_numbers_between_min_and_max)
print("Добуток елементів, які знаходяться між мінімальним та максимальним елементами списку:", product_between_min_and_max,'\n')

if (index_first_positive_number is not None) and  (index_last_positive_number is not None):
    print("Список елементів, які знаходяться між першим та останнім додатніми елементами списку:\n", list_numbers_between_first_and_last_positive)
    print("Сума елементів, які знаходяться між першим та останнім додатніми елементами списку:", sum_between_first_and_last_positive)
else:
    if ((index_first_positive_number is not None) and  (index_last_positive_number is None)) or ((index_first_positive_number is None) and  (index_last_positive_number is not None)):
        print('Порахувати суму елементів, які знаходяться між першим та останнім додатніми елементами списку, неможливо, оскільки у списку тільки 1 додатній елемент.')