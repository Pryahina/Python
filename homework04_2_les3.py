def my_func(x, y):
    rez = x
    if y > 0:
        return print("у должен быть отрицательным")

    else:
        for el in range(0, abs(y)+1):
            rez = rez / x

        return round(rez, 5)


try:
    print(my_func(float(input("Введите x: ")), int(input("Введите y: "))))
except ValueError:
    print("Вы ввели не число")
