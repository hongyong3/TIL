# 4등분하자
def one(x, y):
    apple = 0
    for i in range(x):
        for j in range(y, N):
            apple += data[i][j]
    return apple

def two(x, y):
    apple = 0
    for i in range(x):
        for j in range(y):
            apple += data[i][j]
    return apple

def three(x, y):
    apple = 0
    for i in range(x, N):
        for j in range(y):
            apple += data[i][j]
    return apple

def four(x, y):
    apple = 0
    for i in range(x, N):
        for j in range(y, N):
            apple += data[i][j]
    return apple

import sys
sys.stdin = open("과수원_input.txt", "r")
N = int(input())
data = [list(map(int, input())) for _ in range(N)]
count = 0

for i in range(1, N):
    for j in range(1, N):
        if one(i, j) == two(i, j) and two(i, j) == three(i, j) and three(i, j) == four(i, j):
            count += 1

if count == 0:
    print(-1)
else:
    print(count)