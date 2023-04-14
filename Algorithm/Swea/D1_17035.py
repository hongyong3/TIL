import sys
sys.stdin = open("D1_17035_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    print("#{} {}".format(test_case + 1, N + M))
    