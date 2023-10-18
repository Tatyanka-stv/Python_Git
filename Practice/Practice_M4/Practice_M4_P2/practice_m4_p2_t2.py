numbers = []
while True:
    user_number = input("Введіть ціле число (або 'q' для завершения вводу): ")
    if user_number.lower() == 'q':
        break
    try:
        number = int(user_number)
        numbers.append(number)
    except ValueError:
        print("Некоректне введення даних. Введіть ціле число або 'q' для завершення вводу.")

try:
    target_number = int(input('Введіть число, яке потрібно знайти: '))
    #occurrences = count_occurrences(numbers, target_number)
    count = 0
    for num in numbers:
        if num == target_number:
            count = count +  1
    print('Число '+str(target_number)+' зустрічається у списку '+str(count)+' раз.')
except ValueError:
    print("Некоректне введення даних. Введіть ціле число.")