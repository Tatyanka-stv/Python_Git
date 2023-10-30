class Car:
    def __init__(self, model, year, manufacturer, engine_size, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_size = engine_size
        self.color = color
        self.price = price

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_manufacturer(self):
        return self.manufacturer

    def get_engine_size(self):
        return self.engine_size

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price

    def set_model(self, model):
        self.model = model

    def set_year(self, year):
        self.year = year

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def set_engine_size(self, engine_size):
        self.engine_size = engine_size

    def set_color(self, color):
        self.color = color

    def set_price(self, price):
        self.price = price

    def input_data(self):
        self.model = input('Введіть назву моделі автомобіля: ')
        self.year = input('Введіть рік виробництва: ')
        self.manufacturer = input('Введіть виробника: ')
        self.engine_size = input('Введіть об'"'"'єм двигуна: ')
        self.color = input('Введіть колір: ')
        self.price = float(input('Введіть вартість: '))

    def display(self):
        print('Назва моделі:', self.model)
        print('Рік виробництва: ', self.year)
        print('Виробник: ', self.manufacturer)
        print('Об'"'"'ем двигуна: ', self.engine_size)
        print('Колір: ', self.color)
        print('Ціна: $ ', self.price)


my_car = Car("", "", "", "", "", 0.0)

my_car.input_data()

print('\nІнформація про автомобіль:')
my_car.display()