def power(base, exponent):
    if exponent < 0:
        exponent = abs(exponent)
    if exponent == 0:
        return 1 
    else:
        return base * power(base, exponent - 1) 
  
try:
    print('Знаходимо ступінь числа.')
    base = int(input(('Введіть число: '))) 
    exponent = int(input(('Введіть ступінь: ')))
    if exponent >=0:
        result = power(base, exponent)
        print(str(base)+' ** '+str(exponent)+' = ',result)
    else:
        result = power(base, exponent)
        print(str(base)+' ** ('+str(exponent)+') =  -1/',result)

except:
    print('Ви ввели не ціле число.')       