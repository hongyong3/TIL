import sys
sys.stdin = open("D1_6289_input.txt", "r")

N = str(input())
mat = 0
for i in N:
    mat += int(i)
print(mat)
print(sum(int(i) for i in N))