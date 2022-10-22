# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: - [2, 3, 4, 5, 6] => [12, 15, 16]; - [2, 3, 5, 6] => [12, 15]
from random import randint

lst = [randint(1, 50) for x in range(randint(2, 15))]
lst_mult = []
for i in range(len(lst) // 2):
    lst_mult.append(lst[i] * lst[-(i + 1)])
print(lst)
print(lst_mult)