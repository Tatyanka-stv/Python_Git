class Money:
    def __init__(self, dollars=0, cents=0):
        self.dollars = dollars
        self.cents = cents

    def input_amount(self):
        while True:
            try:
                self.dollars = int(input('Введіть кількість доларів: '))
                if self.dollars < 0:
                    print('Кількість доларів повинна бути не менше 0.')
                    continue
                break
            except ValueError:
                print('Помилка вводу! Введіть цілі числа для кількості доларів.')

        while True:
            try:
                self.cents = int(input('Введіть кількість центів: '))
                if self.cents < 0 or self.cents >= 100:
                    print('Кількість центів повинна бути від 0 до 99.')
                    continue
                break
            except ValueError:
                print('Помилка вводу! Введіть цілі числа для кількості центів.')

    def display(self):
        print('На балансі: ' + str(self.dollars) + ' доларів і ' + str(self.cents) + ' центів.')

    def set_money(self, dollars, cents):
        if dollars >= 0:
            self.dollars = dollars
        if 0 <= cents <= 99:
            self.cents = cents

    def add(self, dollars, cents):
        if dollars >= 0:
            self.dollars += dollars
        if 0 <= cents <= 99:
            self.cents += cents
            if self.cents >= 100:
                self.dollars += self.cents // 100
                self.cents %= 100

    def subtract(self, dollars, cents):
        if dollars >= 0:
            self.dollars -= dollars
        if 0 <= cents <= 99:
            self.cents -= cents
            while self.cents < 0:
                self.dollars -= 1
                self.cents += 100
                if self.dollars < 0:
                    self.dollars = 0

print('\nПриклади виводу даних:')
money = Money(10, 50)
money.display()  

money.set_money(20, 75)
money.display()  

print('\nВводимо бажану кількість грошей:')
money = Money(0, 0)
money.input_amount()

print('\nСкільки грошей Ви бажаєто додати до введеної кількості?')
money1 = Money(0, 0)
money1.input_amount()
money.add(money1.dollars, money1.cents)
print('\nОтримуємо:')
money.display()  
print('\nСкільки грошей Ви бажаєто забрати від вже існуючої кількості?')
money2 = Money(0, 0)
money2.input_amount()
money.subtract(money2.dollars, money2.cents)
print('\nОтримуємо:')
money.display()  