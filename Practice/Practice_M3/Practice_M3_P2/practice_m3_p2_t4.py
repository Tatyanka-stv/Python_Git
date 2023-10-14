length = float(input('Введіть довжину лінії: '))
if abs(length)-int(abs(length))==0 :
     length=int(length)
     if length < 0:
         print('Довжина не може бути відємною.')
     elif length==0:
             print('Довжина не може дорівнювати 0.') 
     else:
         symbol = input('Введіть символ для заповнення лінії: ')
         print('Виводимо лінію із '+symbol+' у кількості '+str(length)+' символів.')
         print(symbol*length)
else:
    print('Довжина введена невірно. Введене число є дійсним.')