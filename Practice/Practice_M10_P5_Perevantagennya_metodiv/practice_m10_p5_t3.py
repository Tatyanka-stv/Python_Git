class Library:
    def __init__(self, name, address, num_books):
        self.name = name
        self.address = address
        self.num_books = num_books

    def input_data(self):
        self.name = input('Введіть назву бібліотеки: ')
        self.address = input('Введіть адресу бібліотеки: ')
        while True:
            try:
                self.num_books = int(input('Введіть кількість книг: '))
                if self.num_books >= 0:
                    return False
                else:
                    print('Ви ввели не додатнє число для кількості книг.')  
            except:
                print('Ви ввели не ціле число для кількості книг.')   

    def set_name (self, name):
        self.name = name

    def get_name(self):
        return self.name             

    def set_address (self, address):
        self.address = address

    def get_address(self):
        return self.address

    def set_num_books (self, num_books):
        self.num_books = num_books

    def get_num_books(self):
        return self.num_books 

    def __add__(self, other):
        if isinstance(other, int):
            return Library(self.name, self.address, self.num_books + other)
        else:
            if isinstance(other, Library):
                return Library(self.name + ' + ' + other.name, self.address + ' + ' + other.address, self.num_books +  other.num_books)

            else:
                raise ValueError("Помилковий операнд для додавання")

    def __sub__(self, other):
        if isinstance(other, int):
            return Library(self.name, self.address, self.num_books - other)
        else:
            raise ValueError("Помилковий операнд для віднімання")

    def __iadd__(self, other):
        if isinstance(other, int):
            self.num_books += other
            return self
        else:
            raise ValueError("Помилковий операнд для додавання")

    def __isub__(self, other):
        if isinstance(other, int):
            self.num_books -= other
            return self
        else:
            raise ValueError("Помилковий операнд для віднімання")

    def __lt__(self, other):
        if isinstance(other, Library):
            return self.num_books < other.num_books
        else:
            raise ValueError("Недійсний операнд для порівняння 'менше'")

    def __gt__(self, other):
        if isinstance(other, Library):
            return self.num_books > other.num_books
        else:
            raise ValueError("Недійсний операнд для порівняння 'більше'")

    def __le__(self, other):
        if isinstance(other, Library):
            return self.num_books <= other.num_books
        else:
            raise ValueError("Недійсний операнд для порівняння 'менше або дорівнює'.")

    def __ge__(self, other):
        if isinstance(other, Library):
            return self.num_books >= other.num_books
        else:
            raise ValueError("Недійсний операнд для порівняння 'більше або дорівнює'.")

    def __eq__(self, other):
        if isinstance(other, Library):
            return self.num_books == other.num_books
        else:
            raise ValueError("Недійсний операнд для порівняння на рівність об'єктів.")

    def __ne__(self, other):
        if isinstance(other, Library):
            return self.num_books != other.num_books
        else:
            raise ValueError("Недійсний операнд для порівняння на нерівність об'єктів.")

    def __str__(self):
        return self.name + ', адреса: '+self.address + ', кількість книг: ' + str(self.num_books)


'''
пояснення між різницею  + та +=
якщо використовується __iadd__ для об'єкта library1, це змінить сам об'єкт library1, 
а якщо ви використовуєте __add__, то буде створено новий об'єкт, і library1 залишиться незмінним.
'''
print('\nВиводимо дані про завдані бібліотеки:')

library1 = Library("Library A", "123 Main St", 100)
library2 = Library("Library B", "456 Elm St", 150)
print(library1, '\n')
print(library2, '\n')

print("Приклад додавання 2 об'єктів класу Library:")
library3 = Library("", "", 0)
library3 = library1 + library2
print(library3, '\n')

print("Приклад додавання числа до об'єкту класу Library:")
library1 += 50  # Додаємо 50 книг
library2 -= 30  # Віднімаємо 30 книг

print(library1, '\n')
print(library2, '\n')

print('\nПриклад порівняння 2 обєктів класу Library:')
# порівняння
if library1 > library2:
    print(library1.name +  ' має більше книг, ніж ' + library2.name)
elif library1 < library2:
     print(library1.name +  ' має менше книг, ніж ' + library2.name)
else:
     print(library1.name +  ' має таку саму книг, як і ' + library2.name)

print("\nПриклад вводу об'єкту класу Library:")
library4 = Library("", "", 0) 
library4.input_data()
print(str(library4))