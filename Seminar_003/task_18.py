# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент 
# к заданному числу X. Пользователь в первой строке вводит натуральное число N – 
# количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random
n = int(input("Ведите количество элементов в массиве -> "))
print(n)
arrayA = [random.randint(0, n) for i in range(n)]
print(arrayA)
number_x = int(input("Введите некоторое число Х -> "))
print(number_x)
nearby_min = abs(number_x - arrayA[0])
index = 0
for i in range(1, n):
    count = abs(number_x - arrayA[i])
    if count < nearby_min:
        nearby_min = count
        index = i
print(f'Число {arrayA[index]} в массиве A наиболее близко по величине к числу {number_x}')
        

