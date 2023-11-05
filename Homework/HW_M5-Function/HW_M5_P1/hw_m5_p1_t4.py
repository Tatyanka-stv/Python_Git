def find_minimum(a, b, c, d, e):
    min_number = min(a, b, c, d, e)
    return min_number

number1 = float(input('Введіть перше число: '))
number2 = float(input('Введіть друге число: '))
number3 = float(input('Введіть третє число: '))
number4 = float(input('Введіть четверте число: '))
number5 = float(input('Введіть п'"'"'яте число: '))

min_result = find_minimum(number1, number2, number3, number4, number5)
print("Мінімальне число із п""'""яти введених чисел: ", min_result)