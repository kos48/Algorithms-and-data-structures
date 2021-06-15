#8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.

user_year = int(input('введите год : '))
if user_year % 4 != 0:
    print("Обычный")
elif user_year % 100 == 0:
    if user_year % 400 == 0:
        print("Високосный")
    else:
        print("Обычный")
else:
    print("Високосный")