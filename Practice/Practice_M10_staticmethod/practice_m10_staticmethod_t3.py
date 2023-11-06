import math

class MathFunctions:
    @staticmethod
    def maximum_of_numbers(a, b, c, d):
        return max(a, b, c, d)

    @staticmethod
    def minimum_of_numbers(a, b, c, d):
        return min(a, b, c, d)

    @staticmethod
    def avg_of_numbers(a, b, c, d):
        return (a + b + c + d) / 4

    @staticmethod
    def factorial_of_number(n):
        if n < 0:
            print('Факторіал числа для відємних чисел підрахувати неможливо.')
            
        elif n == 0 or n == 1:
            print('Факторіал числа'+str(n)+'дорівнює 1.')
        else:
            result = 1
            for i in range(1, n + 1):
                result = result * i
            return result

n1=float(input('Введіть перше число: '))
n2=float(input('Введіть друге число: '))
n3=float(input('Введіть третє число: '))
n4=float(input('Введіть четверте число: '))
print("Максимум:", MathFunctions.maximum_of_numbers(n1, n2, n3, n4))
print("Минимум:", MathFunctions.minimum_of_numbers(n1, n2, n3, n4))
print("Среднее арифметическое:", MathFunctions.avg_of_numbers(n1, n2, n3, n4))
n5=int(input('Введіть ціле число для підрахунку факторіалу: '))
print("Факториал:", MathFunctions.factorial_of_number(n5))