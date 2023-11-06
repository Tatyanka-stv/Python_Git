class LengthConverter:
    @staticmethod
    def meters_to_feet(meters):
        feet = round(meters * 3.28084,3)
        return feet

    @staticmethod
    def feet_to_meters(feet):
        meters = round(feet / 3.28084,3)
        return meters

    @staticmethod
    def kilometers_to_miles(kilometers):
        miles = round(kilometers * 0.621371,3)
        return miles

    @staticmethod
    def miles_to_kilometers(miles):
        kilometers = round(miles / 0.621371,3)
        return kilometers

    @staticmethod
    def meters_to_yards(meters):
        yards = round(meters * 1.09361,3)
        return yards

    @staticmethod
    def yards_to_meters(yards):
        meters = round(yards / 1.09361,3)
        return meters

    @staticmethod
    def meters_to_inches(meters):
        inches = meters * 39.3701
        return inches

    @staticmethod
    def inches_to_meters(inches):
        meters = round(inches / 39.3701,3)
        return meters

    @staticmethod
    def pounds_to_kilograms(pounds):
        kilograms = round(pounds * 0.453592,3)
        return kilograms

    @staticmethod
    def kilograms_to_pounds(kilograms):
        pounds = round(kilograms / 0.453592,3)
        return pounds

    @staticmethod
    def display_meters(meters):
        print(str(meters) + ' метрів')

    @staticmethod
    def display_feet(feet):
        print(str(feet) + ' футів')

    @staticmethod
    def display_miles(miles):
        print(str(miles) + ' миль')

    @staticmethod
    def display_kilometers(kilometers):
        print(str(kilometers) + ' кілометрів')

    @staticmethod
    def display_yards(yards):
        print(str(yards) + ' ярдів')

    @staticmethod
    def display_inches(inches):
        print(str(inches) + ' дюймів')

    @staticmethod
    def display_pounds(pounds):
        print(str(pounds) + ' фунтів')

    @staticmethod
    def display_kilograms(kilograms):
        print(str(kilograms) + ' кілограмів')


pounds = 10
kilograms = LengthConverter.pounds_to_kilograms(pounds)
print(str(pounds) + ' фунтів = ' + str(kilograms) + ' кілограмів')
LengthConverter.display_kilograms(kilograms)


kilograms = 5
pounds = LengthConverter.kilograms_to_pounds(kilograms)
print(str(kilograms) + ' кілограмів = ' + str(pounds) + ' фунтів')
LengthConverter.display_pounds(pounds)

meters = 100
feets = LengthConverter.meters_to_feet(meters)
print(str(meters) + ' метрів = ' + str(feets) + ' футів')
LengthConverter.display_feet(feets)

feets = 120
meters = LengthConverter.feet_to_meters(feets)
print(str(feets) + ' футів = ' + str(meters) + ' метрів')
LengthConverter.display_meters(meters)

kilometers = 1.2
miles = LengthConverter.kilometers_to_miles(kilometers)
print(str(kilometers) + ' кілометрів = ' + str(miles) + ' миль')
LengthConverter.display_miles(miles)

miles = 2
kilometers = LengthConverter.miles_to_kilometers(miles)
print(str(miles) + ' миль = ' + str(kilometers) + ' кілометрів')
LengthConverter.display_kilometers(kilometers)

yards = 100
meters = LengthConverter.yards_to_meters(yards)
print(str(yards) + ' ярдів = ' + str(meters) + ' метрів')
LengthConverter.display_meters(meters)

meters = 50
yards = LengthConverter.meters_to_yards(meters)
print(str(meters) + ' метрів = ' + str(yards) + ' ярдів')
LengthConverter.display_yards(yards)

inches = 100
meters = LengthConverter.inches_to_meters(inches)
print(str(inches) + ' дюймів = ' + str(meters) + ' метрів')
LengthConverter.display_meters(meters)

meters = 25
inches = LengthConverter.meters_to_inches(meters)
print(str(meters) + ' метрів = ' + str(inches) + ' дюймів')
LengthConverter.display_inches(inches)