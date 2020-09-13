import sys
sys.stdin = open("D6_1260_input.txt", "r")

def search(x, y):
    global mat
    dx, dy = 0, 0
    while x + dx < N and data[x + dx][y]:
        dx += 1
    while y + dy < N and data[x][y + dy]:
        dy += 1

    for i in range(x, x + dx):
        for j in range(y, y + dy):
            data[i][j] = 0

    mat.append(dx)
    mat.append(dy)


T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    mat = []
    m = [[0] * 501 for _ in range(501)]

    for i in range(N):
        for j in range(N):
            if data[i][j]:
                search(i, j)

    arr = []
    while mat:
        for i in range(len(mat) // 2):
            if mat.count(mat[2 * i]) == 1:
                arr.append(mat.pop(2 * i))
                arr.append(mat.pop(2 * i))
                break

    print(arr)
    n = len(arr) // 2

    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
                m[i][j] = min(m[i][j], cost)
    print(m[1][n])