# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

arr = [random.randint(0, 100) for i in range(random.randint(10,20))]
print(arr)
max_num = int(input("Заданный максимум равен "))
min_num = int(input("Заданный минимум равен "))
masiv = []

if max_num >= min_num:
   for i in range(len(arr)):
      if max_num >= arr[i] and min_num <= arr[i]:
          masiv.append(i)
print("Индексы элементов массива, значения которых принадлежат заданному массиву: ", masiv)