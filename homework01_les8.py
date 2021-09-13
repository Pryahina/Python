"""Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
(например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных."""


class Date:
    def __init__(self, date_str: str):
        self.date_str = date_str

    @classmethod
    def extract(cls, date_str):
        day, month, year = [int(i) for i in date_str.split('-')]
        return day, month, year

    @staticmethod
    def valid(date_number):
        if 1 <= int(date_number[0]) <= 31:
            if 1 <= int(date_number[1]) <= 12:
                if 2100 >= int(date_number[2]) >= 0:
                    return f"Дата указана верно"
                else:
                    return f"год указан неверно"
            else:
                return f"Месяц указан неверно"
        else:
            return f"День указан неверно"


date_1 = "01-09-2021"
print(f"Преобразование даты {date_1} в числа: {Date.extract(date_1)}")
print(f"Проверка даты {date_1}: {Date.valid(Date.extract(date_1))}")
date_2 = "45-11-2003"
print(f"Проверка даты {date_2}: {Date.valid(Date.extract(date_2))}")
date_3 = "07-18-2005"
print(f"Проверка даты {date_3}: {Date.valid(Date.extract(date_3))}")
date_4 = "05-01-2500"
print(f"Проверка даты {date_4}: {Date.valid(Date.extract(date_4))}")
