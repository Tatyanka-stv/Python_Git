a=int(input('Input start number: '))
b=int(input('Input end number: '))
if a==0:
    a=a+1 
if a%2==1:
    a=a+1
if a>0 and b>0 and a<=b:
    
    for i in range(a,b+1,2):
        print(i, end=' ')
else:
    print('Input number are wrong')               
