import sys
sys.stdin = open("D3_1240_input.txt", "r")

T = int(input())
for test_case in range(1):
    N, M = map(int, input().split())
    # data = [input() for _ in range(N)]
    data = [list(map(int, input().split())) for _ in range(N)]
    # data = [list(map(int, input())) for _ in range(N)]
    print(data)