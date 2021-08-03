sec = int(input("Введите время в секундах:"))
hour = sec // 3600
minute = sec % 3600 // 60
sec = sec % 60
print(f"{hour}:{minute}:{sec}")
