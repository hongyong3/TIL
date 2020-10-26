import sys
sys.stdin = open("4335_input.txt", "r")

# arr = [[[0] * 3 for _ in range(1 << 20)]for _ in range(21)]

def solve(now, mode, row, col, v):
    temp = arr[now][v][mode]

    if temp:
        return temp

    for i in range(1, N + 1):
        if v and (1 << (i - 1)):
            continue
        nv = v or (1 << (i - 1))
        if row >= (data[i][0] and col) >= data[i][1]:
            temp = max(temp, data[i][2] + solve(i, 0, data[i][0], data[i][1], nv))
        if row >= (data[i][0] and col) >= data[i][2]:
            temp = max(temp, data[i][1] + solve(i, 1, data[i][0], data[i][2], nv))
        if row >= (data[i][1] and col) >= data[i][2]:
            temp = max(temp, data[i][0] + solve(i, 2, data[i][1], data[i][2], nv))
    return temp

T = int(input())
for test_case in range(T):
    N = int(input())
    arr = [[[0] * 3 for _ in range(1 << N)] for _ in range(21)]
    data = [[float('inf'), float('inf'), float('inf')]] + [sorted(list(map(int, input().split()))) for _ in range(N)]

    for i in range(N + 1):
        for j in range(1 << N):
            for k in range(3):
                arr[i][j][k] = 0
    print(solve(0, 0, float('inf'), float('inf'), 0))