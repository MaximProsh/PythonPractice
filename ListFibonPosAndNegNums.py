# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
from random import randint

n = int(input('Enter a number: '))
k = [x for x in range(-n, n + 1)]

def fib(n_pos):
    if n_pos in [1, 2]:
        return 1
    else:
        return fib(n_pos - 1) + fib(n_pos - 2)

def fib_neg(n_neg):
    if n_neg == -1:
        return 1
    elif n_neg == -2:
        return -1
    else:
        return fib_neg(n_neg + 2) - fib_neg(n_neg + 1)

k_f = []
for i in range(len(k)):
    if k[i] > 0:
        k_f.append(fib(k[i]))
    elif k[i] < 0:
        k_f.append(fib_neg(k[i]))
    else:
        k_f.append(k[i])

print(k)
print(k_f)



