def pad_string_with_spaces(input_string, desired_length): #функцыя, которая будет добавлять пробелы до указанной длины строки
    # Проверяем текущую длину строки
    current_length = len(input_string)
    
    # Если строка уже достаточно длинная, возвращаем её без изменений
    if current_length >= desired_length:
        return input_string
    
    # Иначе добавляем пробелы до нужной длины
    padding_spaces = ' ' * (desired_length - current_length)
    padded_string = input_string + padding_spaces
    return padded_string


print('Виводимо таблицю множення в діапазоні, який вказує користувач:')
start_num = float(input('Введіть перше число: '))
end_num = float(input('Введіть друге число: '))
import math
if abs(start_num)-int(abs(start_num))==0 and abs(end_num)-int(abs(end_num))==0:
     start_num=int(start_num)
     end_num=int(end_num)
     if (start_num <= 0 and end_num <=0) or (start_num>=0 and end_num<=0) or (start_num<=0 and end_num>=0):
         print('Числа введені невірно. Числа не можуть бути відємними або дорівнювати 0.')
     if start_num>0 and end_num>0:
         if start_num<=end_num:
             for i in range(start_num, end_num+1):
                for j in range(start_num, end_num+1):
                    original_string = str(j)+'*'+str(i)+'='+str(i * j)
                    max_original_string=str(max(start_num,end_num))+'*'+str(max(start_num,end_num))+'='+str(start_num * end_num) #максимальная строка которая может быть сформирована из введенного диапазона например 10*10=100
                    lenght_max_original_string=len(max_original_string)
                    desired_length = lenght_max_original_string+2 #длина строки которая должна быть с учетом дополненных пробелов, мы сами ее фиксируем
                    padded_string = pad_string_with_spaces(original_string, desired_length)
                    print(padded_string,end=' ')
                print(end='\n')
     if start_num>end_num and (end_num>0):
             for i in range(end_num, start_num+1,):
                for j in range(end_num, start_num+1,):
                    original_string = str(j)+'*'+str(i)+'='+str(i * j)
                    max_original_string=str(max(start_num,end_num))+'*'+str(max(start_num,end_num))+'='+str(start_num * end_num) #максимальная строка которая может быть сформирована из введенного диапазона например 10*10=100
                    lenght_max_original_string=len(max_original_string)
                    desired_length = lenght_max_original_string+2 #длина строки которая должна быть с учетом дополненных пробелов, мы сами ее фиксируем
                    padded_string = pad_string_with_spaces(original_string, desired_length)
                    print(padded_string,end=' ')
                print(end='\n')
else:
    print('Числа введені невірно. Вони є дійсними.')

