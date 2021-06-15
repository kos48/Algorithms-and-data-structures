#4. Написать программу, которая генерирует в указанных пользователем границах:
#случайное целое число;
#случайное вещественное число;
#случайный символ.
#Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
#Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import datetime, string

date_random_number=str(datetime.datetime.now()) #воспользуемся датой для случайного числа
random_number=int(date_random_number[24:])
int_number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
act = int(input('Введите что хотите сгенерировать?:\n 1 - случайное целое число \n 2 - случайное вещественное число \n 3 - случайный символ \n :'))
print(act)
if act == 1:
    print('генерируем случайное целое число')
    #создадим список тцелых чисел
    
    #пользователь вводит диапазон чисел
    user_range_from = int(input(f' Введите с какого числа :'))
    user_range_to = int(input(f'Введите до какого числа :'))
    #создаю список чисел диапазона
    user_int_number = int_number[user_range_from  : user_range_to +1]
    len_user_number = len(user_int_number) # определяем длину этого списка
    print (f' Сгенерированное число = {user_int_number[random_number % len_user_number]}')

elif act == 2:
    print('генерируем случайное вещественное число')
    user_range_from = int(input(f' Введите с какого числа :'))
    user_range_to = int(input(f'Введите до какого числа :'))
    #сгенерируем целую часть числа
    user_int_number = int_number[user_range_from  : user_range_to +1]
    len_user_number = len(user_int_number) # определяем длину этого списка
    #сгенерируем дробную часть(можно было бы добавить генерацию сколько знаков после запятой, но времени не хватает!!!)
    date_random_number=str(datetime.datetime.now()) #воспользуемся датой для случайного числа
    random_number=int(date_random_number[24:])
    user_float_number = str(user_int_number[random_number % len_user_number])
    user_float_number = float(user_float_number +'.' + str(random_number))
    print(f'Сгенерированное вещественное число : {user_float_number}')
    
else:
    print('генерируем случайный символ английского алфавита')
    symbol_list= string.ascii_lowercase
    range_symbol_from = input(f' Введите с какого символа :')
    range_symbol_to = input(f' Введите до какого символа :')
    len_range = (symbol_list.index(range_symbol_to) + 1) - (symbol_list.index(range_symbol_from) + 1) + 1
    print (f'Сгенерированный символ = {symbol_list[symbol_list.index(range_symbol_from) + (random_number % len_range)]}')
    