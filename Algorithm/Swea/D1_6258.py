import sys
sys.stdin = open("D1_6258_input.txt", "r")

N = int(input())
mat = {}
for i in range(1, N + 1):
    mat[i] = pow(i, 2)
print(mat)