import sys
sys.stdin = open("D3_3376_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    mat = []
    i, j = 0, 0
    while i < N:
        if i <= 2:
            mat.append(1)
        else:
            mat.append(mat[j] + mat[j + 1])
            j += 1
        i += 1
    print("#{} {}".format(test_case + 1, mat[-1]))