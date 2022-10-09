# Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

day = int(input("Enter number of a week day: "))
if day >= 1 and day <= 5:
    print("No")
elif day == 6 or day == 7:
    print("Yes")
else:
    print("Invalid input")