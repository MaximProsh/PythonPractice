# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся 
# в файле file.txt в одной строке одно число.
from random import randint

file = open('file.txt')
lst_file = []
lst_file_num = []
lines = file.readlines()

for line in lines:
    temp = line.split()
    lst_file.extend(temp)

for i in lst_file:
    if i != '':
        lst_file_num = lst_file_num + [int(i)]

rnd_list = []
for i in range(10):
    rnd_list.append(randint(-100, 100))

sum = 0
for i in lst_file_num:
    for j in range(len(rnd_list)):
        if i == j:
            sum += rnd_list[j]

print(lst_file_num)
print(rnd_list)
print(sum)