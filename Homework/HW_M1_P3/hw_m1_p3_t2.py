a=int(input('Введіть ціле 4-значне число: '))
import math
if abs(a)>=10000 or math.trunc(a/1000)==0:
     print('Ви ввели не 4-значне число.')
else:
     if a<0:
        a=abs(a)
     b=math.trunc(a/1000)#перша цифра
     c=math.trunc((a-b*1000)/100) #друга цифра
     d=math.trunc((a-b*1000-c*100)/10) #третя цифра
     e=a-b*1000-c*100-d*10 #четверта цифра
     print('Цифри, з яких складається введене 4-значне число '+str(a)+' : '+str(b)+' '+str(c)+ ' '+str(d)+' '+str(e))
     print('Добуток цифр дорівнює: ' +str(b)+' * '+str(c)+ ' * '+str(d)+' * '+str(e)+' = ', b*c*d*e)