import sys

sys.stdin = open("D5_17324_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
