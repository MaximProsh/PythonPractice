# Вычислить число c заданной точностью d
# Пример: при d = 0.001, π = 3.142 10^(-1) ≤ d ≤10^(-10)

n = float(input("Enter a floating point number: "))
d = input("Enter a fixed precision number: ")
d_res = 0
for i in d:
    if i == '.':
        d_res = 0
    else:
        d_res += 1

print(round(n, d_res))