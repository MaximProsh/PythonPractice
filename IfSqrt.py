# Напишите программу, которая принимает на вход два числа
# и проверяет, является ли одно число квадратом другого.

from fcntl import F_GETLK64


a = int(input(("Input first number: ")))
b = int(input(("Input second number: ")))
c = 0
d = 0

if a ** 2 == b:
    print(f"Num {b} is sqrt of num {a}")
    c = 1
if b ** 2 == a:
    print(f"Num {a} is sqrt of num {b}")
    d = 1
if c == 1 and d == 1:
    print("Nums are not sqrt for each other")