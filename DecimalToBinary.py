# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример: - 45 -> 101101; - 3 -> 11; - 2 -> 10
n = int(input('Enter number: '))
num = n
bin = []
while n >= 1:    
    if n % 2 == 0:
        bin.append(0)
    else:
        bin.append(1)
    n = n // 2

res = ''
for i in range(len(bin)):
    res += str(bin[-(i + 1)])

print(f"Decimal: {num}, binary: {res}")