class MyError(Exception):
    def __init__(self):
        pass


class StopError(Exception):
    def __init__(self):
        pass


class TypeCheck:
    def __init__(self):
        self.my_list = []

    def check_value(self):
        while True:
            try:
                try:
                    new_list = list(input("Введите список через пробел, для остановки введите stop ").split())
                    for el in new_list:
                        if el == "stop":
                            print(self.my_list)
                            raise StopError
                        else:
                            self.my_list.append(int(el))

                except ValueError:
                    raise MyError
            except MyError:
                ex = input(f"Вы ввели не число! Для продолжения нажмите Enter").lower()


a = TypeCheck()
try:
    a.check_value()
except StopError:
    print("Вы остановили программу")
