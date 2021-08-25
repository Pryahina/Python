"""Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке."""
try:
    my_f = open("my_file.txt", "r")
    count_str = 0
    for line in my_f:
        count_str += 1
        print(f"В строке {count_str} количество слов: {len(line.split())}")
    my_f.close()

    print(f"Количество строк в файле: {count_str}")
except FileNotFoundError:
    print('Файл не найден.')
