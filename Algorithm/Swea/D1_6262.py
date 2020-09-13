import sys
sys.stdin = open("D1_6262_input.txt", "r")

data = str(input())
mat = {}
for i in data:
    mat[i] = data.count(i)
for k, v in mat.items():
    print("{},{}".format(k, v))