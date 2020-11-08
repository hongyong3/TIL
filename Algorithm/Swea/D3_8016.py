import sys
sys.stdin = open("D3_8016_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    print("#{} {} {}".format(test_case + 1, 2 * ((N - 1) * (N - 1) + 1) - 1, 2 * N * N - 1))