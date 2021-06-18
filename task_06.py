# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random

my_massive = []
for i in range(1, 20):
    my_massive.append(random.randint(1, 100))
print(my_massive)

# my_massive = [30, 42, 43, 30, 89, 92, 3, 3, 2, 3, 23, 53, 26, 61, 79, 73, 35, 66, 35, 81, 61]
max_number = 0
min_number = my_massive[0]
i = 0
max_idx = 0
min_idx = 0

for el in my_massive:
    if max_number < el:
        max_number = el
        max_idx = i
    elif min_number > el:
        min_number = el
        min_idx = i
    i +=1

print(f'max={max_number} idx={max_idx}, min={min_number} idx={min_idx}')
if min_idx > max_idx:
    min_idx, max_idx = max_idx, min_idx

print(sum(my_massive[min_idx + 1 : max_idx]))

