import sys
sys.stdin = open("D3_8888_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M, K = map(int, input().split())
    people = [[0, 0, 0] for _ in range(N)]
    score = [0] * M
    for i in range(N):
        t = 