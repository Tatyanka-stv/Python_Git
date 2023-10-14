check=True
while check==True:
    start = float(input('Введіть початок діапазону: '))
    end = float(input('Введіть кінець діапазону: '))

    import math
    if abs(start)-int(abs(start))==0 and abs(end)-int(abs(end))==0:
        start=int(start)
        end=int(end)
        if start >= end:
            print('Помилка! Неправильно введені межі діапазона.')
        else:
            user_number = float(input('Введіть ціле число: '))
            if abs(user_number)-int(abs(user_number))==0:
                user_number=int(user_number)
                while user_number < start or user_number > end:
                    print('Число не входить в діапазон.')
                    user_number = float(input('Введіть число: '))
                if abs(user_number)-int(abs(user_number))==0:
                    user_number=int(user_number)
                    for i in range(start, end + 1):
                        if i == user_number:
                            print('!'+str(i)+'!', end=' ')
                        else:
                            print(i, end=' ')   
                    check=False                                 
                else:
                    print('Ви ввели не ціле число для перевірки.')    
            else:
                print('Ви ввели не ціле число для перевірки.')
    else:
        print('Ви ввели невірні числа для діапазону.')      
print('\nЗавдання виконано!')          
