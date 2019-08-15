import sys
sys.stdin = open("D3_6057_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(M)]
    temp = [[0] * N  for _ in range(2)]
    for i in range(N):
        temp[data[i][0]]