from datetime import datetime
import math

def is_year_high(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def days_between_dates(date1, date2):
    date_format = "%Y-%m-%d"
    date1 = datetime.strptime(date1, date_format)
    date2 = datetime.strptime(date2, date_format)
    delta = abs(date2 - date1)
    return delta.days


print('Визначаємо різницю між заданими датами. Введіть дати у вигляді 2023-10-01')
date_str1 =input('Введіть першу дату: ')
date_str2 = input('Введіть другу дату: ')
print('Різница у днях між '+date_str1 + ' та  '+ date_str2 + ': ' + str(days_between_dates(date_str1, date_str2)) + ' днів.')

print('Визначаємо чи є введений рік високосним.')
year = int(input('Введіть рік: '))
if is_year_high(year):
    print(str(year) + ' - високосний рік')
else:
    print(str(year) + ' - не високосний рік')