class City:
    def __init__(self, name, region, country, population, postal_code, phone_code):
        self.name = name
        self.region = region
        self.country = country
        self.population = population
        self.postal_code = postal_code
        self.phone_code = phone_code

    def input_data(self):
        self.name = input("Введіть назву міста: ")
        self.region = input("Введіть назву області: ")
        self.country = input("Введіть назву країни: ")
        self.population = int(input("Введіть кількість мешканців у місті: "))
        self.postal_code = input("Введіть поштовий індекс міста: ")
        self.phone_code = input("Введіть телефоний код міста: ")

    def show_data(self):
        print("Назва міста:", self.name)
        print("Назва області:", self.region)
        print("Назва країни:", self.country)
        print("Кількість мешканців у місті:", self.population)
        print("Поштовий індекс міста:", self.postal_code)
        print("Телефоний код міста:", self.phone_code)

    def get_name(self):
        return self.name

    def get_region(self):
        return self.region

    def get_country(self):
        return self.country

    def get_population(self):
        return self.population

    def get_postal_code(self):
        return self.postal_code

    def get_phone_code(self):
        return self.phone_code

    def set_name(self, name):
        self.name = name

    def set_region(self, region):
        self.region = region

    def set_country(self, country):
        self.country = country

    def set_population(self, population):
        self.population = population

    def set_postal_code(self, postal_code):
        self.postal_code = postal_code

    def set_phone_code(self, phone_code):
        self.phone_code = phone_code

# Пример использования класса
print("Перший варіант роботи з об""'""єктом:")
city = City("Київ", "Київська область", "Україна", 3500000, "01100", "+38044")
city.show_data()

print("\nДругий варіант роботи з об""'""єктом:")
city.input_data()
city.show_data()

print("\nТретій варіант роботи з об""'""єктом:")
city.set_name(input("Введіть нову назву міста: "))
new_name = city.get_name()
print("Нова назва міста:", new_name)