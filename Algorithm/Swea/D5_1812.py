import sys
sys.stdin = open("D5_1812_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))