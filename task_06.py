#6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток.
#После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано.
#Если за 10 попыток число не отгадано, то вывести загаданное число.
import random

random_number = random.randint(0, 100)
print(random_number)
for i in range(1, 11):
    print(i)
    user_number = int(input(f'Попытка № {i} Введите число от 0-100 :'))
    if user_number == random_number :
        print(f'Вы угадали, с {i} попытки!!!')
        break
    elif user_number > random_number:
        print('загаданное число меньше вашего!!!')
    elif user_number < random_number:
        print('загаданное число больше вашего!!!')
    if i == 10:
        print(f'загаданное число = {random_number}')
