class Human:
    number_of_people = 0 #лічильник для підрахунку кількості створених обєктів
    def __init__(self):
        self.full_name = ''
        self.birth_date = ''
        self.contact_phone = ''
        self.city = ''
        self.country = ''
        self.address = ''
        Human.number_of_people += 1 #збільшуємо лічильник на +1 при створенні окремого обєкту

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

    def input_person_data(self):
            full_name = input('Введіть прізвище, ім\'я, по-батькові: ')
            birth_date = input('Введіть дату народження: ')
            contact_phone = input('Введіть номер телефону: ')
            city = input('Введіть місто: ')
            country = input('Введіть країну: ')
            address = input('Введіть домашню адресу: ')
            self.set_full_name(full_name)
            self.set_birth_date(birth_date)
            self.set_contact_phone(contact_phone)
            self.set_city(city)
            self.set_country(country)
            self.set_address(address)
            

    def show_info_of_person(self):
        print("Прізвище, імя, по-батькові: ", self.full_name)
        print("Дата народження: ", self.birth_date)
        print("Телефон: ", self.contact_phone)
        print("Місто: ", self.city)
        print("Країна: ", self.country)
        print("Домашня адреса: ", self.address)

    @staticmethod
    def get_number_of_people():
        return Human.number_of_people

print('\nВиводимо інформацію заздалегідь створеного об'"'"'єкту '"'"'Людина'"'"'.')
person1 = Human()
person1.set_full_name('Коцький Пан Мяу')
person1.set_birth_date('10-03-2020')
person1.set_contact_phone('1234567')
person1.set_city('Диканька')
person1.set_country('Україна')
person1.set_address('Ведьмаків провулк, 7')
person1.show_info_of_person()

print('\nВводимо інформацію про новий об'"'"'єкт '"'"'Людина'"'"'.')
person2 = Human()
person2.input_person_data()
print('\nВиводимо інформацію про новостворений об'"'"'єкт '"'"'Людина'"'"'.')
person2.show_info_of_person()

print('\nКількість створених об'"'"'ектів класу "Людина":', Human.get_number_of_people())