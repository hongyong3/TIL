import sys
sys.stdin = open("D1_6249_input.txt", "r")

a = input()
num = list(range(10))
mat = [0] * 10
for i in range(len(a)):
    mat[int(a[i])] += 1
print(*num)
print(*mat)