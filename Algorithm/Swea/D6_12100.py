import sys
sys.stdin = open("D6_12100_input.txt", "r")

dx = [- 1, 1, 0, 0]
dy = [0, 0, - 1, 1]

T = int(input())
for test_case in range(T):
    N, M, d, e = map(int, input().split())
    arr = [input() for _ in range(N)]
    proc = [input() for _ in range(d)]
    program = [input() for _ in range(2 * e)]