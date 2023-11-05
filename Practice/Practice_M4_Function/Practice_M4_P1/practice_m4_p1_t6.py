def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    #прості числа мають вигляд 6k ± 1 (де k - це ціле число)

    '''умова перевірки чи є число number простим: 
    чи воно ділиться націло на будь-яке число i, де i знаходиться в діапазоні від 2 до квадратного кореня з number.'''
    
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

try:
    number = int(input('Введіть число: '))
    if is_prime(number):
        print(str(number)+' - просте число.')
    else:
        print(str(number)+' - не є простим числом.')
except:
    print('Введене число не є цілим. Перевірити чи є число простим неможливо.')