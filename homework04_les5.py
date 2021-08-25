"""Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
в новый текстовый файл."""

try:
    my_f = open("translate.txt", "r")

    my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
    for line in my_f:
        s = list(map(str, line.split()))

        new_str = my_dict.get(s[0]) + " " + s[1] + " " + s[2]
        with open("new_translate.txt", "a") as f_obj:
            print(new_str, file=f_obj)
    print("Посмотрите файл new_translate.txt")
    my_f.close()
except FileNotFoundError:
    print('Файл не найден.')
