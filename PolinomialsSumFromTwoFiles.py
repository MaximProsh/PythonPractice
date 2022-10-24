# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
path = 'plnml1.txt'
file = (open(path, 'r'))
poly1 = list(file)
file.close()

path = 'plnml2.txt'
file = (open(path, 'r'))
poly2 = list(file)
file.close()

res = ''
for i in poly1[0]:
    if i == '=':
        break
    else:
        res += i

res += '+ '

for i in poly2[0]:
    if i == '=':
        break
    else:
        res += i

with open('sum_plnml.txt', 'a') as file:
    file.write(res)