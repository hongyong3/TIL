import sys
sys.stdin =open("문자열비교_input.txt", "r")
def BruteForce(M, N):
    i = 0
    j = 0
    while j < M and i < N:
        if data_2[i] != data_1[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == M:
        return 1
    else:
        return 0
T = int(input())
for test_case in range(1, T + 1):
    data_1 = input()
    data_2 = input()
    M = len(data_1)
    N = len(data_2)

    print("#{} {}".format(test_case, BruteForce(M, N)))