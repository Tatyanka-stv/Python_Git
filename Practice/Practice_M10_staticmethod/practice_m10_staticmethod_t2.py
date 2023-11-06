class Square:
    # Счетчик подсчетов площади
    count_of_squares_of_figures= 0

    @staticmethod
    def quantity_count():
        Square.count_of_squares_of_figures += 1

    @staticmethod
    def get_count():
        return Square.count_of_squares_of_figures

    @staticmethod
    def figure_triangle(side, height):
        Square.quantity_count()
        return 0.5 * side * height

    @staticmethod
    def figure_rectangle(length, width):
        Square.quantity_count()
        return length * width

    @staticmethod
    def figure_square(side):
        Square.quantity_count()
        return side * side

    @staticmethod
    def figure_rhombus(diagonal1, diagonal2):
        Square.quantity_count()
        return 0.5 * diagonal1 * diagonal2

side = float(input('Введіть основу трикутника: '))
height = float(input('Введіть висоту трикутника: '))
print('Площа трикутника:', Square.figure_triangle(side, height))

lenght = float(input('Введіть довжину прямокутника: '))
width = float(input('Введіть ширину прямокутника: '))
print('Площа прямокутника:', Square.figure_rectangle(lenght, width))

side = float(input('Введіть основу квадрата: '))
print('Площа квадрата:', Square.figure_square(side))

diagonal1 = float(input('Введіть довжину першої діагоналі ромба: '))
diagonal2= float(input('Введіть довжину другої діагоналі ромба: '))
print('Площа ромба:', Square.figure_rhombus(diagonal1, diagonal2))

print('Кількість підрахунків площ фігур:', Square.get_count())