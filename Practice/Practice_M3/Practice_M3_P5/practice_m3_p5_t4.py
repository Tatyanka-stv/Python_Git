try:
    rows = int(input('Введіть кількість рядків у ромбі: '))
    if rows <=0:
        print('Введене число не є додатнім.')
    if rows ==1:
        print('Побудувати ромб неможливо.')
    else:
        for i in range(1, rows + 1):
            print(' ' * (rows - i) + '*' * (2 * i - 1))

        for i in range(rows - 1, 0, -1):
            print(' ' * (rows - i) + '*' * (2 * i - 1))

except ValueError:
    print('Помилка! Введіть ціле число для кількості рядків.')