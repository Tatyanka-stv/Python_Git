class Device:
    def __init__(self, brand, model, power):
        self.brand = brand
        self.model = model
        self.power = power

    def turn_on(self):
        print("Пристрій " + self.brand + ' ' + self.model + " увімкнений.")

    def turn_off(self):
       print("Пристрій " + self.brand + ' ' + self.model + " вимкнений.")

    def input_data(self):
        self.brand = input('Введіть бренд пристрою: ')
        self.model = input('Введіть модель пристрою: ')
        while True:
            try:
                self.power = float(input('Введіть потужність пристрою (в ватах): '))
                if self.power <= 0:
                    print('Потужність повинна бути більше нуля.')
                else:
                    break
            except ValueError:
                print('Помилка вводу! Введіть коректне число.')

    def show_data(self):
        print('Бренд: ' + self.brand)
        print('Модель: ' + self.model)
        print('Потужність: ' + str(self.power) + ' Вт')

class CoffeeMachine(Device):
    def __init__(self, brand, model, power, coffee_type):
        super().__init__(brand, model, power)
        self.coffee_type = coffee_type

    def make_coffee(self):
        print('Готуємо каву '+ self.coffee_type + ' з ' + self.brand + ' ' + self.model + '.')

    def input_data_of_coffeemachine(self):
            super().input_data()
            self.coffee_type = input("Введіть марку кофе: ")
           
    def show_info_of_coffeemachine(self):
        super().show_data()
        print("Марка кофе: ", self.coffee_type)   

class Blender(Device):
    def __init__(self, brand, model, power, speed_levels):
        super().__init__(brand, model, power)
        self.speed_levels = speed_levels

    def blend(self, time_in_minutes, blender_power, vegetable_weight):
        print('Переробляємо ' + str(vegetable_weight) + ' грам овочів/фруктів протягом ' +str(time_in_minutes) + ' хвилин на рівні швидкості ' + str(self.speed_levels) + ' з потужністю ' + str( blender_power) + ' на ' + self.brand + ' ' + self.model)
    
    def input_vegetable_weight(self):
        while True:
            try:
                vegetable_weight = float(input("Введіть вагу овочів/фруктів у грамах: "))
                if vegetable_weight <= 0:
                    print("Вага овочів/фруктів повинна бути більше нуля.")
                else:
                    return vegetable_weight
            except ValueError:
                print("Помилка вводу! Введіть коректне число.")

    def input_blender_power(self):
        while True:
            try:
                blender_power = int(input("Введіть потужність блендера у ваттах: "))
                if blender_power <= 0:
                    print("Потужність блендера повинна бути більше нуля.")
                else:
                    return blender_power
            except ValueError:
                print("Помилка вводу! Введіть коректне ціле число.")              

    def calculate_blending_time(self, fruit_weight): 
        # Розрахунок часу переробки фруктів в залежності від потужності блендера
        time_per_100g = 1  # 1 хвилина на 100 грамів
        power_in_watts = self.power
        time_in_minutes = (fruit_weight / 100) * (time_per_100g / (power_in_watts / 1000))
        return time_in_minutes 
    
    def input_data_of_blender(self):
            super().input_data()
            self.speed_levels = input('Введіть кількість рівнів потужності: ')
           
    def show_info_of_blender(self):
        super().show_data()
        print('Кількість рівнів потужностей:', self.speed_levels)   

class MeatGrinder(Device):
    def __init__(self, brand, model, power, meat_type):
        super().__init__(brand, model, power)
        self.meat_type = meat_type
    
    def grind_meat(self, quantity):
        grinding_time = self.calculate_grinding_time(quantity)
        print("Переробка " + str(quantity) + " грам " +self.meat_type + ' на ' + self.brand + ' ' + self.model + ' займає ' + str(grinding_time) + ' хвилин.')
        
    def calculate_grinding_time(self, quantity):
        power_in_watts = self.power
        time_per_100g = 1  
        time_in_minutes = (quantity / 100) * (time_per_100g / (power_in_watts / 1000))
        return time_in_minutes    
    
    def input_meat_weight(self):
        while True:
            try:
                meat_weight = float(input("Введіть вагу м'яса у грамах: "))
                if meat_weight <= 0:
                    print("Вага м'яса повинна бути більше нуля.")
                else:
                    return meat_weight
            except ValueError:
                print("Помилка вводу! Введіть коректне число.")

    def input_meat_grinder_power(self):
        while True:
            try:
                meat_grinder_power = int(input("Введіть потужність м'ясорубки у ваттах: "))
                if meat_grinder_power <= 0:
                    print("Потужність м'ясорубки повинна бути більше нуля.")
                else:
                    return meat_grinder_power
            except ValueError:
                print("Помилка вводу! Введіть коректне ціле число.")

    def input_data_of_meatgrinder(self):
            super().input_data()
            self.meat_type = input("Введіть тип м'яса: ")
           
    def show_info_of_meatgrinder(self):
        super().show_info_of_person()
        print("Тип м'яса: ", self.meat_type)   

print('\nПрацюємо з класом Device: \n')
device = Device("BrandX", "Model_Y", 1000)
device.show_data()
print()
device.input_data()
print()
device.show_data()

print('\nПрацюємо з класом CoffeeMachine: \n')
coffee_machine = CoffeeMachine('', '', 0, '')
coffee_machine.input_data_of_coffeemachine()
print()
coffee_machine.show_info_of_coffeemachine()
print()
coffee_machine.turn_on()
coffee_machine.make_coffee()
coffee_machine.turn_off()

print('\nПрацюємо з класом Blender: \n')
blender = Blender('', '', 0, '')
blender.input_data_of_blender()
print()
blender.show_info_of_blender()
print('\nПереробка овочів/фруктів блендером:\n')
blender_power = blender.input_blender_power()
vegetable_weight = blender.input_vegetable_weight()
blender.turn_on()
blender.blend(blender.calculate_blending_time(vegetable_weight), blender_power, vegetable_weight)
blender.turn_off()

print('\nПрацюємо з класом MeatGrinder: \n')
meat_grinder = MeatGrinder('', '', 0, '')
meat_grinder.input_data_of_meatgrinder()
print()
meat_grinder.show_info_of_meatgrinder
print("\nПереробка м'яса м'ясорубкою:\n")
meat_grinder_power = meat_grinder.input_meat_grinder_power()
meat_weight = meat_grinder.input_meat_weight()
meat_grinder.turn_on()
meat_grinder.grind_meat(meat_weight)
meat_grinder.turn_off()
