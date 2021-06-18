# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

# import random
# 
# my_massive = []
# for i in range(1, 20):
#     my_massive.append(random.randint(1, 100))
# print(my_massive)

my_massive = [30, 42, 43, 30, 89, 92, 3, 3, 2, 3, 23, 53, 26, 61, 79, 73, 35, 66, 35, 81, 61]


min_number = my_massive[0]
i = 0

min_idx = 0

for el in my_massive:
    if min_number > el:
        min_number = el
        min_idx = i
    i +=1

min_number_next = my_massive[0]    

for el in my_massive:
    if min_number > min_number_next > el :
        print(el)
        min_number_next = el
#         min_idx = i


print(f'min={min_number} min_next={min_number_next}')



