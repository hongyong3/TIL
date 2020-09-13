import sys
sys.stdin = open("D4_5213_input.txt", "r")

def solve():
    for i in range(1, 1000001, 2):
        for j in range(i, 1000001, i):
            mat[j] += i
    arr2[0] = mat[0]
    for i in range(1, 1000001):
        arr2[i] = arr2[i - 1] + mat[i]

T = int(input())
mat, arr2 = [0] * 1000001, [0] * 1000001
solve()
for test_case in range(T):
    L, R = map(int, input().split())
    mat = arr2[R] - arr2[L - 1]
    print("#{} {}".format(test_case + 1, mat))