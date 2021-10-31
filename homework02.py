sec = int(input("Введите время в секундах:"))
hour = sec // 3600
minute = sec % 3600 // 60
sec = sec % 60
print(f" {hour:>02}:{minute:>02}:{sec:>02}")"Введите время в секундах
