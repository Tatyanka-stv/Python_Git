def maxof4digitals(a,b,c,d):
    return max(a, b, c, d)

print('Введіть 4 числа:')
a=float(input('a=')) 
b=float(input('b='))  
c=float(input('c=')) 
d=float(input('d='))  
result = maxof4digitals(a,b,c,d)
print('Максимальне число: ', result) 