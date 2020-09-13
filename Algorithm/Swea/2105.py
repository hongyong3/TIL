import sys
sys.stdin = open("2105_input.txt", "r")

def solve(x, y):
    global mat
    choice = []
    dx = [- 1, - 1, 1, 1]   # 우상향대각 자상향대각 좌하향대각 우하향대각 if : 1 3  % 2 // else: 2 4 % 2
    dy = [1, - 1, - 1, 1]   # 좌상향대각 우상향대각 좌하향대각 우하향대각
    leftarr = arr[0]
    rightarr = arr[1]
    for i in range(4):
        if i % 2:
            for _ in range(1, leftarr):
                x = x + dx[i]
                y = y + dy[i]
                if not (0 <= x < N and 0 <= y < N): return
                if data[x][y] in choice: return
                choice.append(data[x][y])
        else:
            for _ in range(1, rightarr):
                x = x + dx[i]
                y = y + dy[i]
                if not (0 <= x < N and 0 <= y < N): return
                if data[x][y] in choice: return
                choice.append(data[x][y])
    if ans < len(choice):
        ans = len(choice)

def check(x, y, chk, n):
    if n == 2:
        chk = 1
        for i in mat:
            chk *= i
        if chk <= mat:
            return
        else:
            solve(x, y)
    else:
        for i in range(2, N):
            mat[n] = i
            check(x, y, chk, n + 1)

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    mat, mat = - 1, [0] * 2

    for i in range(N):
        for j in range(N):
            if (i == j == 0) or (i == j == N - 1) or (i == 0 and j == N - 1) or (i == N - 1 and j == 0): continue
            check(i, j, 0, 0)
    print("#{} {}".format(test_case + 1, mat))