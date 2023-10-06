_month=float(input('Введіть номер місяця року: '))
import math
if _month-math.trunc(abs(_month))==0.0:
    _month=int(_month)
    if _month<=0 or _month>12:
     print('Невірно введений номер місяця року.')
    else:
     if _month==1: print('Місяць року - січень')
     if _month==2: print('Місяць року - лютий')
     if _month==3: print('Місяць року - березень')
     if _month==4: print('Місяць року - квітень')
     if _month==5: print('Місяць року - травень')
     if _month==6: print('Місяць року - червень')
     if _month==7: print('Місяць року - липень')
     if _month==8: print('Місяць року - серпень')
     if _month==9: print('Місяць року - вересень')
     if _month==10: print('Місяць року - жовтень')
     if _month==11: print('Місяць року - листопад')
     if _month==12: print('Місяць року - грудень')
else: 
    print('Невірно введений номер місяця року.')   