def lucky_number(number):
    if len(str(number)) == 6:
        first_part = number // 1000
        second_part = number % 1000   
        sum_first_part = sum(int(digit) for digit in str(first_part))
        sum_second_part = sum(int(digit) for digit in str(second_part))
        return sum_first_part == sum_second_part
    else:
        print('Введене число не є 6-значним.')
        return False

try:
    print('Перевіряємо чи є число '+'"'+'щасливим'+'"'+':')
    number = int(input('Введіть 6-значне число: '))
    print('Відповідь: ', lucky_number(number))
except:
    print('Введене число не є '+'"'+'щасливим'+'"'+'.')