r=float(input('Введіть розмір файла у Гігабайтах: '))
if r>0:
    v=int(input('Введіть швідкість завантаження файлів у бітах в секунду: '))
    if v>0:
        import math
        print('Переводимо Гігабайт в біти: ',math.trunc(round(r*(2**33),0)))
        _seconds=math.trunc(round((r*(2**33))/(v*(2**20)))) #розраховуємо час завантаження у секундах
        #print('час у секундах= ',math.trunc(round(t,0))) #перевірочний рядок розрахунку скільки секунд йде завантаження
        print('Оберіть номер операції, що потрібно порахувати: ') 
        print('1: час завантаження у годинах: ')  
        print('2: час завантаження у хвилинах: ')
        print('3: час завантаження у секундах: ')
        n=float(input())
        if n-math.trunc(abs(n))==0.0:
            n=int(n)
            if n==1:
              _hours=math.trunc(_seconds/3600) #скільки цілих годин пройшло
              _minutes=math.trunc(_seconds/60)-_hours*60 #скільки хвилин, які не увійшли у цілі години, що пройшли з початку доби
              _seconds=_seconds-math.trunc(_seconds/60)*60 #скільки секунд, які не увійшли у цілі години та цілі хвилини, що пройшли с початку доби
              print('Файл розміром '+str(r)+' Гігабайт буде завантажуватися '+str(_hours)+' годин(а) '+str(_minutes)+' хвилин(а) '+str(_seconds)+' секунд(а)')
            
            elif n==2:
             #підраховуємо скільки секунд, хвилин пройшло с початку доби
             _minutes=math.trunc(_seconds/60) #скільки цілих хвилин, що пройшли з початку доби
             _seconds=_seconds-math.trunc(_seconds/60)*60 #скільки залишилося секунд, які не увійшли у цілі хвилини, що пройшли с початку доби
             print('Файл розміром '+str(r)+' Гігабайт буде завантажуватися '+str(_minutes)+' хвилин(а) '+str(_seconds)+' секунд(а)')
            
            elif n==3:
              print('Файл розміром '+str(r)+' Гігабайт буде завантажуватися '+str(math.trunc(round(_seconds,0)))+ ' секунд(а)')                  
            
            else: 
                print('Введено невірний номер операції')  
        else:
            print('Введено невірний номер операції')  
    else:
        print('Введено невірна швидкість завантаження')               
else:
    print('Введено невірний розмір файла')         