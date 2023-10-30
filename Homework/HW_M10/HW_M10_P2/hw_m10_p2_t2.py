class Book:
    def __init__(self, title, year, publisher, genre, author, price):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def get_title(self):
        return self.title

    def get_year(self):
        return self.year

    def get_publisher(self):
        return self.publisher

    def get_genre(self):
        return self.genre

    def get_author(self):
        return self.author

    def get_price(self):
        return self.price

    def set_title(self, title):
        self.title = title

    def set_year(self, year):
        self.year = year

    def set_publisher(self, publisher):
        self.publisher = publisher

    def set_genre(self, genre):
        self.genre = genre

    def set_author(self, author):
        self.author = author

    def set_price(self, price):
        self.price = price

    def input_data(self):
        self.title = input('Введіть назву книги: ')
        self.year = input('Введіть рік видавництва: ')
        self.publisher = input('Введіть видавника: ')
        self.genre = input('Введіть жанр: ')
        self.author = input('Введіть автора: ')
        self.price = float(input('Введіть ціна: '))

    def show_data(self):
        print('Назва книги: ', self.title)
        print('Рік видавнцтва: ', self.year)
        print('Видавник: ', self.publisher)
        print('Жанр: ', self.genre)
        print('Автор: ', self.author)
        print('Ціна: $ ', self.price)


#перевантажуємо методи
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.price < other.price

    def __le__(self, other):
        return self.price <= other.price

    def __gt__(self, other):
        return self.price > other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __str__(self):
        return 'Назва книги: '+self.title+'\nРік видавництва: '+str(self.year)+'\nВидавник: '+self.publisher+'\nЖанр: '+self.genre+'\nАвтор: '+self.author+'\nЦіна: $ '+str(self.price)


my_book1 = Book("", "", "", "", "", 0.0)

my_book1.input_data()

print('\nВиводимо інформацію про книгу:')
my_book1.show_data()
print()

my_book2 = Book("Янголи та демони", 2010, "Оріон", "детектив", "Антоніо Альварес", 250)
print(str(my_book2))
print()

my_book3 = Book("Темрява", 1996, "Якуба", "фантастика", "Міракль", 450)
print(str(my_book3))
print()

if my_book1 > my_book2:
    print("Книга '" + my_book1.title + "' вартує більше, ніж книга '" +  my_book2.title + "'")
else:
    print("Книга '" + my_book2.title + "' вартує більше, ніж книга '" +  my_book1.title + "'")


if my_book2 > my_book3:
    print("Книга '" + my_book2.title + "' вартує більше, ніж книга '" +  my_book3.title + "'")
else:
    print("Книга '" + my_book3.title + "' вартує більше, ніж книга '" +  my_book2.title + "'")