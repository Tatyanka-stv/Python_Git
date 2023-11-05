def summa(a, b):
    if a > b:
         return 0
    else:
         return a + summa(a + 1, b)

try:
    a = int(input("Введіть a: "))
    b = int(input("Введіть b: "))   
    result = summa(a, b)
    print('Сума чисел від '+str(a)+' до '+str(b)+' дорівнює ',result)
except:
    print('Ви ввели не ціле число.')    