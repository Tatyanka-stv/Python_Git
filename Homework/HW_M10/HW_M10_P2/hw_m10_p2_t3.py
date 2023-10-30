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

    def __str__(self):
        return 'Назва стадіону: '+self.name+'\nДата відкриття: '+self.opening_date+'\nКраїна: '+self.country+'\nМісто: '+self.city+'\nМісткість: '+str(self.capacity)+' осіб.'

    # Добавляем конструктор с параметрами
    @classmethod
    def create_with_defaults(cls):
        return cls('Стадіон-Арена', '2000-01-01', 'Україна', 'Київ', 50000)

    #перевантажили методи для поріняння стадіонів по місткості
    def __eq__(self, other):
        return self.capacity == other.capacity

    def __lt__(self, other):
        return self.capacity < other.capacity

    def __le__(self, other):
        return self.capacity <= other.capacity

    def __gt__(self, other):
        return self.capacity > other.capacity

    def __ge__(self, other):
        return self.capacity >= other.capacity



stadium1 = Stadium("", "", "", "", 0)

print('\nВводимо інформацію про стадіон:')
stadium1.input_data()

print('\nВиводимо інформацію про стадіон:')
stadium1.show_data()

stadium2 = Stadium.create_with_defaults()
print('\n', str(stadium2))

stadium3 = Stadium("Стадіон-Кристал", "2010-10-10", "Україна", "Херсон", 2000)
print('\n', str(stadium3))

if stadium1 == stadium2:
    print(stadium1.name + ' та '+stadium2.name+' мають однакову місткість.')
else:
    if stadium1 > stadium2:
        print(stadium1.name + ' має місткість більшу, ніж  '+stadium2.name+'.')
    else:
        print(stadium2.name + ' має місткість більшу, ніж  '+stadium1.name+'.')    

if stadium2 == stadium3:
    print(stadium1.name + ' та '+stadium2.name+' мають однакову місткість.')
else:
    if stadium2 > stadium3:
        print(stadium2.name + ' має місткість більшу, ніж  '+stadium3.name+'.')
    else:
        print(stadium3.name + ' має місткість більшу, ніж  '+stadium2.name+'.')          