def draw_chessboard(cell_size):
    for i in range(1,8+1): #розмір дошки 8*8 клітинок
        if i%2==0: #перевіряємо кратність кратність рядків і: якщо 1,3,5,7 то починаємо з *, якщо 2,4,6,8-почнаємо з -
            for j in range(1 * cell_size,9*cell_size):
                if (int(j / cell_size)) % 2 == 0: #ця умова перевіряє коли саме треба змінювати друк * на -
                    print('*', end='')
                else:
                    print('-', end='')
            print()
        else:    
            for j in range(1 * cell_size,9*cell_size):
                if (int(j / cell_size)) % 2 == 0:
                    print('-', end='')
                else:
                    print('*', end='')
            print()
try:
    cell_size = int(input('Введіть розмір клітинки (скільки символів має бути у клітинці): '))
    
    if cell_size >0:
        draw_chessboard(cell_size)
    else:
        print('Розмір клітинки не може бути відємним або дорівнювати 0.')    

except ValueError:
    print('Помилка! Введіть ціле число.')


    