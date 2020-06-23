import sys
sys.stdin = open("2112_input.txt", "r")

import itertools

T = int(input())
for test_case in range(1):
    D, W, K = map(int, input().split())
    ans = 0
    data = [list(map(int, input().split())) for _ in range(D)]