def show_summa(a,b):
    if a>b:
         print('Перше число більше ніж друге число. Сформувати діапазон неможливо.') 
    else: 
        if a!=b: 
            i = int(round(a,0))
            summa = 0
            while i>= a and i<=b:
                print(i, end=' ')
                summa = summa + i 
                i = i +1      
        else:
            print('Перше число дорівнює другому числу. Вивести числа неможливо, так як немає проміжку.') 
    return summa

print('Введіть верхню та нижню межі діапазону чисел:')
a=float(input('a=')) 
b=float(input('b='))  
result = show_summa(a,b) 
print('\nСума чисел в завданом діапазоні дорівнює ', result)              