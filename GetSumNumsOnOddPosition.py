# Задайте список из нескольких чисел. Напишите программу, которая найдёт 
# сумму элементов списка, стоящих на нечётной позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from random import randint

lst = [randint(1, 50) for x in range(randint(2, 15))]
lst_odd = []
sum = 0
for i in range(len(lst)):
    if i % 2 == 0:
        lst_odd.append(lst[i])
        sum += lst[i]

print("Start list:", lst)
print(f"Numbers on odd position: {lst_odd}. Numbers sum on odd positions: {sum}")