# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

my_massive = [8, 3, 15, 6, 4, 2]
idx_massive = []

i = 0       
while i < len(my_massive):
    if my_massive[i] % 2 == 0:
        idx_massive.append(i)
    i +=1
print(idx_massive)