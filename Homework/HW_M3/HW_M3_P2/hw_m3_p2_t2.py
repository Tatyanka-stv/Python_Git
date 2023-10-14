length_of_line = float(input("Введіть довжину лінії: "))
import math
if length_of_line-math.trunc(abs(length_of_line))==0.0:
     length_of_line=int(length_of_line)
     if length_of_line <= 0:
         print('Введене число не може бути длиною рядка. Побудувати лінію неможливо.')
     else:
         symbol_to_display = input("Введіть символ для заповнення лінії: ")
         for i in range(length_of_line):
             print(symbol_to_display)
else:
     print('Введене число є дійсним і не може бути длиною рядка. Побудувати лінію неможливо.')