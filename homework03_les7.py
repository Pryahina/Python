"""Реализовать программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий количеству
ячеек клетки (целое число). В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам. Метод должен возвращать строку вида *****\n*****\n*****...,
где количество ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает,
то в последний ряд записываются все оставшиеся."""


class Cell:
    def __init__(self, quantity: int):
        self.quantity = quantity

    def __add__(self, second):
        return f"Сумма двух клеток равна: {self.quantity + second.quantity} яч."

    def __sub__(self, second):
        sub = self.quantity - second.quantity
        return f"Разность двух клеток равна: {sub} яч." if sub > 0 else "Разность меньше нуля"

    def __mul__(self, second):
        return f"Произведение двух клеток равно: {self.quantity * second.quantity} яч."

    def __truediv__(self, second):
        return f"Деление двух клеток равно: {self.quantity // second.quantity} яч."

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row}\\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return f"Разбиение клетки из {self.quantity} яч. на ряд из {cells_in_row} яч: {row}"


first_cell = 30
second_cell = 15
f = Cell(first_cell)
s = Cell(second_cell)
print(f"Размер первой клетки равен: {first_cell} яч.\nРазмер второй клетки равен: {second_cell} яч.")
print(Cell.__add__(f, s))
print(Cell.__sub__(f, s))
print(Cell.__mul__(f, s))
print(Cell.__truediv__(f, s))
print(Cell.make_order(f, 7))
print(Cell.make_order(s, 7))
