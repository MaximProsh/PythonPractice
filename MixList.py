# Реализуйте алгоритм перемешивания списка.
import random
start_lst = [random.randint(-50, 50) for i in range(8)]
finish_lst = random.sample(start_lst, len(start_lst))
print(start_lst)
print(finish_lst)