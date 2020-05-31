import sys
sys.stdin = open("D5_3462_input.txt", "r")

num = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
T = int(input())
for test_case in range(T):
    A, B = map(int, input().split())
    A, B = A / 100, B / 100
    PA, PB = 0, 0

    for i in range(31):
        if i not in num:
            a = pow(1 - A, 30 - i) * pow(A, i)
            b = pow(1 - B, 30 - i) * pow(B, i)
            combi = 1
            for j in range(i):
                combi *= (30 - j) / (1 + j)
            PA += a * combi
            PB += b * combi
    print("#{} {}".format(test_case + 1, "%0.5f" % (1 - PA * PB)))