import sys
sys.stdin = open("D4_8822_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, X = map(int, input().split())
    print("#{} {}".format(test_case + 1, 0 if X == (1 or 2 * N - 1) else 1))