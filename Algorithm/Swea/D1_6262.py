import sys
sys.stdin = open("D1_6262_input.txt", "r")

data = str(input())
ans = {}
for i in data:
    ans[i] = data.count(i)
for k, v in ans.items():
    print("{},{}".format(k, v))