class Number:
    def __init__(self,n): #присвоєння значення классу Number
        self.number = n
    
    def get_number(self):
        return self.number

    def set_number(self, number):
        self.number = number

    def input_number(self):
        try:
            number = int(input('Введіть ціле число: '))
            self.set_number(number)
        except:
            print('Ви ввели не ціле число.')

    def show_number(self):
        try:
            if self is None:
                print('Ви не ввели число')
            else:
                print('Введений екземпляр класу: '+str(self.number))
        except:
            print('Ви ввели не ціле число.')

    def __str__(self):
        return str(self.number)

    def __add__(self, other): # перевантаження методу додавання-2 екземпляра класа Number, 1 екземпляр класа +число int, 1 екземпляр + число float
        if isinstance(other, Number):# перевіряєм чи є other  екземпляром класу Number (oператор isintance (аналог функції type) которая проверяет, является ли указанный объект экземпляром определенного класса или типа.
            return Number(self.number + other.number)
        elif isinstance(other, (int, float)): # в даному випадку other це вже безпосередньо число типу int або float, НЕ Є ЕКЗЕПЛЯРОМ класу Number
            return Number(self.number + other)
        else:
            print('Даний тип операнда неможливий для оператора додавання +.')

    def __sub__(self, other): # перевантаження методу віднімання -2 екземпляра класа Number, 1 екземпляр класа +число int, 1 екземпляр + число float
        if isinstance(other, Number):
            return Number(self.number - other.number)
        elif type(other) is int:
            return Number(self.number - other)
        elif type(other) is float:
            return Number(self.number - other)
        else:
            print('Даний тип операнда неможливий для оператора віднімання -.')

    def __mul__(self, other):  # перевантаження методу множення-2 екземпляра класа Number, 1 екземпляр класа +число int, 1 екземпляр + число float
        if isinstance(other, Number):
            return Number(self.number * other.number)
        elif type(other) is int:
            return Number(self.number * other)
        elif type(other) is float:
             return Number(self.number * other)
        else:
            print('Даний тип операнда неможливий для оператора множення *.')

    def __truediv__(self, other):  # перевантаження методу ділення-2 екземпляра класа Number, 1 екземпляр класа +число int, 1 екземпляр + число float
        if isinstance(other, Number):
            if other.number == 0:
                print('Ділення на 0 неможливе!')
            else:
                return Number(round(self.number / other.number,2))
        if isinstance(other, (int, float)):
            if other == 0:
                print('Ділення на 0 неможливе!')
            else:
                return Number(round(self.number / other, 2))
        else:
            print('Даний тип операнда неможливий для оператора ділення /.')

    #перевантаження операторів на правосторонні операції:

    def __radd__(self, other): # перевантаження методу додавання-2 екземпляра класа Number, 1 екземпляр класа +число int, 1 екземпляр + число float
        if isinstance(other, Number):# перевіряєм чи є other  екземпляром класу Number (oператор isintance (аналог функції type) которая проверяет, является ли указанный объект экземпляром определенного класса или типа.
            return Number(self.number + other.number)
        elif isinstance(other, (int, float)): # в даному випадку other це вже безпосередньо число типу int або float, НЕ Є ЕКЗЕПЛЯРОМ класу Number
            return Number(self.number + other)
        else:
            print('Даний тип операнда неможливий для оператора додавання +.')

    def __rsub__(self, other): # перевантаження методу віднімання -2 екземпляра класа Number, 1 екземпляр класа +число int, 1 екземпляр + число float
        if isinstance(other, Number):
            return Number(self.number - other.number)
        elif type(other) is int:
            return Number(self.number - other)
        elif type(other) is float:
            return Number(self.number - other)
        else:
            print('Даний тип операнда неможливий для оператора віднімання -.')

    def __rmul__(self, other):  # перевантаження методу множення-2 екземпляра класа Number, 1 екземпляр класа +число int, 1 екземпляр + число float
        if isinstance(other, Number):
            return Number(self.number * other.number)
        elif type(other) is int:
            return Number(self.number * other)
        elif type(other) is float:
             return Number(self.number * other)
        else:
            print('Даний тип операнда неможливий для оператора множення *.')

    def __rtruediv__(self, other):  # перевантаження методу ділення-2 екземпляра класа Number, 1 екземпляр класа +число int, 1 екземпляр + число float
        if isinstance(other, Number):
            if other.number == 0:
                print('Ділення на 0 неможливе!')
            else:
                return Number(round(self.number / other.number,2))
        if isinstance(other, (int, float)):
            if other == 0:
                print('Ділення на 0 неможливе!')
            else:
                return Number(round(self.number / other, 2))
        else:
            print('Даний тип операнда неможливий для оператора ділення /.')




print('\nБлок 1: 2 екзмепляри класу Number.')  
#перевірка 2 екземпляра класу
num1 = Number(20) #надаємо значення 20 екземпляру num1 класу Number 
print('Перший екземпляр класу: '+ str(num1))
num2 = Number(35) #надаємо значення 35 екземпляру num1 класу Number 
print('Другий екземпляр класу: '+ str(num2))

# викоуємо арифметичні операції
result_addition = num1 + num2
result_subtraction = num1 - num2
result_multiplication = num1 * num2
result_division = num1 / num2

print('Результат додаванняя: ', result_addition)  
print('Результат віднімання: ', result_subtraction) 
print('Результат множення: ', result_multiplication) 
print('Результат ділення: ', result_division)  

print('\nБлок 2: 1 екзмепляр класу Number та число.')
#перевірка 1 екземпляр класу + число
num1 = Number(20) 
print('Екземпляр класу: '+ str(num1))
num2 = 10 
print('Число: '+ str(num2))

# викоуємо арифметичні операції
result_addition = num1 + num2
result_subtraction = num1 - num2
result_multiplication = num1 * num2
result_division = num1 / num2

print('Результат додаванняя: ', result_addition)  
print('Результат віднімання: ', result_subtraction) 
print('Результат множення: ', result_multiplication) 
print('Результат ділення: ', result_division)  


#перевірка правосторонніх операцій
#перевірка  число + 1 екземпляр класу 
print('\nБлок 3: число та 1 екзмепляр класу Number.')
num1 = 45
print('Число: '+ str(num1))
num2 = Number(25)  
print('Екземпляр класу: '+ str(num2))

# викоуємо арифметичні операції
result_addition = num1 + num2
result_subtraction = num1 - num2
result_multiplication = num1 * num2
result_division = num1 / num2

print('Результат додаванняя: ', result_addition)  
print('Результат віднімання: ', result_subtraction) 
print('Результат множення: ', result_multiplication) 
print('Результат ділення: ', result_division)  

#приклад вводу та виводу екземпляра класа
print('\nБлок 4: Вводимо та виводемо екзмепляр класу Number.')
num3 = Number(None)
num3.input_number()
num3.show_number()  