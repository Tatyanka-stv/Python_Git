class Animal:
    def __init__(self, name, kingdom, classes, species, habitat, size, weight):
        self.name = name
        self.kingdom = kingdom
        self.сlasses = classes
        self.species = species #вид
        self.habitat = habitat #середовище проживання
        self.size = size
        self.weight = weight

    def input_data(self):
        self.name = input('Введіть назва: ')
        self.kingdom = input('Введіть царство: ')
        self.classes = input('Введіть клас: ')
        self.species = input('Введіть ареал проживання: ')
        self.habitat = input('Введіть середовище проживання: ')
        self.size = input('Введіть розмір, см: ')
        self.weight = input('Введіть вагу, кг: ')

    def show_info(self):
        print('Назва: ' + self.name)
        print('Царство: ' + self.kingdom)
        print('Класс: ' + self.classes)
        print('Ареал проживання: ' + self.species)
        print('Середовище проживання: ' + self.habitat)
        print('Розмір, см: ' + self.size)
        print('Вага, кг: ' + self.weight)
    
    def type_eat(self, food):
        print(self.name + ' - харчування: ' + food)

    
class Tiger(Animal):
    def __init__(self, name, kingdom, classes, species, habitat, size, weight, subspecies):
        super().__init__(name, kingdom, classes, species, habitat, size, weight)
        self.subspecies = subspecies #підвид

    def input_data(self):
        super().input_data()
        self.subtype = input('Введіть підтип: ')

    def show_info(self):
        super().show_info()
        print('Підтип: ' + self.subtype)
     

class Crocodile(Animal):
    def __init__(self, name, kingdom, classes, species, habitat, size, weight, subtype):
        super().__init__(name, kingdom, classes, species, habitat, size, weight)
        self.subtype = subtype

    def input_data(self):
        super().input_data()
        self.subtype = input('Введіть підтип: ')

    def show_info(self):
        super().show_info()
        print('Підтип: ' + self.subtype)

class Kangaroo(Animal):
    def __init__(self, name, kingdom, classes, species, habitat, size, weight, subspecies):
        super().__init__(name, kingdom, classes, species, habitat, size, weight)
        self.subspecies = subspecies

    def input_data(self):
        super().input_data()
        self.subtype = input('Введіть підтип: ')

    def show_info(self):
        super().show_info()
        print('Підтип: ' + self.subtype)    


tiger = Tiger("", "", "", "", "", "", "", "")
print('\nВведіть інформацію про клас '"'"'Тигр'"'"':')
tiger.input_data()

print('\nВведіть інформацію про клас '"'"'Крокодил'"'"':')
crocodile = Crocodile("", "", "", "", "", "", "", "")
crocodile.input_data()

print('\nВведіть інформацію про клас '"'"'Кенгуру'"'"':')
kangaroo = Kangaroo("", "", "", "", "", "", "", "")
kangaroo.input_data()

print('\nВведіть інформацію про харчування згідно класам:')
food1 = input('Чим харчуються тигри: ') 
food2 = input('Чим харчуються крокодили: ')
food3 = input('Чим харчуються кенгуру: ')

print('\nВиводимо іинформацію про паспорти тварин.\n')
print('Інформація про тигра:')
tiger.show_info()
tiger.type_eat(food1)
print('\nІнформація про крокодила:')
crocodile.show_info()
crocodile.type_eat(food2)
print('\nІнформація про кенгуру:')
kangaroo.show_info()
kangaroo.type_eat(food3)
