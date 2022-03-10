import sys
sys.stdin = open("D3_13732_input.txt", "r")

def solve(r, c):
    idx, jdx = 0, 0
    while r + idx < N:
        if arr[r + idx][c] == '#':
            idx += 1
        else:
            break

    while c + jdx < N:
        if arr[r][c + jdx] == '#':
            jdx += 1
        else:
            break

    if idx != jdx:
        return 'no'

    for x in range(r, r + idx):
        for y in range(c, c + jdx):
            visited[x][y] = 1
            if arr[x][y] == '.':
                return "no"

    return "yes"

T = int(input())
for test_case in range(T):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    chk = True
    ans = 'yes'

    for i in range(N):
        for j in range(N):
            if arr[i][j] == '#' and not visited[i][j]:
                if chk:
                    chk = False
                    ans = solve(i, j)
                else:
                    ans = 'no'
                    break

    print("#{} {}".format(test_case + 1, ans))