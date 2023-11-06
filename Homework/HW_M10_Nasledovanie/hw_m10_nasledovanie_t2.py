class Ship:
    def __init__(self, name, length, displacement):
        self.name = name
        self.length = length
        self.displacement = displacement

    def input_data(self):
        self.name = input('Введіть назву корабля: ')
        while True:
            try:
                self.length = float(input('Введіть довжину корабля (у метрах): '))
                if self.length <= 0:
                    print('Довжина повинна бути більше нуля.')
                else:
                    break
            except ValueError:
                print('Помилка вводу! Введіть коректне число для довжини.')
        
        while True:
            try:
                self.displacement = float(input('Введіть водотоннажність корабля (у тоннах): '))
                if self.displacement <= 0:
                    print('Водотоннажність повинна бути більше нуля.')
                else:
                    break
            except ValueError:
                print('Помилка вводу! Введіть коректне число для водотоннажності.')

    def display_info(self):
        print('Назва: ' + self.name)
        print('Довжина: ' + str(self.length) + ' метрів.')
        print('Водотоннажність: ' + str(self.displacement) + ' тонн.')


class Frigate(Ship):
    def __init__(self, name, length, displacement, num_missiles):
        super().__init__(name, length, displacement)
        self.num_missiles = num_missiles

    def input_data_of_frigate(self):
        super().input_data()
        while True:
            try:
                self.num_missiles = int(input('Введіть кількість ракет на борту: '))
                if self.num_missiles <= 0:
                    print('Кількість ракет повинна бути більше нуля.')
                else:
                    break
            except ValueError:
                print('Помилка вводу! Введіть коректне число для кількості ракет.')

    def display_info_of_frigate(self):
        super().display_info()
        print('Кількість ракет на борту: ' + str(self.num_missiles) + ' штук.')


class Destroyer(Ship):
    def __init__(self, name, length, displacement, num_cannons):
        super().__init__(name, length, displacement)
        self.num_cannons = num_cannons

    def input_data_of_destroyer(self):
        super().input_data()
        while True:
            try:
                self.num_cannons = int(input('Введіть кількість гармат на борту: '))
                if self.num_cannons <= 0:
                    print('Кількість гармат повинна бути більше нуля.')
                else:
                    break
            except ValueError:
                print('Помилка вводу! Введіть коректне число для кількості гармат.')

    def display_info_of_destroyer(self):
        super().display_info()
        print('Кількість гармат на борту: ' + str(self.num_cannons) + ' штук.')


class Cruiser(Ship):
    def __init__(self, name, length, displacement, missile_system):
        super().__init__(name, length, displacement)
        self.missile_system = missile_system

    def input_data_of_cruiser(self):
        super().input_data()
        self.missile_system = input('Введіть кількість систем ракет на борту: ')
        while True:
            try:
                self.missile_system = int(self.missile_system)
                if self.missile_system <= 0:
                    print('Кількість систем ракет повинна бути більше нуля.')
                else:
                    break
            except ValueError:
                print('Помилка вводу! Введіть коректне число для кількості систем ракет.')

    def display_info_of_cruiser(self):
        super().display_info()
        print('Кількість систем ракет на борту: ' + str(self.missile_system))


print("\nІнформація про фрегат:")
frigate = Frigate('', 0, 0, 0)
frigate.input_data_of_frigate()
print()
frigate.display_info_of_frigate()

print("\nІнформація про есмінець:")
destroyer = Destroyer('', 0, 0, 0)
destroyer.input_data_of_destroyer()
print()
destroyer.display_info_of_destroyer()

print("\nІнформація про крейсер:")
cruiser = Cruiser('', 0, 0, '')
cruiser.input_data_of_cruiser()
print()
cruiser.display_info_of_cruiser()