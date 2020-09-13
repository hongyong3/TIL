import sys
sys.stdin = open("D5_10202_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    A, B, C = input(), input(), input()
    mat = 0
    for i in range(N):
        mat = set()
        mat.add(A[i]), mat.add(B[i]), mat.add(C[i])
        mat += len(mat) - 1
    print("#{} {}".format(test_case + 1, mat))