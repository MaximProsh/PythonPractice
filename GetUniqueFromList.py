# Дана последовательность чисел. Получить список уникальных элементов заданной 
# последовательности, список повторяемых и убрать дубликаты из заданной последовательности.

lst = [1, 2, 3, 5, 1, 5, 3, 10]
unique = [i for i in lst if lst.count(i) == 1]
repeats_num = [x for i, x in enumerate(lst) if i != lst.index(x)]
del_repeat = list(set(lst))

print(unique, repeats_num, del_repeat)