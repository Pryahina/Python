def salary(work_time, tarif, bonus):
    print("Выработка в часах: ", work_time)
    print("Ставка в час: ", tarif)
    print("Премия: ", bonus)
    total = int(work_time) * int(tarif) + int(bonus)
    print("Зарплата: ", total)
