# Первая реализация, когда переменные задаются в программе

def my_func(var1, var2, var3):
    minimal = min(var1, var2, var3)
    return var1 + var2 + var3 - minimal


print(my_func(10, 20, 5))


# Вторая реализация, переменные задаются пользователем
def my_func(var1, var2, var3):
    minimal = min(var1, var2, var3)

    return var1 + var2 + var3 - minimal


try:
    print(my_func(int(input("Введите первую переменную: ")), int(input("Введите вторую переменную: ")),
                  int(input("Введите третью переменную: "))))

except ValueError:
    print("Вы ввели не число")
