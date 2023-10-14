try:
    user_num = int(input('Введіть число: '))

    while True:
        #menu
        print('Меню:')
        print('1. Визначити кількість цифр у числі')
        print('2. Порахувати суму цифр')
        print('3. Порахувати середнє арифметичне значення цифр')
        print('4. Порахувати кількість нулів у числі')
        print('5. Вихід')


        choice = int(input('Оберіть опцію: '))

        if choice == 1:
            count_digits = len(str(user_num))
            print('Кількість  цифр у числі : ', count_digits)

        elif choice == 2:
            sum_of_digits = 0
            for digit in str(user_num):
                sum_of_digits = sum_of_digits + int(digit)
            print('Сума цифр числа: ', sum_of_digits)

        elif choice == 3:
            avg_of_digits = 0
            digits = 0
            sum_of_digits = 0
            number_of_digits = 0
            for digit in str(user_num):
                digits = int(digit)
                sum_of_digits = sum_of_digits + digits
                number_of_digits = number_of_digits + 1
            avg_of_digits = sum_of_digits/number_of_digits    
            print('Середнє арифметичне значення усіх цифр числа: ', round(avg_of_digits,4))

        elif choice == 4:
            count_zeros = str(user_num).count('0')
            print('Кількість нулей у числі: ', count_zeros)

        elif choice == 5:
            print('Вихід з програми.')
            break

        else:
            print('Некоректний вибір. Спробуйте ще раз.')

except ValueError:
    print('Помилка! Введіть ціле число.')