import sys
sys.stdin = open("D2_1285_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    