n=float(input('Введіть будь-яке ціле число: '))
import math
if n-math.trunc(abs(n))==0.0:
    n=int(n)
    if n!=0:
        if n%2==0:
         print(n,'Even number')
        else:
         print(n,'Odd number')
    else:
         print('Ви ввели не ціле число, а 0')
else:         
 print('Ви ввели не ціле, а дійсне число.')
       
