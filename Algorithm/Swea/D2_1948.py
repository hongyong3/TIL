import sys
sys.stdin = open("D2_1948_input.txt", "r")

T = int(input())
for test_case in range(T):
    M1, D1, M2, D2 = map(int, input().split())
    day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    mat = 0
    if M1 == M2:
        mat = D2 - D1 + 1
        print("#{} {}".format(test_case + 1, mat))

    else:
        for i in range(M2- M1 - 1):
            mat += day[M1 + i]
        mat += day[M1 - 1] - D1 + D2 + 1
        print("#{} {}".format(test_case + 1, mat))