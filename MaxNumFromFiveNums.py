from random import randint
array = []

for x in range(5):
    rnd = randint(1, 100)
    array.append(rnd)
print(array)

max = 0
for x in array:
    if x > max:
        max = x
print(max)
