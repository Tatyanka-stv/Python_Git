m=float(input('Введіть кількість метрів: '))
if m<0:
    print('Метри не можить бути відємними ')
else:
    #import math
    #if m-math.trunc(m)!=0: #перевіряємо чи введене число  є дійсним
    # print('Ви ввели не цілу кількість метрів')
    #else:
     #m=int(m)
     print(str(m)+' метрів  = '+str(int(round(m*10,0)))+' дециметрів')
     print(str(m)+' метрів  = '+str(int(round(m*100,0)))+' сантиметрів')
     print(str(m)+' метрів  = '+str(int(round(m*1000,0)))+' міліметрів')
     print(str(m)+' метрів  = '+str(round(m/1609.34,3))+' милі ')