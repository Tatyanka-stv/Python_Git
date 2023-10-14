x = float(input('Введіть ціле число x: '))
y = float(input('Введіть ціле число y: '))
import math
if abs(x)-math.trunc(abs(x))==0.0 and abs(y)-math.trunc(abs(y))==0.0:
     x=int(x)
     y=int(y)
     if x==0 and y<=0:
          print('Результат не визначений.')
     elif x !=0:
         result = x ** y
         print('Результат: '+str(x)+' в степени '+str(y)+' = '+str(round(result,3)))
else:   
     print('Ви ввели не цілі числа.')  
