class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def setDay(self,day):
        self.day = day

    def getDay(self):
        return self.day
    
    def setMonth(self, month):
        self.month = month
        
    def getMonth(self):
        return self.month   
    
    def setYear(self, year):
        self.year = year
        
    def getYear(self):
        return self.year   
    
    def __str__(self):
        return str(self.day)+'.'+str(self.month)+'.'+str(self.year) 

class Human:
    def __init__(self, day, month, year):
        self.name = ''
        self.by_name = '' #по-батькові
        self.surname = ''
        self.birth_date = Date(day, month, year)
        self.contact_phone = '+38...'
        self.country = ''
        self.city = ''
        self.address_street = ''
        self.address_house = ''
        self.address_apartment = ''

    def set_name(self, name):
        self.name = name

    def set_by_name(self, by_name):
        self.by_name = by_name  

    def set_surname(self, surname):
        self.surname = surname     

    def set_birth_date(self, day, month, year):
        self.birth_date.setDay(day)
        self.birth_date.setMonth(month)
        self.birth_date.setYear(year)

    def set_contact_phone(self, contact_phone):
        self.contact_phone = contact_phone    

    def set_country(self, country):
        self.country = country

    def set_city(self, city):
        self.city = city
    
    def set_address_street(self, street):
        self.address_street = street

    def set_address_house(self, house):
        self.address_house = house

    def set_address_apartment (self, apartment):
        self.address_apartment = apartment

    def get_name(self):
        return self.name
    
    def get_by_name(self):
        return self.by_name
    
    def get_surname(self):
        return self.surname
    
    def get_birth_date_day(self):
        return self.birth_date.getDay
            
    def get_birth_date_month(self):
        return self.birth_date.getMonth
       
    def get_birth_date_year(self):
        return self.birth_date.getYear
    
    def get_contact_phone(self):
        return self.contact_phone   

    def get_country(self):
        return self.country
    
    def get_city(self):
        return self.city
 
    def get_address_street(self):
        return self.address_street
    
    def get_address_house(self):
        return self.address_house
    
    def get_address_apartment(self):
        return self.address_apartment

    def show_data(self):
        print()
        print('Виводимо інформацію про персону: ')
        print('Прізвище, імя, по-батькові:' + self.name + ' ' + self.by_name + ' ' + self.surname)
        print('Дата народження:', self.birth_date)
        print('Контактний телефон:', self.contact_phone)
        print('Країна:', self.country)
        print('Місто:', self.city)
        print('Домашня адреса: вул. ' + self.address_street + ', д. ' + self.address_house + ', кв. ' + self.address_apartment)

    def __str__(self):
        return str(self.name)+' '+ str(self.by_name)+' ' + str(self.surname) + ' ' + str(self.birth_date)+' '+str(self.contact_phone)+' '+str(self.city)+' '+str(self.country)+' '+str(self.address_street) + ' '+str(self.address_house)+' '+str(self.address_apartment)
    
    
    #функція введення даних
    def input_data_of_person(self):
        print('Вводимо повную інформацію про персону:')
        name = input('Введіть імя: ')
        self.set_name(name)
        by_name = input('Введіть по-батькові: ')
        self.set_by_name(by_name)
        surname = input('Введіть прізвище: ')
        self.set_surname(surname)
        day = input('Введіть дату дня народження: ')
        month = input('Введіть місяць народження: ')
        year = input('Введіть рік народження: ')
        self.set_birth_date(day, month, year)
        contact_phone = input('Введіть номер телефона у форматі +38...: ')
        self.set_contact_phone(contact_phone)
        country = input('Введіть страну: ')
        self.set_country(country)
        city = input('Введіть місто: ')
        self.set_city(city)
        address_street = input('Введіть назву вулиці: ')
        self.set_address_street(address_street)  
        address_house = input('Введіть номер будинку: ')
        self.set_address_house(address_house)    
        address_apartment = input('Введіть номер квартири: ')
        self.set_address_apartment(address_apartment)   



person1 = Human(0, 0, 0)  # ФИШКА!!!!!! Изначально задаем дату рождения с нулевыми значениями для избежания ошибки при инициализации класа Human
person1.input_data_of_person()

print('Перший варіант виводу інформації про людину. ')
#виводимо через метод show_data() класу Human
person1.show_data()

print('Другий варіант виводу інформації про людину. ')
#виводимо через окремі методи для кожного елементу обєкта  класу Human
print('ПІБ:' + str(person1.get_name()) + ' ' + str(person1.get_by_name()) + ' ' + str(person1.get_surname()))
       
print('Третій варіант виводу інформації про людину. ')
print(person1)