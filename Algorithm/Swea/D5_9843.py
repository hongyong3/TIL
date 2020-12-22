import sys
sys.stdin = open("D5_9843_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    temp = int(pow(2 * N, 0.5))
    print("#{} {}".format(test_case + 1, temp if temp * (temp + 1) == 2 * N else - 1))
