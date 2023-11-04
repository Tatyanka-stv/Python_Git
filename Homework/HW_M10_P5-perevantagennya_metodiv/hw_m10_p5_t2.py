class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(self.imag)}i"

    def __add__(self, other):
        if isinstance(other, Complex):
            real_part = self.real + other.real
            imag_part = self.imag + other.imag
            return Complex(real_part, imag_part)

    def __sub__(self, other):
        if isinstance(other, Complex):
            real_part = self.real - other.real
            imag_part = self.imag - other.imag
            return Complex(real_part, imag_part)

    def __mul__(self, other):
        if isinstance(other, Complex):
            real_part = self.real * other.real - self.imag * other.imag
            imag_part = self.real * other.imag + self.imag * other.real
            return Complex(real_part, imag_part)

    def __truediv__(self, other):
        if isinstance(other, Complex):
            denominator = other.real**2 + other.imag**2
            real_part = (self.real * other.real + self.imag * other.imag) / denominator
            imag_part = (self.imag * other.real - self.real * other.imag) / denominator
            return Complex(real_part, imag_part)

    @classmethod
    def input_complex(cls):
        while True:
            try:
                real = float(input('Введіть дійсну частину: '))
                imag = float(input('Введіть уяву частину: '))
                return cls(real, imag)
            except ValueError:
                print('Некоректний ввод. Введіть числа.')


complex1 = Complex(2, 3)
complex2 = Complex(1, -2)

sum_result = complex1 + complex2
difference_result = complex1 - complex2
product_result = complex1 * complex2
division_result = complex1 / complex2

print("complex1:", complex1)
print("complex2:", complex2)
print("Сума:", sum_result)
print("Різниця:", difference_result)
print("Добуток:", product_result)
print("Ділення:", division_result)

complex_number = Complex.input_complex()
print('Ви ввели комплексне число ',complex_number)