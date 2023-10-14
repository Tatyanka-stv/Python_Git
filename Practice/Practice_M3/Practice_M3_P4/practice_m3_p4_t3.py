side_length = float(input('Введіть довжину сторони квадрату: '))
import math
if abs(side_length)-int(abs(side_length))==0:
     side_length=int(side_length)
     if side_length <= 0:
         print('Число введено невірно. Число повинно бути додатнім.')
     else:
         print('*' * side_length) #малюємо верхню сторону квадрату
         for i in range(side_length - 2):
             print('*' + ' ' * (side_length - 2) + '*') #малюємо бокові сторони квадрату
         print('*' * side_length) #малюємо нижню сторону квадрату     
else:
    print('Число введено невірно. Воно є дійсним.')