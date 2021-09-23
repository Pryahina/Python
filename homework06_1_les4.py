from itertools import count

try:
    number_start = int(input("Введите число с которого начинать: "))
    number_end = int(input("Введите до какого числа генерировать: "))
except ValueError:
    print("Вы ввели не число")
    exit()
for el in count(number_start):
    if el > number_end:
        break
    else:
        print(el)
