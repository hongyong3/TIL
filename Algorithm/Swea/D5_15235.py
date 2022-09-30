import sys
sys.stdin = open("D5_15235_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    NArr = [list(map(str, input().split())) for _ in range(N)]
    print(NArr)