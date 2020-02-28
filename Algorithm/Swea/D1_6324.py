import sys
sys.stdin = open("D1_6324_input.txt", "r")

def solve(data):
    for i in data:
        if i not in ans:
            ans.append(i)

data = [1, 2, 3, 4, 3, 2, 1]
ans = []
solve(data)
print(data)
print(ans)