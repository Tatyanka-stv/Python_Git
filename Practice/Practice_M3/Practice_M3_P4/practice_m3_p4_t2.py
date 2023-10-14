side_length = float(input('Введіть довжину сторони прямокутника: '))
side_width = float(input('Введіть  ширину сторони прямокутника: '))
import math
if abs(side_length)-int(abs(side_length))==0 and abs(side_width)-int(abs(side_width))==0:
     side_length=int(side_length)
     side_width=int(side_width)
     if side_length <= 0 or side_width <=0:
         print('Числа введено невірно. Числа повинні бути додатніми.')
     else:
         for i in range(side_length):
             print('*  ' * side_width)
else:
    print('Числі введено невірно. Вони є дійсними.')