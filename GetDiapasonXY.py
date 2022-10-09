# Напишите программу, которая по заданному номеру четверти, показывает 
# диапазон возможных координат точек в этой четверти (x и y).

num_quart = int(input("Enter quarter number from 1 to 4: "))

if num_quart == 1:
    print("The diapason first qaurter is: \nX: 0 - +∞ \nY: 0 - +∞")

if num_quart == 2:
    print("The diapason second qaurter is: \nX: 0 - -∞ \nY: 0 - +∞")

if num_quart == 3:
    print("The diapason third qaurter is: \nX: 0 - -∞ \nY: 0 - -∞")

if num_quart == 4:
    print("The diapason fourth qaurter is: \nX: 0 - +∞ \nY: 0 - -∞")

if num_quart < 1 or num_quart > 4:
    print("Invalid input")