import sys
sys.stdin = open("D2_1976_input.txt", "r")

T = int(input())

for test_case in range(T):
    H1, M1, H2, M2 = map(int, input().split())
    sum_H, sum_M = 0, 0
    sum_H = H1 + H2
    sum_M = M1 + M2
    if sum_H > 12:
        sum_H = sum_H -12
    if sum_M > 60:
        sum_M = sum_M - 60
        sum_H += 1
    print("#{} {} {}".format(test_case + 1, sum_H, sum_M))