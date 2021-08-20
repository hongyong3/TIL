import sys
sys.stdin = open("D3_12322_input.txt", "r")

def solve(x, y, size):
    if size == 1:
        ans[arr[x][y]] += 1
        return
    chk = [0, 0]
    for i in range(x, x + size):
        for j in range(y, y + size):
            chk[arr[i][j]] = 1
    if chk[0] and chk[1]:
        solve(x, y, size // 2)
        solve(x + size // 2, y, size // 2)
        solve(x, y + size // 2, size // 2)
        solve(x + size // 2, y + size // 2, size // 2)
    elif chk[0]:
        ans[0] += 1
    else:
        ans[1] += 1

T = int(input())
for test_case in range(T):
    N = int(input())
    ans = [0, 0]
    arr = [list(map(int, input().split())) for _ in range(N)]
    solve(0, 0, N)
    print("#{}".format(test_case + 1), *ans)
    