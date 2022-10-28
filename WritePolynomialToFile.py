# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: k=2 => 2x^2 + 4x + 5 = 0 или x^2 + 5 = 0 или 10x^2 = 0
from random import randint

k = int(input("Enter power of a polynomial: "))
lst_k = [randint(0, 100) for x in range(k + 1)]
res = ''
for i in range(k):
    if k - i > 1:
        res += f'{lst_k[i]}x^{k - i} + '
    elif k - i == 1:
        res += f'{lst_k[i]}x + '
res += f'{lst_k[len(lst_k) - 1]} = 0'

with open('plnml.txt', 'a') as file:
    file.write(res + '\n')

print(lst_k)
print(res)