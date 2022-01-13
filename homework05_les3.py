def my_func():
    rez = 0
    global symbol
    global m
    m = 0
    symbol = 0
    my_list = list(input("Введите список через пробел, для остановки введите f ").split())
    for el in my_list:
        if el == "f":
            symbol = "f"
            m = rez
            return symbol, m
        else:
            el = int(el)
            rez = rez + el

    return rez


total = 0
try:
    while True:
        k = my_func()
        if symbol == "f":
            break
        else:
            total = total + k

    print(total + m)

except ValueError:
    print("Вы ввели не число")