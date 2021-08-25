"""Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""


with open("number.txt", "w") as f_obj:
    print("1 2 3 4 5 25 40", file=f_obj)
with open("number.txt", "r") as f_obj:
    s = f_obj.read()
    s = list(map(str, s.split()))
i = 0
total = 0
while i < len(s):
    total = total + float(s[i])
    i += 1

print(f"Сумма чисел в файле number.txt: {total}")

