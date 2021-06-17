#2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

user_number = int(input('Введите число : '))
even=odd=0
while user_number>0:
    if user_number%2 == 0:
        even += 1
    else:
        odd += 1
    user_number = user_number//10
print(f'четных - {even}, нечетных - {odd}')