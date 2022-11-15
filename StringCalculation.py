# Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный.
# Добавьте возможность использования скобок, меняющих приоритет операций.

# 1. Через функцию eval
print(eval(input('Enter mathematical expression: ')))

# 2. Попытка решить с помощью алгоритма сортировочной станции.
# Попытка неудачная и незавершенная, запутался и надо разбираться. Оставляю 
# для преподавательского интереса :)

exp = input('Enter mathematical expression: ')
exp_lst = (exp.split())
print(exp_lst)

rank = {"^": 3, "/": 2, "*": 2, "+": 1, "-": 1}
output = []
stack = []

for i in exp_lst:
    if i.isdigit():
        output.append(i)
    elif i in rank:
        if not stack:
            stack.append(i)
        elif rank.get(stack[-1]) < rank.get(i):
            stack.append(i)
        elif rank.get(stack[-1]) == rank.get(i):
            output.append(stack[-1])
            stack.append(i)
            stack.pop(-1)
        elif rank.get(stack[-1]) > rank.get(i):
            output.append(stack[-1])
            stack.pop()     
while stack:
    output.append(stack[-1])
    stack.pop()

print(output)
print(stack)

# Вычисление из постфиксной записи 
result = 0
stack_fin = []     
for i in output:
    if i.isdigit():
        stack_fin.append(i)
    if i in rank:
        tmp = eval(str(f'{stack_fin[-2]} {i} {stack_fin[-1]}'))
        result += tmp
        stack_fin.pop(-2)
        stack_fin.pop(-1)

print(result)
    



