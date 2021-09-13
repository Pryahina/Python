"""Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие
только чисел. Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя
данные и заполнять список только числами. Класс-исключение должен контролировать типы данных элементов
списка."""


class MyException(Exception):
    def __init__(self, num):
        self.num = num

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            if denominator == 0:
                raise MyException("Делить на ноль нельзя!")
            else:
                res = divider / denominator
                return res
        except MyException as err:
            return err


try:
    print(MyException.divide_by_null(int(input("Введите делимое: ")), int(input("Введите делитель: "))))
except ValueError:
    print("Вы ввели не число")
