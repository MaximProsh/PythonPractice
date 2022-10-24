# Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности.

lst_start = [3, 3, 5, 'Уфа', 6, 9, 'Work', 13, 'Уфа', 9]
lst_finish = [i for i in lst_start if not lst_start.count(i) > 1]
print(lst_start)
print(lst_finish)