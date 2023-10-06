print('Введіть кількість годин від 0 до 24:')
h=float(input())
if h>=0 and h<=24:
    if (h>=0 and h<6) or h==24:
        print('Good Night')
    elif h>=6 and h<13:
        print('Good Morning') 
    elif h>=13 and h<17:
        print('Good Day')  
    elif h>=17 and h<24:
        print('Good Evening')         
else:
    print('Ви ввели неправильно години')        