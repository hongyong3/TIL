import sys
sys.stdin = open("D1_17048_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    print("#{} {}".format(test_case + 1, 1 if N % 2 else 2))