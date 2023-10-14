num = float(input('Введіть довжину лінії: '))
if abs(num)-int(abs(num))==0 :
     num=int(num)
     if num < 0:
         print('Довжина не може бути відємною.')
     elif num==0:
             print('Довжина не може дорівнювати 0.') 
     else:
         print('Виводимо лінію із * у кількості '+str(num)+' символів.')
         print('*'*num)
else:
    print('Довжина введена невірно. Введене число є дійсним.')