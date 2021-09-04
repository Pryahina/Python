"""Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname,
position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
 на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров)."""


class Worker:
    name: str
    surname: str
    position: str
    _income: dict


class Position(Worker):

    def __init__(self, name, surname, wage, bonus):
        self.name = name
        self.surname = surname
        self._income = {'wage': wage, 'bonus': bonus}

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


p = Position(name="Светлана", surname="Иванова", wage=50000, bonus=5000)

print(f"Полное имя сотрудника: {p.get_full_name()}")
print(f"Доход: {p.get_total_income()}")
