print('Розяснення до задачі:')
print('Відбувається введення чисел доки не введемо число 7')

while True:
     input_number = float(input('Введіть число: '))
     if input_number != 7:
         total_summa = 0
         max_number = input_number
         min_number = input_number
         while True:
             input_number = float(input('Введіть число: '))
             if input_number == 7:
                 print('Good bye!')
                 break
             else:
                 total_summa = total_summa + input_number
                 max_number = max(max_number,input_number)
                 min_number =min(min_number,input_number)

         print('Сума введених чисел, які не дорівнюють 7:', total_summa)
         print("Максимальне число  серед введених чисел, які не дорівнюють 7:", max_number)
         print("Мінімальне число серед введених чисел, які не дорівнюють 7:", min_number)
     else:
         print('Good bye!')
         break