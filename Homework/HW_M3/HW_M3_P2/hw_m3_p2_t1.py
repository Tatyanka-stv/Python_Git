start_num = float(input('Введіть початкове число: '))
end_num = float(input('Введіть кінцеве число: '))
import math
if start_num-math.trunc(abs(start_num))==0.0 and end_num-math.trunc(abs(end_num))==0.0:
    start_num=int(start_num)
    end_num=int(end_num)
    if start_num>end_num:
        print('Стартове число більше за кінцеве число. Створити діапазон для виконання задачі неможливо.')
    elif start_num==end_num:
         print('Стартове число дорівнює кінцевому числу. Створити діапазон для виконання задачі неможливо.')
    else:
        sum_even=0 #сума парних чисел
        sum_odd=0 #сума непарних чисел
        sum_multiple_of_9=0  #сума чисел, кратних 9
        count_even=0 #кількість парних чисел
        count_odd=0 #кількість непарних чисел
        count_multiple_of_9=0 #кілкість чисел, кратних 9

        for i in range(start_num, end_num + 1,1):
            if i % 2 == 0:
                sum_even=sum_even + i
                count_even= count_even + 1
            else:
                sum_odd=sum_odd + i
                count_odd=count_odd + 1

            if i % 9 == 0:
                sum_multiple_of_9=sum_multiple_of_9 + i
                count_multiple_of_9=count_multiple_of_9 + 1

        if count_even > 0:
             avg_even = sum_even / count_even
        else:
             avg_even = 0

        if count_odd > 0:
             avg_odd = sum_odd / count_odd
        else:
             avg_odd = 0

        if count_multiple_of_9 > 0:
             avg_multiple_of_9 = sum_multiple_of_9 / count_multiple_of_9
        else:
             avg_multiple_of_9 = 0
   
        print("Сума парних чисел:", sum_even)
        print("Середнє арифметичне значення парних чисел:", avg_even)
        print("Сума непарних чисел:", sum_odd)
        print("Середнє арифметичне значення непарних чисел:", avg_odd)
        print("Сума чисел, які кратні 9:", sum_multiple_of_9)
        print("Середнє арифметичне значення чисел, які кратні 9:", avg_multiple_of_9)
else:
    print('Ви ввели невірні числа. ')     

