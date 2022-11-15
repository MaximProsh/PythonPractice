# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока 
# делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента 
# достаются сделавшему последний ход.
from random import randint

def gamerin(name):
    x = int(input(f"{name}, how many candies you'll take (1-28): "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, enter correct number: "))
    return x

def step_result(gamer, took, summary, ontable):
    print(f"{gamer} took {took} candies, he have {summary}. On the table {ontable} candies.")

gamer1 = input("Enter first gamer's name: ")
gamer2 = input("Enter second's gamer's name: ")
candies_sum = int(input("How many candies is on the table: "))
who_first = randint(0,1)

if who_first:
    print(f"{gamer1} go first")
else:
    print(f"{gamer2} go first")

summary1 = 0 
summary2 = 0

while candies_sum > 28:
    if who_first:
        took = gamerin(gamer1)
        summary1 += took
        candies_sum -= took
        who_first = False
        step_result(gamer1, took, summary1, candies_sum)
    else:
        took = gamerin(gamer1)
        summary2 += took
        candies_sum -= took
        who_first = True
        step_result(gamer2, took, summary2, candies_sum)

if who_first:
    print(f"Winner is {gamer1}")
else:
    print(f"Winner is {gamer2}")