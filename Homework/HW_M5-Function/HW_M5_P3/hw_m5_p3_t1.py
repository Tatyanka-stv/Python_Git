def NOD_recursive(a, b):
    if b == 0:
        return a
    else:
        return NOD_recursive(b, a % b)

try:
    number1 = int(input('Введіть перше число: '))
    number2 = int(input('Введіть друге число: '))
    result = NOD_recursive(number1, number2)
    print('Найбільший спільний дільник чисел '+str(number1)+ ' та '+ str(number2)+' дорівнює ' + str(result)) 
except:
    print('Ви ввели не цілі числа.')           