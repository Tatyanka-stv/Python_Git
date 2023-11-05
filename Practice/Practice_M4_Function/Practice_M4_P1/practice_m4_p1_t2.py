def show_neparny(a,b):
     if a>b:
         print('Перше число більше ніж друге число. Вивести числа неможливо.') 
     else: 
          if a!=b: 
               i = int(a)+1
               while i>= a and i<=b:
                    if i % 2 !=0:
                         print(i, end=' ')
                         i = i + 1
                    else:
                         i = i +1     
          else:
               print('Перше число дорівнює другому числу. Вивести числа неможливо, так як немає проміжку.') 
     
print('Введіть 2 числа:')
a=float(input('a=')) 
b=float(input('b='))  
show_neparny(a,b)               