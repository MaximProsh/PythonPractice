# Напишите программу, удаляющую из текста все слова, 
# в которых присутствуют все буквы "абв".
with open('delabv.txt') as file:
    start_text = file.read()

lst = start_text.split()
# print(lst)
abv = ['a', 'б', 'в', 'А', 'Б', 'В']
final_text = ''

for i in lst:
    count = 0
    for j in range(len(i)):
        if i[j] in abv:
            count += 1
    if count == 0:
        final_text += i + ' '

print(final_text)

with open('delabv_f.txt', 'a') as file:
    file.write(final_text)