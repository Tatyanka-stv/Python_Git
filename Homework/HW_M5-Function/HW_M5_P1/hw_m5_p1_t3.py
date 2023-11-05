def draw_square(side, symbol, fill_operation):
    for i in range(side):
        for j in range(side):
            if fill_operation == 'true' or fill_operation == 't' or i == 0 or i == side - 1 or j == 0 or j == side - 1:
                print(symbol, end=' ')
            else:
                print(' ', end=' ')
        print()

import math
side = float(input("Введіть довжину сторони квадрата: "))
if abs(side)-int(abs(side)) == 0:
    side = int(side)
    if side > 0:
        symbol = input("Введите символ для заполнения: ")
        fill_operation = input("Заповнити квадрат? (True/False): ")
        fill_operation = fill_operation.lower() 
        draw_square(side, symbol, fill_operation)
    else:
        if side < 0:
            print('Довжина сторони квадрата не може бути відємною. Побудувати квадрат неможливо.')
        else:        
            print('Довжина сторони квадрата не може дорівнювати 0. Побудувати квадрат неможливо.')
else:
    print('Ви ввели не ціле число.')            