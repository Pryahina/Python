"""Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники."""


class OfficeEquipment:  # базовый класс "Оргтехника"

    def __init__(self, price: int, id_number: int):  # у каждой оргтехники определена цена и id номер
        self.price = price
        self.id_number = id_number


class Printer(OfficeEquipment):  # класс принтеров, printer_name - уникальный параметр для принтера
    def __init__(self, printer_name: str, price: int, id_number: int):
        super().__init__(price, id_number)
        self.printer_name = printer_name


class Scanner(OfficeEquipment):  # класс сканеров, scanner_name - уникальный параметр для сканера
    def __init__(self, scanner_name: str, price: int, id_number: int):
        super().__init__(price, id_number)
        self.scanner_name = scanner_name


class Xerox(OfficeEquipment):  # класс ксероксов, xerox_name - уникальный параметр для ксерокса
    def __init__(self, xerox_name, price, id_number):
        super().__init__(price, id_number)
        self.xerox_name = xerox_name


class CapacityException(Exception):  # класс - исключения для проверки склада
    def __init__(self, current, needle):
        self.current = current
        self.needle = needle


class EquipmentStock:  # склад для оргтехники
    max_count: int
    equipment: list

    def __init__(self, count=0):
        self.max_count = count
        self.equipment = []

    def store(self, equipment: list):  # проверка можно ли поместить технику на склад
        if len(self.equipment) >= self.max_count:
            raise CapacityException(len(self.equipment), len(self.equipment) + len(equipment))
        elif len(equipment) > (self.max_count - len(self.equipment)):
            raise CapacityException(self.max_count, len(self.equipment) + len(equipment))

        else:
            print(f"Осталось свободных мест на складе: {self.max_count - len(equipment)}")


stock = EquipmentStock(2)  # определяем вместимость склада (можно поменять цифру, будет другое сообщение)

equipment_list = [Printer("Принтер лазерный HP Laser 107r", 5000, 342423), # Заводим новую оргтехнику
                  Scanner("Сканер EPSON Perfection V19", 4000, 353523),
                  Xerox("Ксерокс XEROX Phaser 3020", 3000, 434533)]
try:
    stock.store(equipment_list)  # добавляем технику на склад и проверяем поместиться ли на складе
except CapacityException:
    print("На складе не хватает места")


