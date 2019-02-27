import sys
sys.stdin = open('색종이(초)_input.txt', 'r')
T = int(input())
data = [[0 for _ in range(101)] for _ in range(101)]
count = 0
for test_case in range(T):
    N, M = map(int, input().split())
    for i in range(N, (N + 10)):
        for j in range(M, (M + 10)):
            data[i][j] = 1
for i in range(len(data)):
    for j in range(len(data)):
        if data[i][j] == 1:
            count += 1
print(count)