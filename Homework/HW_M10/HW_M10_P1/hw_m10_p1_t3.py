class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def get_name(self):
        return self.name

    def get_opening_date(self):
        return self.opening_date

    def get_country(self):
        return self.country

    def get_city(self):
        return self.city

    def get_capacity(self):
        return self.capacity

    def set_name(self, name):
        self.name = name

    def set_opening_date(self, opening_date):
        self.opening_date = opening_date

    def set_country(self, country):
        self.country = country

    def set_city(self, city):
        self.city = city

    def set_capacity(self, capacity):
        self.capacity = capacity

    def input_data(self):
        self.name = input('Введіть назву стадіону: ')
        self.opening_date = input('Введіть дату відкриття: ')
        self.country = input('Введіть країну: ')
        self.city = input('Введіть місто: ')
        self.capacity = int(input('Введіть місткість: '))

    def show_data(self):
        print('Назва стадіону: ', self.name)
        print('Дата відкриття: ', self.opening_date)
        print('Країна: ', self.country)
        print('Місто: ', self.city)
        print('Місткість: '+str(self.capacity)+ ' осіб. ')


my_stadium = Stadium("", "", "", "", 0)

print('\nВводимо інформацію про стадіон:')
my_stadium.input_data()

print('\nВиводимо інформацію про стадіон:')
my_stadium.show_data()