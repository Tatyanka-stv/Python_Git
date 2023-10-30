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
        try:
            self.model = input('Введіть назву моделі автомобіля: ')
            self.year = input('Введіть рік виробництва: ')
            self.manufacturer = input('Введіть виробника: ')
            self.engine_size = float(input('Введіть об'"'"'єм двигуна: '))
            self.color = input('Введіть колір: ')
            self.price = float(input('Введіть вартість: '))
        except:
            print('Ви ввели невірні числові дані.')

    def show_data(self):
        print('Назва моделі:', self.model)
        print('Рік виробництва: ', self.year)
        print('Виробник: ', self.manufacturer)
        print('Об'"'"'ем двигуна: ', self.engine_size)
        print('Колір: ', self.color)
        print('Ціна: $ ', self.price)

    # додали конструктор для створення обєкта з заданими параметрами cls(model, year, manufacturer, engine_size, color, price)
    @classmethod
    def create_with_defaults(cls):
        return cls("Unknown", "Unknown", "Unknown", 0.0, "Unknown", 0.0)

    # Перевантаження метода str для виведення інформації про обєкт
    def __str__(self):
        return 'Модель: '+self.model+' Рік випуску: '+str(self.year)+' Виробник: '+self.manufacturer+" Об""'""єм двигуна: "+str(self.engine_size)+' Колір: '+self.color+' Ціна: $ '+str(self.price)

    # Перевантаження метода eq для порівняння двух обєктів за декількома властивостями
    def __eq__(self, other):
        return self.model == other.model and self.manufacturer == other.manufacturer and self.engine_size == other.engine_size

    # Перевантаження метода  для порівняння двух обєктів по ціні
    def __lt__(self, other):
        return self.price < other.price

    def __le__(self, other):
        return self.price <= other.price

    def __gt__(self, other):
        return self.price > other.price

    def __ge__(self, other):
        return self.price >= other.price

car1 = Car("Toyota", 2020, "Toyota", 2.5, "Серебряный", 20000)
car2 = Car.create_with_defaults()
car3 = Car("", "", "", "", "", 0.0)
car3.input_data()

print('\nВиводимо іформацію про автомобілі:')
print('Автомобіль 1:')
car1.show_data()

print('\nАвтомобіль 2 (створений конструктором):')
car2.show_data()

print('Автомобіль 3:')
print(str(car3))

#перевірка роботи перевантажених методів порівнянн = > <
if car1 == car2:
    print('\nАвтомобіль 1 та Автомобіль 2 ідентичні.')
else:
    print('\nАвтомобіль 1 та Автомобіль 2 різні.')

if car1 == car3:
    print('\nАвтомобіль 1 та Автомобіль 3 ідентичні.')
else:
    print('\nАвтомобіль 1 та Автомобіль 3 різні.')

if car2 == car3:
    print('\nАвтомобіль 2 та Автомобіль 3 ідентичні.')
else:
    print('\nАвтомобіль 2 та Автомобіль 3 різні.')

if car1 < car2:
    print('\nАвтомобіль 1 менше вартує ніж Автомобіль 2.')
else:
    print('\nАвтомобіль 1 більш вартує ніж Автомобіль 2.')

if car1 > car3:
    print('\nАвтомобіль 1 більше вартує ніж Автомобіль 3.')
else:
    print('\nАвтомобіль 1 менше вартує ніж Автомобіль.')

