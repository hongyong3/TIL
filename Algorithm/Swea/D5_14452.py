import sys
sys.stdin = open("D5_14452_input.txt", "r")

T = int(input())
for test_case in range(T):
    X, N, Y, M = map(int, input().split())