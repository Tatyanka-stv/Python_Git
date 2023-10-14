a=int(input('Input start number: '))
b=int(input('Input end number: '))
if a<b:
    for i in range(b,a-1,-1):
        print(i, end=' ')
       
else:
    for i in range(a, b-1, -1):
         print(i, end=' ')
    