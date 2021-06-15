#5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

import string
symbol_list= string.ascii_lowercase
start_symbol=input('Введите первый символ : ')
finish_symbol = input('введите конечный символ : ')
#выщитываем сколько между ними букв
difference = (symbol_list.find(finish_symbol))-(symbol_list.find(start_symbol))-1
print(f'{start_symbol} = {symbol_list.find(start_symbol)+1} , {finish_symbol} = {symbol_list.find(finish_symbol)+1}\nмежду ними {difference} символов')
