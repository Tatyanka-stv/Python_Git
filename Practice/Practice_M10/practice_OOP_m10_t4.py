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
        numerator = int(input('Введіть чисельник: '))
        denominator = int(input('Введіть знаменник: '))
        self.set_numerator(numerator)
        self.set_denominator(denominator)

    def display(self):
        print(str(self.numerator)+'/'+str(self.denominator))

    def sum_of_fractions(self, other_fraction):
        new_numerator = (self.numerator * other_fraction.denominator) + (other_fraction.numerator * self.denominator)
        new_denominator = self.denominator * other_fraction.denominator
        return Fraction(new_numerator, new_denominator)

    def fraction_difference(self, other_fraction):
        new_numerator = (self.numerator * other_fraction.denominator) - (other_fraction.numerator * self.denominator)
        new_denominator = self.denominator * other_fraction.denominator
        return Fraction(new_numerator, new_denominator)

    def fraction_multiply(self, other_fraction):
        new_numerator = self.numerator * other_fraction.numerator
        new_denominator = self.denominator * other_fraction.denominator
        return Fraction(new_numerator, new_denominator)

    def fraction_divide(self, other_fraction):
        if other_fraction.numerator == 0:
            print('Ділення на ноль неможливо.')
            return None
        new_numerator = self.numerator * other_fraction.denominator
        new_denominator = self.denominator * other_fraction.numerator
        return Fraction(new_numerator, new_denominator)

print('Приклад виводу завданих дробів.')
fraction1 = Fraction(1, 2)
fraction2 = Fraction(3, 4)

print("Дріб 1:")
fraction1.display()

print("Дріб 2:")
fraction2.display()

print('Дії над дробами.')
sum_result = fraction1.sum_of_fractions(fraction2)
print('Сумма:')
sum_result.display()

diff_result = fraction1.fraction_difference(fraction2)
print('Різниця:')
diff_result.display()

mul_result = fraction1.fraction_multiply(fraction2)
print('Множення:')
mul_result.display()

div_result = fraction1.fraction_divide(fraction2)
print('Ділення:')
div_result.display()

print('Приклад вводу дробу:')
print('Дріб 1:')
my_fraction1 = Fraction(0,1) #ФІШКА! вводимо первинні значення Fraction(0,1), щоб можна було користувачеві вводити самостійно дроби
my_fraction1.input_data()
my_fraction1.display()
print('\nДріб 2:')
my_fraction2 = Fraction(0,1) 
my_fraction2.input_data()
my_fraction2.display()

print('Дії над дробами.')
sum_result = my_fraction1.sum_of_fractions(my_fraction2)
print('Сумма:')
sum_result.display()

diff_result = my_fraction1.fraction_difference(my_fraction2)
print('Різниця:')
diff_result.display()

mul_result = my_fraction1.fraction_multiply(my_fraction2)
print('Множення:')
mul_result.display()

div_result = my_fraction1.fraction_divide(my_fraction2)
print('Ділення:')
div_result.display()
