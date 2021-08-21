from itertools import cycle

my_list = ["раз", "два", "три"]
iter = cycle(my_list)

try:
    count = int(input("Сколько слов вывести: "))
except ValueError:
    print("Вы ввели не число")
    exit()

i = 0
while i < count:
    print(next(iter))
    i += 1
