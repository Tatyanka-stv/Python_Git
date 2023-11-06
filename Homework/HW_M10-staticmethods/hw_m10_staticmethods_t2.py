class TemperatureConverter:
    count = 0  # лічильник для підрахунку конвертацій

    @staticmethod
    def celsius_to_farengeit(celsius):
        farengeit = (celsius * 9/5) + 32
        TemperatureConverter.count += 1
        return farengeit

    @staticmethod
    def farengeit_to_celsius(farengeit):
        celsius = (farengeit - 32) * 5/9
        TemperatureConverter.count += 1
        return celsius

    @staticmethod
    def get_conversion_count():
        return TemperatureConverter.count

    @staticmethod
    def input_celsius_temperature():
        while True:
            try:
                celsius = float(input('Введіть температуру в градусах Цельсія: '))
                return celsius
            except ValueError:
                print('Помилка вводу! Введіть коректне число.')

    @staticmethod
    def input_farengeit_temperature():
        while True:
            try:
                farengeit = float(input('Введіть температуру в градусах Фаренгейта: '))
                return farengeit
            except ValueError:
                print('Помилка вводу! Введіть коректне число.')

    @staticmethod
    def display_celsius_temperature(celsius):
        print('Температура в градусах Цельсія: '+ str(round(celsius,2)) + '°C')

    @staticmethod
    def display_farengeit_temperature(farengeit):
        print('Температура в градусах Фаренгейта: ' + str(round(farengeit,2)) + '°F')

celsius_temperature1 = 25
farengeit_temperature1 = TemperatureConverter.celsius_to_farengeit(celsius_temperature1)
print(str(celsius_temperature1) + '°C в Фаренгейтах: ' + str(round(farengeit_temperature1,2)))

farengeit_temperature2 = 95
celsius_temperature2 = TemperatureConverter.farengeit_to_celsius(farengeit_temperature2)
print(str(farengeit_temperature2) + '°F в Цельсиях: ' + str(round(celsius_temperature2,2)))

celsius_temperature = TemperatureConverter.input_celsius_temperature()
farengeit_temperature = TemperatureConverter.celsius_to_farengeit(celsius_temperature)
TemperatureConverter.display_farengeit_temperature(farengeit_temperature)

farengeit_temperature = TemperatureConverter.input_farengeit_temperature()
celsius_temperature = TemperatureConverter.farengeit_to_celsius(farengeit_temperature)
TemperatureConverter.display_celsius_temperature(celsius_temperature)

print('Кількість конвертацій: ' + str(TemperatureConverter.get_conversion_count()))