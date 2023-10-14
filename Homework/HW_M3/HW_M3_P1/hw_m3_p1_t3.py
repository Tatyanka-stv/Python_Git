a=float(input('Input start number > 0 : '))
b=float(input('Input end number > 0 : '))
import math
if a==b: 
     print('Input number are wrong, because start number = end number.') 
else: 
     if a-math.trunc(abs(a))==0.0 and b-math.trunc(abs(b))==0.0: #перевіряємо чи введені числа є дійсними, 
         #якщо дійсні-пишемо про помилку, якщо цілі, то перетвороємо тип float на itn без крапки після цілої частини для використання у функції range
         a=int(a)
         b=int(b)
         if  a>=0 and b>=0:    
             if a>b: 
                 print('Input number are wrong, because start number > end number.')
             else:        
                 if a<b:
                     for i in range(a,b+1,1):
                         if a==0:
                             a=1
                         else:
                             if i%3==0: print('Fizz', end=' ')
                             if i%5==0: print('Buzz', end=' ')
                             if i%3!=0 and i%5!=0: print(i, end=' ')                    
         else: 
             print('Input number is wrong')                      
     else:
         print('Input number are wrong, because input number is float')