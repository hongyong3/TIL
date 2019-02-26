import sys
sys.stdin = open("피자 굽기_input.txt", "r")
T = int(input())
for test_case in range(1, T+1):
    N, M = list(map(int, input().split()))
    data = list(input().split())
    Q = [0] * N
    i = 0
