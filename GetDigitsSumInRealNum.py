# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

n = input("Enter a real number: ")
sum = 0
for i in n:
    if i.isdigit():
        sum += int(i)
print(sum)