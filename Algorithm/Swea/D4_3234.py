import sys
sys.stdin = open("D4_3234_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    left, right, count = 0, 0, 0