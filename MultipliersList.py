# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
n = int(input("Enter a natural number: "))
lst_m = [i for i in range(2, n // 2 + 1) if n % 2 == 0]
if not lst_m:
    print("The number is prime")
else:
    print(lst_m)