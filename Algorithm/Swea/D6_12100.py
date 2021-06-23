import sys
sys.stdin = open("D6_12100_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M, d, e = map(int, input().split())
    arr = [input() for _ in range(N)]
    darr = [input() for _ in range(d)]
    earr = [input() for _ in range(2 * e)]