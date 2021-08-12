def my_func(x, y):
    if y > 0:
        return print("у должен быть отрицательным") # сделала проверку y, т.к. по условиям задачи он отриц

    return round(x ** y, 5)


try:
    print(my_func(float(input("Введите первую переменную: ")), int(input("Введите вторую переменную: "))))
except ValueError:
    print("Вы ввели не число")
