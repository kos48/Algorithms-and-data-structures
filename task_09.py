# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import random
M = 5
N = 5
my_matrix = []
for i in range(N):
    b = []
    for j in range(M):
        n = int(random()*200)
        b.append(n)
        print(n, ' ', end='')
    my_matrix.append(b)
    print()
    
mx = -1
for j in range(M):
    mn = 200
    for i in range(N):
        if my_matrix[i][j] < mn:
            mn = my_matrix[i][j]
    if mn > mx:
        mx = mn
print("Максимальный среди минимальных: ", mx)
    

