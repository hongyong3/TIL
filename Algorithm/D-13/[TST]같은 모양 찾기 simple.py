import sys
sys.stdin = open('같은 모양 찾기_input.txt', 'r')
T = int(input())
data = [list(map(int, input())) for i in range(T)]
X = int(input())
ans = [list(map(int, input())) for i in range(X)]
count = 0
stack = []

for y in range(0,T-X+1):
    for x in range(0,T-X+1):
        for i in range(X):
            stack.append(data[y+i][x:x +X])
        if stack == ans:
            count += 1
        stack = []

print(count)