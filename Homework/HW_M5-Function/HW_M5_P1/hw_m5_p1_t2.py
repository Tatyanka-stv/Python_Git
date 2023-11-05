def show_even_numbers(start_number, end_number):
    start_number = int(start_number)
    end_number = int(end_number)
    if start_number > end_number:
        print("Числа введено невірно!. Перше число повинно бути менше або дорівнювати другому числу.")
        return
    else:
        for number in range(start_number, end_number + 1,1):
            if number % 2 == 0:
                print(number, end=' ')

import math

start_number = float(input("Введіть перше число: "))
end_number = float(input("Введіть друге число: "))

show_even_numbers(start_number, end_number)