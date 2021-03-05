import sys
sys.stdin = open("D2_11608_input.txt", "r")

def solve(idx, total):
    global ans
    if idx == N:
        if ans > total:
            ans = total
    if total > ans:
        return
    for i in range(N):
        if not chk[i]:
            chk[i] = 1
            solve(idx + 1, total + data[idx][i])
            chk[i] = 0

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    chk = [0] * N
    ans = float('inf')
    solve(0, 0)
    print("#{} {}".format(test_case + 1, ans))