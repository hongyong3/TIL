import sys
sys.stdin = open("D2_1983_input.txt", "r")

T = int(input())
for test_case in range(T):
    avg = 0
    N, M = list(map(int, input().split()))
    data = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        avg = int((data[M][0] * 0.35 + data[M][1] * 0.45 + data[M][2] * 0.2))
        if avg 