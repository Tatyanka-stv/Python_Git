class Fraction:
    
    def __init__(self, numerator, denominator):
        self.numerator = numerator 
        self.denominator = denominator 

    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    def set_numerator(self, numerator):
        self.numerator = numerator

    def set_denominator(self, denominator):
        if denominator != 0:
            self.denominator = denominator
        else:
            print('Знаменник не може дорівнювати нулю.')

    def input_data(self):
        try:
            numerator = int(input('Введіть чисельник: '))
            denominator = int(input('Введіть знаменник: '))
            self.set_numerator(numerator)
            self.set_denominator(denominator)
        except:
            print('Ви ввели не ціле число. Чисельник та знаменник дробу повинні бути цілими числами.')

    def display(self):
        if  (self.numerator is None) or (self.denominator is None) or (type(self.numerator) is not int) or (type(self.denominator) is not int):
            print('Вивести на екран дріб неможливо.')
        else:
            if self.denominator == 0:
                print('Вивести на екран дріб неможливо, так як знаменник не може дорівнювати 0.')
            else:
                print(str(self.numerator)+'/'+str(self.denominator))

    def __add__(self, other_fraction): 
        if isinstance(other_fraction, Fraction):
            if self.denominator == other_fraction.denominator:
                new_numerator = self.numerator + other_fraction.numerator
                new_denominator = self.denominator
                return Fraction(new_numerator, new_denominator)
            else:
                new_numerator = (self.numerator * other_fraction.denominator) + (other_fraction.numerator * self.denominator)
                new_denominator = self.denominator * other_fraction.denominator
                return Fraction(new_numerator, new_denominator)
        else:
            print('Даний тип операнда неможливий для оператора додавання +.')
        
    def __sub__(self, other_fraction):
        if isinstance(other_fraction, Fraction):
            if self.denominator == other_fraction.denominator:
                new_numerator = self.numerator - other_fraction.numerator
                new_denominator = self.denominator
                return Fraction(new_numerator, new_denominator)
            else:
                new_numerator = (self.numerator * other_fraction.denominator) - (other_fraction.numerator * self.denominator)
                new_denominator = self.denominator * other_fraction.denominator
                return Fraction(new_numerator, new_denominator)
        else:
            print('Даний тип операнда неможливий для оператора віднімання -.')
        

    def __mul__(self, other_fraction):
        if isinstance(other_fraction, Fraction):
            new_numerator = self.numerator * other_fraction.numerator
            new_denominator = self.denominator * other_fraction.denominator
            return Fraction(new_numerator, new_denominator)       
        else:
            print('Даний тип операнда неможливий для оператора множення *.')

    def __truediv__(self, other_fraction):
        if isinstance(other_fraction, Fraction):
            if other_fraction.numerator == 0:
                print('Деление на ноль невозможно.')
                return Fraction(1, 0)  
            else:
                new_numerator = self.numerator * other_fraction.denominator
                new_denominator = self.denominator * other_fraction.numerator
                return Fraction(new_numerator, new_denominator)
        else:
            print('Данный тип операнда невозможен для оператора деления /.')
            return Fraction(0, 0)

print('Приклад виводу завданих дробів.')
fraction1 = Fraction(1, 2)
fraction2 = Fraction(3, 4)

print("Дріб 1:")
fraction1.display()

print("Дріб 2:")
fraction2.display()

print('Дії над дробами.')
sum_result = fraction1 + fraction2
print('Сумма:')
sum_result.display()

diff_result = fraction1 - fraction2
print('Різниця:')
diff_result.display()

mul_result = fraction1 * fraction2
print('Множення:')
mul_result.display()

div_result = fraction1 / fraction2
print('Ділення:')
div_result.display()

print('Приклад вводу довільних дробів:')
print('Дріб 1:')
my_fraction1 = Fraction(None,None) #ФІШКА! вводимо первинні значення Fraction(None,None), щоб можна було користувачеві вводити самостійно дроби
my_fraction1.input_data()
my_fraction1.display()
print('\nДріб 2:')
my_fraction2 = Fraction(None,None) 
my_fraction2.input_data()
my_fraction2.display()

print('Дії над дробами.')

if (my_fraction1.numerator is not None) and (my_fraction1.denominator is not None) and (my_fraction2.numerator is not None) and (my_fraction2.denominator is not None):
    if isinstance(my_fraction1.numerator, int) and isinstance(my_fraction1.denominator, int) and isinstance(my_fraction2.numerator, int) and isinstance(my_fraction2.denominator, int):
        sum_result = my_fraction1 + my_fraction2
        print('Сумма:')
        sum_result.display()

        diff_result = my_fraction1 - my_fraction2
        print('Разница:')
        diff_result.display()

        mul_result = my_fraction1 * my_fraction2
        print('Умножение:')
        mul_result.display()

        div_result = my_fraction1 / my_fraction2
        print('Деление:')
        div_result.display()
    else:  
        print('Вивести на екран дії з дробями невоможливо.')
else:
    print('Дроби не сформовані. Працювати з ними неможливо.')