class Passport:
    def __init__(self, first_name, last_name, birth_date, passport_number):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.passport_number = passport_number

    def input_data(self):
        self.first_name = input("Введіть ім'я: ")
        self.last_name = input('Введіть прізвище: ')
        self.birth_date = input('Введите дату народження: ')
        self.passport_number = input('Введите номер звичайного паспорту: ')
    
    def show_info(self):
        print("Ім'я: " + self.first_name)
        print('Прізвище: ' +self.last_name)
        print('Дата народження: ' + self.birth_date)
        print('Номер паспорту: ' + self.passport_number)


class ForeignPassport(Passport):
    def __init__(self, first_name, last_name, birth_date, passport_number, foreign_passport_number, visas=[]):
        super().__init__(first_name, last_name, birth_date, passport_number)
        self.foreign_passport_number = foreign_passport_number
        self.visas = visas

    def add_visa(self, visa_info):
        self.visas.append(visa_info)

    def input_data(self):
        super().input_data()
        self.foreign_passport_number = input('Введіть номер закордонного паспорту: ')
        num_of_visas = int(input('Введіть кількість віз: '))
        self.visas = []
        for i in range(num_of_visas):
            visa_info = input('Введіть інформацію про візу: ' + str(i + 1) + ': ')
            self.visas.append(visa_info)
   
    def show_info(self):
        super().show_info()
        print('Номер закордонного паспорта: ' + self.foreign_passport_number)
        print('Візи:')
        for visa in self.visas:
            print(visa)

print('Вводіть інформацію для звичайного паспорта: ')
passport = Passport('', '', '', '')
passport.input_data()

print('\nВводіть інформацію для закордонного паспорта: ')
foreign_passport = ForeignPassport('', '', '', '', '', [])
foreign_passport.input_data()

foreign_passport.add_visa('Германія')

print('\nВиводимо інформацію про паспорти: ')
print('Звичайний паспорт: ')
passport.show_info()
print('\nЗакордонний паспорт:')
foreign_passport.show_info()