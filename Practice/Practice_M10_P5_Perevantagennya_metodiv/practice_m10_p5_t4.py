class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def get_day(self):
        return self.day

    def set_day(self, day):
        self.day = day

    def get_month(self):
        return self.month

    def set_month(self, month):
        self.month = month

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year


    @classmethod
    def input_date(cls):
        while True:
            try:
                day = int(input('Введіть день (1-31): '))
                month = int(input('Введіть місяць (1-12): '))
                year = int(input('Введіть рік: '))

                if (1 <= day <= 31) and (1 <= month <= 12) and (year >= 0):
                    return cls(day, month, year)
                else:
                    print('Введена некоректна дата. Спробуйте ще раз.')
            except ValueError:
                print('Некоректне введення. Введіть вірні числа.')


    def show_date(self):
        if  (self.day is not None) and (self.month is not None) and (self.year is not None) :
            print(str(self.day)+'/'+str(self.month) +'/'+str(self.year))   
            
        else:
            print('Вивести на екран дату неможливо.')

    def __sub__(self, other_date):
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days1 = self.day
        for i in range(1, self.month):
            days1 = days1 + days_in_month[i]
        days1 = days1+ self.year * 365

        days2 = other_date.day
        for i in range(1, other_date.month):
            days2 = days2 + days_in_month[i]
        days2 = days2 + other_date.year * 365

        return abs(days1 - days2)

    def __add__(self, days_to_add): # lдодаємо до дати кількість днів
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days = self.day + days_to_add
        month = self.month
        year = self.year

        while days > days_in_month[month]:
            if month == 2 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                days_in_month[2] = 29  # Високосний рік
            else:
                days_in_month[2] = 28  # Не високосний рік

            days = days - days_in_month[month]
            month = month + 1

            if month > 12:
                month = 1
                year = year + 1

        return Date(days, month, year)

    def __str__(self):
        return str(self.day) + '/' + str(self.month) + '/' + str(self.year)


date1 = Date(1, 1, 2023)
date2 = Date(1, 1, 2022)

difference = date1 - date2
print('Виводимо різницю між 2ма встановленими датами: ')
print('Різниця дат між ' +str(date1) + ' та ' + str(date2) + ' складає ' + str(difference) + ' днів.')

date3 = Date(0, 0, 0)
date3 = Date.input_date()
date3.show_date()

while True:
    try:
        add_number_days = int(input('Введіть кількість днів, на яку бажаєте збільшити дату:'))

        if add_number_days >= 0:
            new_date = date3 + add_number_days
            print('Збільшена дата: ' + str(new_date))
            break
        else:
            print("Ви ввели від'ємне число. Введіть число >=0. ")
    except ValueError:
        print('Некоректне введення. Введіть вірні числа.')

