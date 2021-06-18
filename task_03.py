#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

# my_massive = []
# for i in range(1, 10):
#     my_massive.append(random.randint(1, 100))
my_massive =[20, 79, 60, 35, 30, 1, 9, 20, 45]
print(my_massive)
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

my_massive[max_idx], my_massive[min_idx] = my_massive[min_idx], my_massive[max_idx]

print(my_massive)
