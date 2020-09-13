import sys
sys.stdin = open("D1_6241_input.txt", "r")

data = list(map(str, input().split('/')))
mat = []
for i in data:
    if i:
        mat.append(i)
print("protocol: {}".format(mat[0][:- 1]))
print("host: {}".format(mat[1]))
print("others: {}".format(mat[2]))