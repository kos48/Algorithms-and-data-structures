#4. Определить, какое число в массиве встречается чаще всего.
import random

# my_massive =[20, 79, 60, 35, 30, 1, 9, 20, 45, 79, 43, 79, 2, 4]

my_massive = []
for i in range(1, 1000):
    my_massive.append(random.randint(1, 100))
# print(my_massive)    

max_entry=0

for i in range(len(my_massive)):
    if my_massive.count(my_massive[i]) > my_massive.count(my_massive[i-1]):
        max_entry = my_massive[i]
print(max_entry)
    