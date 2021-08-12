def user(lastname, firstname, year, city, email, phone):
    print(lastname, firstname, year, city, email, phone)


user(lastname=input("Введите фамилию "), firstname=input("Введите имя "),
     year=input("Введите год рождения "), city=input("Введите город "),
     email=input("Введите email "), phone=input("Введите телефон "))
