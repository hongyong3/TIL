import sys
sys.stdin = open("참외 밭_input.txt", "r")
T = int(input())
field = []
order=[]
for i in range(6):
    a, b = map(int, input().split())
    order.append(a)
    field.append(b)

stack=[]
big = 1
small = 1
for i in order:
    if order.count(i) == 2 and i not in stack:
        stack.append(i)
for i in range(6):
    if order[i] in stack:
        if order[(i+1)%6] in stack and order[(i-1)%6] in stack:
            small *= field[i]
    else:
        big*=field[i]

print((big-small)*T)