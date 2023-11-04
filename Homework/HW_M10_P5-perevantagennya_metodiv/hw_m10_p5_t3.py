class Airplane:
    def __init__(self, model, max_passengers, current_passengers=0):
        self.model = model
        self.max_passengers = max_passengers
        self.current_passengers = current_passengers

    def __eq__(self, other):
        if isinstance(other, Airplane):
            return self.model == other.model

    def __add__(self, passengers):
        if isinstance(passengers, int) and passengers >= 0:
            new_passengers = self.current_passengers + passengers
            return Airplane(self.model, self.max_passengers, new_passengers)
        else:
            raise ValueError('Невірна кількість пасажирів для додавання.')

    def __iadd__(self, passengers):
        if isinstance(passengers, int) and passengers >= 0:
            self.current_passengers += passengers
            return self
        else:
            raise ValueError('Невірна кількість пасажирів для додавання.')

    def __sub__(self, passengers):
        if isinstance(passengers, int) and passengers >= 0:
            new_passengers = self.current_passengers - passengers
            return Airplane(self.model, self.max_passengers, new_passengers)
        else:
            raise ValueError('Невірна кількість пасажирів для віднімання.')

    def __isub__(self, passengers):
        if isinstance(passengers, int) and passengers >= 0:
            self.current_passengers -= passengers
            return self
        else:
            raise ValueError('Невірна кількість пасажирів для віднімання.')

    def __lt__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers < other.max_passengers

    def __le__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers <= other.max_passengers

    def __gt__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers > other.max_passengers

    def __ge__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers >= other.max_passengers

    def __str__(self):
        return 'Літак ' + str(self.model) + ' з поточною кількістью пасажирів: '+ str(self.current_passengers) + ' із загальною кількість місць: '+ str(self.max_passengers)
    
    @classmethod
    def input_airplane(cls):
        while True:
            try:
                model = input("Введіть модель літака: ")
                max_passengers = int(input('Введіть максимальну кількість пасажирів: '))
                current_passengers = int(input('Введіть поточну кількість пасажирів на борту: '))    
                if max_passengers >= 0 and current_passengers >= 0:
                    if max_passengers >= current_passengers:
                        return cls(model, max_passengers, current_passengers)
                    else:
                        print('Поточна кількість пасажирів не може бути більша за максимальну кількість місць.')
                else:
                    print("Максимальна та поточна кількості пасажирів повинні бути не від'ємними числами.")
            except:
                print("Помилка при введенні чисел.")



# Приклад використання
airplane1 = Airplane("Boeing 747", 416, 100)
airplane2 = Airplane("Airbus A380", 853, 600)
print('Інформація про літаки із завданими параметрами:')
print(airplane1)
print(airplane2)

# Порівняння типів самолетів 
if airplane1 == airplane2:
    print('Літаки однакові за моделлю.')
else:
     print('Літаки неоднакові за моделлю.')   
  
# Додавання пасажирів, Віднімання пасажирів
print('Інформація про літаки зі зміненими параметрами:')
airplane1 += 100  
print(airplane1)  

airplane2 -= 200  
print(airplane2)  

 # Порівняння за максимальною кількістю пасажирів 
if airplane1 > airplane2:
    print('Перший літак має більшу максимальну кількість місць.')
else:
    if airplane1 < airplane2:    
        print('Перший літак має меншу максимальну кількість місць.')
    else:    
        print('Літаки мають однакову максимальну кількість місць.')

print('Вводимо дані про довільний літак: ')
airplane = Airplane.input_airplane()
print(airplane)      