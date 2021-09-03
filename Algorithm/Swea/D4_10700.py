import sys
sys.stdin = open("D4_10700_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    