import sys
sys.stdin = open("D3_3431_input.txt", "r")

T = int(input())
for test_case in range(T):
    L, U, X = map(int, input().split())
    if L <= X <= U:
        print("#{} {}".format(test_case + 1, 0))
    elif X < L:
        print("#{} {}".format(test_case + 1, L - X))
    elif X > U:
        print("#{} {}".format(test_case + 1, - 1))