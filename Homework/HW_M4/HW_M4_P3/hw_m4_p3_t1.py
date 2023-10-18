import random
# Генерация двух случайных списков целых чисел
list1 = [random.randint(1, 20) for _ in range(10)]
list2 = [random.randint(10, 30) for _ in range(15)]
print('Список 1:', list1)
print('Список 2:', list2)

# 1 Формирование третьего списка, содержащего элементы обоих списков
combined_list = list1 + list2
print('Комбінований список:', combined_list)

# 2 формируем комбинированныйсписок без повторений, проверяя элементы списка на совпадение друг с другом
unique_combined_list = [] #создаем пустой список
for item in combined_list:
    if item not in unique_combined_list:
        unique_combined_list.append(item)
print('Комбінований список без повторень елементів 2х вихідних списків:', unique_combined_list)

#3 формируем комбинированный список из общих элементов 2х списков, которые есть в обоих списках
common_elements_list = []
for item in list1:
    if item in list2:
        common_elements_list.append(item)
print('Комбіновани список, який містить спільні елементи 2х вихідних списків: ', common_elements_list)        

#4 формируем комбинированный список, содержащий только уникальные элементы каждого из списков
unique_elements_list = []
# Добавляем уникальные элементы из первого списка
for item in list1:
    if item not in unique_elements_list:
        unique_elements_list.append(item)
# Добавляем уникальные элементы из второго списка
for item in list2:
    if item not in unique_elements_list:
        unique_elements_list.append(item)
print('Комбінований список, який містить тільки унікальні елементи 2х вихідних списків: ', unique_elements_list)

#5 формируем комбинированный список, содержащий максимальные и минимальные  элементы из 2х начальных списков
import sys
min_max_list = []
# Находим минимальное и максимальное значение для list1 
min_list1 = sys.maxsize
max_list1 = -sys.maxsize
for item in list1:
    min_list1 = min(min_list1, item)
    max_list1 = max(max_list1, item)
min_max_list.extend([min_list1, max_list1])
# Находим минимальное и максимальное значение для list2
min_list2 = sys.maxsize
max_list2 = -sys.maxsize
for item in list2:
    min_list2 = min(min_list2, item)
    max_list2 = max(max_list2, item)
min_max_list.extend([min_list2, max_list2])
print('Комбінований список, який складається з мінімальних та максимальних значень кожного списка:' , min_max_list)