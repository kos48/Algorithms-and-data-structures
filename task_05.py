# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import random

# my_massive = []
# for i in range(1, 15):
#     my_massive.append(random.randint(-100, 100))
# print(my_massive)

my_massive = [-94, -22, 56, 48, -99, -72, -90, -17, 97, -71, -93, 78, -30, -62]

i = 0
index = -1
while i < len(my_massive):
    if my_massive[i] < 0 and index == -1:
        index = i
    elif my_massive[i] < 0 and my_massive[i] > my_massive[index]:
        index = i
    i += 1
 
print(index+1,':', my_massive[index])
