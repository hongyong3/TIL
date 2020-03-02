import sys
sys.stdin = open("D1_6295_input.txt", "r")

N, M = map(int, input().split(', '))
arr = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        arr[i][j] = i * j
print(arr)