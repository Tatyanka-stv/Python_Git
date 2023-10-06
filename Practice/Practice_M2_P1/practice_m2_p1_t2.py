n=float(input('Введіть будь-яке ціле число: '))
import math
if n-math.trunc(abs(n))==0.0:
    n=int(n)
    if n!=0:
        if n%7==0:
              print(n,' Number is multiple 7')
        else:
             print(n,' Number is not multiple 7')
    else:
         print('Ви ввели 0, перевірити дане число на кратність 7 неможливо')       
else:         
 print('Ви ввели не ціле, а дійсне число.')