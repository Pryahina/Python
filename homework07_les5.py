"""Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна
содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь
(со значением убытков)."""


import json

try:
    with open('firm.txt', 'r+') as file:
        statistics = []
        profit = {}
        average_profit = {}
        av = 0
        prof = 0
        i = 3
        for line in file:
            name, form, revenue, damage = line.split()
            total = int(revenue) - int(damage)
            if total >= 0:
                prof = prof + total
            else:
                i -= 1
            profit[name] = total
        statistics.append(profit)
        if i != 0:
            (av) = prof / i
            average_profit['average_profit'] = round(av)
            statistics.append(average_profit)
        else:
            print('Все компании работают в убыток')
            print(statistics)
    with open('file.json', 'a+') as json_file:
        json.dump(statistics, json_file)
    print("Посмотрите файл file.json")
except FileNotFoundError:
    print('Файл не найден.')
