# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.
# Пример: - [1.1, 1.2, 3.1, 5, 10.01] => 0.2
from random import randint, uniform

lst = [round(uniform(0, 20), 2) for x in range(randint(2, 10))]
lst_f = [round(i % 1, 2) for i in lst]
min, max = lst_f[0], 0
for i in lst_f:
    if min > i:
        min = i
    if max < i:
        max = i

print(f"The start list is: {lst}")
print(f"The fractional parts list is: {lst_f}")
print(f"Difference between min ({min}) and max ({max}) parts is {max - min}")