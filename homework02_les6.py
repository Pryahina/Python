"""Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна. Проверить работу метода."""


class Road:
    _length: int
    _width: int
    weight: int
    thickness: int

    def __init__(self, length, width, weight=25, thickness=5):
        self._width = width
        self._length = length
        self.weight = weight
        self.thickness = thickness

    def calculate(self):
        return self._length * self._width * self.weight * self.thickness


r = Road(length=5000, width=20)
print(f"Масса асфальта: {r.calculate()/1000} т")
