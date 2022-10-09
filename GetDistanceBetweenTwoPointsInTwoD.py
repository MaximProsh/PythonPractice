# Напишите программу, которая принимает на вход координаты двух точек и 
# находит расстояние между ними в 2D пространстве.
from math import sqrt

x1 = int(input("Input coordinate X for A point: "))
y1 = int(input("Input coordinate Y for A point: "))
x2 = int(input("Input coordinate X for B point: "))
y2 = int(input("Input coordinate Y for B point: "))

d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(round(abs(d), 2))
