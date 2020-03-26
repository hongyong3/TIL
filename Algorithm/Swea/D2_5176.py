import sys
sys.stdin = open("D2_5176_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    tree = [[0] * 3 for _ in range(N + 2)]

    