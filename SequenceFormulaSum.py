# Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.

n = int(input("Enter a number: "))
sum = 0
for i in range(1, n + 1):
    app_num = (1 + 1 / i) ** i
    sum += app_num
    app_num = 0
print(sum)