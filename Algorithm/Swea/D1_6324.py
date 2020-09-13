import sys
sys.stdin = open("D1_6324_input.txt", "r")

def solve(data):
    for i in data:
        if i not in mat:
            mat.append(i)

data = [1, 2, 3, 4, 3, 2, 1]
mat = []
solve(data)
print(data)
print(mat)