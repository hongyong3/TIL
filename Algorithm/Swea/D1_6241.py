import sys
sys.stdin = open("D1_6241_input.txt", "r")

data = list(map(str, input().split('/')))
ans = []
for i in data:
    if i:
        ans.append(i)
print("protocol: {}".format(ans[0][:- 1]))
print("host: {}".format(ans[1]))
print("others: {}".format(ans[2]))