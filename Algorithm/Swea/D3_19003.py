import sys
sys.stdin = open("D3_19003_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    arr = [input() for _ in range(N)]
    # arr = list(map(int, input().split()))
