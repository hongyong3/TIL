import sys
sys.stdin = open("D2_1983_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, K = list(int(input().split()))
    data = list(map(int, input().split()))