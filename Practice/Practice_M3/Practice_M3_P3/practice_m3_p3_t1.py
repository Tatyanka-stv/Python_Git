number = float(input('Введіть число: '))
import math
if abs(number)-int(abs(number))==0:
     number=int(number)
     if number <= 0:
         print('Число введено невірно. Число повинно бути додатнім.')
     else:
         print('Виводимо таблицю множення для числа '+str(number)+' : ')
         for i in range(1, 11):
             print(str(number)+'*'+str(i)+'='+str(number*i))
else:
    print('Число введено невірно. Воно є дійсним.')