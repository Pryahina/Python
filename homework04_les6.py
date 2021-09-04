""".Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости."""


class Car:
    speed: float
    color: str
    name: str
    is_police: bool

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"машина {self.name} поехала"

    def stop(self):
        return f"\nмашина {self.name} остановилась"

    def turn(self, direction):
        return f"\nмашина {self.name} повернула {direction}"

    def show_speed(self):
        return f"\nСкорость машины: {self.speed}"


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f"\nВнимание! Превышение скрости! Скорость машины: {self.speed}"
        else:
            return f"\nСкорость машины: {self.speed}"


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f"\nВнимание! Превышение скрости! Скорость машины: {self.speed}"
        else:
            return f"\nСкорость машины: {self.speed}"


class PoliceCar(Car):
    pass


t = TownCar(60, "красный", "Ford Focus", False)
print('1:\n' + t.go(), t.show_speed(), t.turn("налево"), t.turn("направо"), t.stop())

s = SportCar(150, "желтый", "Porche", False)
print('2:\n' + s.go(), s.show_speed(), s.turn("налево"), s.stop())

w = WorkCar(50, "оранжевый", 'Kamaz', False)
print('3:\n' + w.go(), w.show_speed(), w.turn("направо"), w.stop())

p = PoliceCar(90, "белый", "BMW", True)
print('4:\n' + p.go(), p.show_speed(), p.turn("налево"), p.stop())
