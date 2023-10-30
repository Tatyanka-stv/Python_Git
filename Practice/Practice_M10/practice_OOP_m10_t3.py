class Country:
    def __init__(self, name, continent, population, phone_code, capital, cities=[]):
        self.name = name
        self.continent = continent
        self.population = population
        self.phone_code = phone_code
        self.capital = capital
        self.cities = cities

    def input_data(self):
        self.name = input('Введіть назву країни: ')
        self.continent = input('Введіть назву континенту: ')
        self.population = int(input('Введіть кількість мешканців у країні: '))
        self.phone_code = input('Введіть телефоний код країни: ')
        self.capital = input('Введіть назву столиці країни: ')
        city_count = int(input('Введіть кількість міст у країні: '))
        self.cities = []
        for i in range(city_count):
            city_name = input('Введіть назву міста: ')
            self.cities.append(city_name)

    def display_data(self):
        print('Назва країни: ', self.name)
        print('Назва континенту: ', self.continent)
        print('Кількість мешканців у країні: ', self.population)
        print('Телефоний код країни: ', self.phone_code)
        print('Назва столиці: ', self.capital)
        print('Перелік міст країни: ', ", ".join(self.cities))

    def get_name(self):
        return self.name

    def get_continent(self):
        return self.continent

    def get_population(self):
        return self.population

    def get_phone_code(self):
        return self.phone_code

    def get_capital(self):
        return self.capital

    def get_cities(self):
        return self.cities

    def set_name(self, name):
        self.name = name

    def set_continent(self, continent):
        self.continent = continent

    def set_population(self, population):
        self.population = population

    def set_phone_code(self, phone_code):
        self.phone_code = phone_code

    def set_capital(self, capital):
        self.capital = capital

    def add_city(self, city_name):
        self.cities.append(city_name)

print('Перший приклад виводу інформації про країну: ')
country = Country('Україна', 'Євразія', 350000, '+380552', 'Київ', ['Харків', 'Львів'])
country.display_data()

print('\nПриклад вводу інформації по країні: ')
country.input_data()
print('\nДругий приклад виводу інформації про країну: ')
country.display_data()

print('\nНова назва країни: ')
new_name = country.get_name()
print('Нова назва країни: ', new_name)