"""Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица."""


class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for row in self.my_list:
            for i in row:
                print(f"{i:5}", end="")
            print()

    def __add__(self, second):
        for i in range(len(self.my_list)):
            for j in range(len(second.my_list[i])):
                self.my_list[i][j] = self.my_list[i][j] + second.my_list[i][j]
        return Matrix.__str__(self)


m = Matrix([[5, 1, 3], [8, 2, 6], [4, 1, 7]])
print("Матрица 1: ")
m.__str__()

new_m = Matrix([[2, 1, 5], [6, 9, 1], [10, 3, 7]])
print("\nМатрица 2: ")
new_m.__str__()

print("\nСумма матриц: ")
m.__add__(new_m)
