import sys
sys.stdin = open("D2_1986_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    if N % 2 == 1:
        print("#{} {}".format(test_case + 1, int(N / 2 + 1)))
    else:
        print("#{} {}".format(test_case + 1,  - int(N / 2)))