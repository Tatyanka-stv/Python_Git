import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def input_radius(self):
        while True:
            try:
                radius = float(input('Введіть радіус кола: '))
                if radius > 0:
                    self.radius = radius
                    break
                else:
                    print("Введіть додатнє значення для радіуса.")
            except ValueError:
                print('Некоректне введення. Введіть число.')

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return False

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        raise TypeError('Порівняти неможливо, оскільки одне із значень не є об\'єктами класу Circle.')

    def __le__(self, other):
        if isinstance(other, Circle):
            return self.radius <= other.radius
        raise TypeError('Порівняти неможливо, оскільки одне із значень не є об\'єктами класу Circle.')

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius
        raise TypeError('Порівняти неможливо, оскільки одне із значень не є об\'єктами класу Circle.')

    def __ge__(self, other):
        if isinstance(other, Circle):
            return self.radius >= other.radius
        raise TypeError('Порівняти неможливо, оскільки одне із значень не є об\'єктами класу Circle.')

    
    def __add__(self, value):
        if isinstance(value, (int, float)):
            if self.radius + value > 0:
                #self.radius = self.radius + value
                return Circle(self.radius + value)
            else:
                print('Введене число додати до радіусу неможливо. Коло не можливо побудувати.')
        else:
            raise TypeError('Додати число до радіусу неможливо, оскільки одне із значень не є числом.')
                

    def __sub__(self, value):
        if isinstance(value, (int, float)):
            if self.radius - value > 0:
                #self.radius = self.radius - value
                return Circle(self.radius - value)
            else:
                print('Введене число відняти від радіусу неможливо. Коло не можливо побудувати.')
        
        else:
            raise TypeError('Відняти число від радіусу неможливо, оскільки одне із значень не є числом.')


    def __iadd__(self, value):
        if isinstance(value, (int, float)):
            if self.radius + value >= 0:
                self.radius += value
                return self
            else:
                print('Помилка! Ви ввели невірне число. Коло не можливо побудувати.')
        else:
            raise TypeError('Додати число до радіусу неможливо, оскільки одне із значень не є числом.')
        

    def __isub__(self, value):
        if isinstance(value, (int, float)):
            if self.radius - value >0:
                self.radius -= value
                return self
            else:
                print('Помилка! Ви ввели невірне число. Коло не можливо побудувати.')
        else:
            raise TypeError('Відняти число від радіусу неможливо, оскільки одне із значень не є числом.')
        

    def __str__(self):
        return 'Коло з радіусом ' + str(self.radius)

    def area(self):
        return math.pi * self.radius ** 2



circle1 = Circle(0)
circle2 = Circle(0)
print('\nВводимо радіуси 2х кіл для демонстрації роботи з ними:')
circle1.input_radius()
print(circle1)
circle2.input_radius() 
print(circle2)

if circle1 == circle2:
    print('Радіуси кіл рівні.')
else:
    if circle1 > circle2:
        print('Радіус першого кола більший.')
    else:
        print('Радіус другого кола більший.')

print('\nПропорційна зміна радіусів кіл:')
delta1 = float(input('Введіть число, на яке треба збільшити радіус першого кола: '))
result1 = Circle(0)
result1 = circle1 + delta1
print(result1)

delta2 = float(input('Введіть число, на яке треба зменшити радіус другого кола: '))
result2 = Circle(0)
result2 = circle2 - delta2
print(result2)

print('\n*******')

circle1 += delta1
print(circle1)

circle2 -= delta2
print(circle2)