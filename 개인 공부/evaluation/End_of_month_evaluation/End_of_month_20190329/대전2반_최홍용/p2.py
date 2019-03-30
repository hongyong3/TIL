import sys
sys.stdin = open("p2_input.txt", "r")

# def sum(x, y, sums):
#     global max
#     if sums > max:
#         max = sums





T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    ans = []
    max = 0
    for i in range(N):
        for j in range(i:N)