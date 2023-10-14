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
                 print('1. Output all the numbers in the range:') 
                 for i in range(a,b+1,1):
                     print(i, end=' ')
                 print('\n')      
                 print('2. Output all numbers in a range in descending order:') 
                 for i in range(b,a-1,-1):
                     print(i, end=' ') 
                 print('\n')      
                 print('3. All numbers are multiples of 7:') 
                 if b<7 and a<b:
                     print('There are no multiples of 7 because end numder < 7')   
                 else:          
                     if a<b:
                         for i in range(a,b+1,1):
                             if a==0:
                                 a=1
                             else:
                                 if i%7==0:
                                     print(i, end=' ')  
                 print('\n')      
                 print('4. Count of numbers that are multiples of 5: ') 
                 if b<5 and a<b:
                     print('There are no multiples of 5 because end numder < 5')   
                 else:
                     if a<b:
                         n=0
                         for i in range(a,b+1,1):
                             if a==0:
                                 a=1
                             else:
                                 if i%5==0:
                                     n=n+1   
                         print('N=',n) 
                     
         else: 
             print('Input number is wrong')                   
     else:
         print('Input number are wrong, because input number is float')