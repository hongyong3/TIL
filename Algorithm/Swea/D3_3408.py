import sys
sys.stdin = open("D3_3408_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    S1, S2, S3 = 0, 0, 0
    S1 = N * (N + 1) // 2
    S2 += N ** 2
    S3 += N * (N + 1)
    print("#{} {} {} {}".format(test_case + 1, S1, S2, S3))