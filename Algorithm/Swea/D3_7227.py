import sys
sys.stdin = open("D3_7227_input.txt", "r")

'''
나올 수 있는 경우의 수
nC(n//2) % 2?
'''
def solve(n, cnt):
    if cnt == N // 2:
        pass

    for i in range(N):
        if not chk[i]:
            chk[i] = 1
            solve(n + 1, cnt + 1)
            chk[i] = 0

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    ans = float('inf')
    chk = [0] * N