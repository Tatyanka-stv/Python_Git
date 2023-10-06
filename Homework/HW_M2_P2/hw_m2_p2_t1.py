_day=float(input('Введіть номер дня тижня: '))
import math
if _day-math.trunc(abs(_day))==0.0:
    _day=int(_day)
    if _day<=0 or _day>7:
     print('Невірно введений номер дня тижня ')
    else:
     if _day==1: print('День тижня - понеділок')
     if _day==2: print('День тижня - вівторок')
     if _day==3: print('День тижня - середа')
     if _day==4: print('День тижня - четвер')
     if _day==5: print('День тижня - пятниця')
     if _day==6: print('День тижня - субота')
     if _day==7: print('День тижня - неділя')
else: 
    print('Невірно введений номер дня тижня ')   