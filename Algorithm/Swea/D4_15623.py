import sys
sys.stdin = open("D4_15623_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    print(arr)