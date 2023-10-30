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

my_book = Book("", "", "", "", "", 0.0)

my_book.input_data()

print('\nВиводимо інформацію про книгу:')
my_book.show_data()