print('Обраховуємо площу трикутника: ')
c=float(input('Введіть основу трикутника: '))
if c==0:
    print('Основа трикутника не може дорівнювати 0')
else:
    if c<0:
     print('Основа трикутника не може бути менше 0')   
    else:
        h=float(input('Введіть висота трикутника: '))
        if h==0:
             print('Висота трикутника не може дорівнювати 0')
        else: 
            if h<0:
             print('Висота трикутника не може бути менше 0')  
            else:
                print('Площа трикутника дорівнює: '+str(round(c*h/2,2)))