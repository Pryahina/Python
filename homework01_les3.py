def div():
    try:
        var1 = float(input("Введите первую переменную: "))
        var2 = float(input("Введите вторую переменную: "))
    except ValueError:
        return print("Вы ввели не число")

    rez = round(var1 / var2, 2)

    return rez


try:
    print(div())
except ZeroDivisionError:
    print("На ноль делить нельзя")
