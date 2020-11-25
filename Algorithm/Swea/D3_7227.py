import sys
sys.stdin = open("D3_7227_input.txt", "r")

'''
나올 수 있는 경우의 수
nC(n//2) // 2
'''
case = [0, 1, 3, 10, 35, 126, 462, 1716, 6435, 24310, 92378]

def solve(n, cnt):
    global ans, c

    if not c or not ans:
        return
    if cnt == N // 2:
        c -= 1
        x, y = 0, 0
        for i in range(N):
            if chk[i]:
                x += data[i][0]
                y += data[i][1]
            else:
                x -= data[i][0]
                y -= data[i][1]
        if ans > x * x + y * y:
            ans = x * x + y * y
        return

    for i in range(n, N):
        if not chk[i]:
            chk[i] = 1
            solve(i + 1, cnt + 1)
            chk[i] = 0

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    ans = float('inf')
    chk = [0] * N
    c = case[N // 2]
    solve(0, 0)
    print("#{} {}".format(test_case + 1, ans))