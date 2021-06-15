#6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
import string
symbol_list= string.ascii_lowercase
print(symbol_list)
user_symbol = input('Введите номер буквы :')
print(symbol_list[int(user_symbol)-1])
