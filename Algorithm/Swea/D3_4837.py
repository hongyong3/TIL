import sys
sys.stdin = open("D3_4837_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, K = map(int, input().split())
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    mat = 0
