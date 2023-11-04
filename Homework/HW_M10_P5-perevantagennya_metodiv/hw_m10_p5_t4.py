class Flat:
    def __init__(self, area, price):
        self.area = area
        self.price = price

    def __eq__(self, other):
        if isinstance(other, Flat):
            return self.area == other.area

    def __ne__(self, other):
        if isinstance(other, Flat):
            return self.area != other.area

    def __lt__(self, other):
        if isinstance(other, Flat):
            return self.price < other.price

    def __le__(self, other):
        if isinstance(other, Flat):
            return self.price <= other.price

    def __gt__(self, other):
        if isinstance(other, Flat):
            return self.price > other.price

    def __ge__(self, other):
        if isinstance(other, Flat):
            return self.price >= other.price

    def show_flat(self):
        print('Площа квартири: ' + str(self.area) + ' кв. м')
        print('Ціна квартири: ' + str(self.price) + ' грн.')

    @classmethod
    def input_flat(cls):
        while True:
            try:
                area = float(input('Введіть площу квартири: '))
                price = float(input('Введіть ціну квартири: '))

                if area > 0 and price > 0:
                    return cls(area, price)
                else:
                    print("Площа та ціна повинні бути додатними числами.")
            except ValueError:
                print('Некоректний ввід. Введіть числа.')


flat1 = Flat(100, 200000)
flat2 = Flat(80, 180000)
flat1.show_flat()
flat2.show_flat()

if flat1 == flat2:
    print("Площі квартир рівні")
else:
    print("Площі квартир відмінні")

if flat1 != flat2:
    print("Площі квартир відмінні")
else:
    print("Площі квартир рівні")

if flat1 > flat2:
    print("Перша квартира дорожча за другу")
else:
    print("Перша квартира дешевша за другу")

if flat1 <= flat2:
    print("Друга квартира дорожча або рівна за першу")
else:
    print("Перша квартира дорожча за другу")

print('Приклад вводу інформації про довільну квартиру:')
flat3 = Flat.input_flat()
flat3.show_flat()