"""Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата."""


class ComplexNumber:
    def __init__(self, num_1, num_2, *args):
        self.num_1 = num_1
        self.num_2 = num_2

    def __add__(self, other):
        if self.num_2 + other.num_2 >= 0:
            return f"z = {self.num_1 + other.num_1} + {self.num_2 + other.num_2} * i"
        else:
            return f"z = {self.num_1 + other.num_1} - {abs(self.num_2 + other.num_2)} * i"

    def __mul__(self, other):
        if (self.num_1 * other.num_2 + other.num_1 * self.num_2) >= 0:
            return f'z = {self.num_1 * other.num_1 - (self.num_2 * other.num_2)} + {self.num_1 * other.num_2 + other.num_1 * self.num_2} * i'
        else:
            return f'z = {self.num_1 * other.num_1 - (self.num_2 * other.num_2)} - {abs(self.num_1 * other.num_2 + other.num_1 * self.num_2)} * i'

    def __str__(self):
        return f'z = {self.num_1} + {self.num_2} * i'


z_1 = ComplexNumber(2, -4)
z_2 = ComplexNumber(5, -1)
print(f"Первое комплексное число: {z_1}")
print(f"Второе комплексное число: {z_2}")
print(f"Сумма комплексных чисел: {z_1 + z_2}")
print(f"Произведение комплексных чисел: {z_1 * z_2}")
