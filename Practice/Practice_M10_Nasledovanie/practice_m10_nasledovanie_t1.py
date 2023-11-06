class Human:
    def __init__(self):
        self.full_name = ''
        self.birth_date = ''
        self.contact_phone = ''
        self.city = ''
        self.country = ''
        self.address = ''

    def set_full_name(self, full_name):
        self.full_name = full_name

    def set_birth_date(self, birth_date):
        self.birth_date = birth_date

    def set_contact_phone(self, contact_phone):
        self.contact_phone = contact_phone

    def set_city(self, city):
        self.city = city

    def set_country(self, country):
        self.country = country

    def set_address(self, address):
        self.address = address

    def input_data(self):
        self.full_name = input("Введіть прізвище, імя, по-батькові: ")
        self.birth_date = input("Введіть дату народження: ")
        self.contact_phone = input("Введіть контактний номер телефона: ")
        self.city = input("Введіть місто: ")
        self.country = input("Введіть країну: ")
        self.address = input("Введіть адресу: ")

    def show_info_of_person(self):
        print('Прізвище, імя, по-батькові:', self.full_name)
        print('Дата народження:', self.birth_date)
        print('Телефон:', self.contact_phone)
        print('Місто:', self.city)
        print('Країна:', self.country)
        print('Домашня адреса:', self.address)

class Builder(Human):
    def __init__(self, full_name, birth_date, contact_phone, city, country, address, qualification):
        super().__init__()
        self.full_name = full_name
        self.birth_date = birth_date
        self.contact_phone = contact_phone
        self.city = city
        self.country = country
        self.address = address
        self.qualification = qualification

    def input_data(self):
        super().input_data()
        self.qualification = input('Введіть кваліфікацію будівника: ')

    def show_info_of_builder(self):
        super().show_info_of_person()
        print('Кваліфікація будівника:', self.qualification)


class Sailor(Human):
    def __init__(self, full_name, birth_date, contact_phone, city, country, address, sea_experience):
        super().__init__()
        self.full_name = full_name
        self.birth_date = birth_date
        self.contact_phone = contact_phone
        self.city = city
        self.country = country
        self.address = address
        self.sea_experience = sea_experience

    def input_data(self):
        super().input_data()
        self.sea_experience = input('Введіть досвід у морі у роках: ')

    def show_info_of_sailor(self):
        super().show_info_of_person()
        print('Морський досвід, роки:', self.sea_experience)        

class Pilot(Human):
    def __init__(self, full_name, birth_date, contact_phone, city, country, address, flying_time):
        super().__init__()
        self.full_name = full_name
        self.birth_date = birth_date
        self.contact_phone = contact_phone
        self.city = city
        self.country = country
        self.address = address
        self.flying_time = flying_time

    def input_data(self):
            super().input_data()
            self.flying_time = input('Введіть кількість налітаних годин: ')

    def show_info_of_pilot(self):
        super().show_info_of_person()
        print('Налітано годин:', self.flying_time)     

# Створюємо обєкт класа Human
person1 = Human()
print('\n1. Інформація про 1у персону класу '"'"'Human'"'.\n")
person1.set_full_name('Іваненко Іван Іванович')
person1.set_birth_date('01.01.1980')
person1.set_contact_phone('+1234567890')
person1.set_city('Київ')
person1.set_country('Україна')
person1.set_address('вул. Мирна, буд. 1б кв. 2')
person1.show_info_of_person()

# Створюємо обєкт класа Human
print('\n2. Введіть інформація про 2у персону класу '"'"'Human'"'.\n")
person2 = Human()
person2.input_data()
print('\nВиводимо отриману інформацію:\n')
person2.show_info_of_person()

# Створюємо обєкт класа Builder
print('\n3. Інформація про персону класу '"'"'Builder'"'.\n")
builder1 = Builder('Петренко Петро Петрович', '02.02.1970', '+1234567', 'Львів', 'Україна', 'вул. Соборна, буд. 2', 'Прораб')
print('\nВиводимо отриману інформацію про персону класу '"'"'Builder'"'"'.\n')
builder1.show_info_of_builder()

# Створюємо обєкт класа Sailor
print('\n4. Введіть інформація про персону класу '"'"'Sailor'"'"'.\n')
sailor = Sailor('','','','','','',0)
sailor.input_data()
print('\nВиводимо отриману інформацію про персону класу '"'"'Sailor'"'.\n")
sailor.show_info_of_sailor()

# Створюємо обєкт класа Pilot
print('\n5. Інформація про персону класу '"'"'Pilot'"'.\n")
pilot = Pilot('Федоренко Федір Іванович', '01.02.1988', '+4563217', 'Харків', 'Україна', 'вул. Аерофлотська, буд. 4', '1000')
pilot.show_info_of_pilot()       