import sys
sys.stdin = open("D5_3503_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = sorted(list(map(int, input().split())))
    mat = 0
    for i in range(N - 2):
        mat = max(mat, data[i + 2] - data[i])
    print("#{} {}".format(test_case + 1, mat))