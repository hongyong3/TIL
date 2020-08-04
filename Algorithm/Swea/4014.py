import sys
sys.stdin = open("4014_input.txt", "r")

T = int(input())
for test_case in range(1):
    N, X = map(int, input().split())
    dataRow = [list(map(int, input().split())) for _ in range(N)]
    dataCol = [[element for element in t] for t in zip(*dataRow)]
    ans = 0

    for i in range(N):
        