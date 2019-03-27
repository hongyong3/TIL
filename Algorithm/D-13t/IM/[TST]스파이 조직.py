import sys
sys.stdin = open("스파이 조직_input.txt", "r")
N, spy = map(str, input().split())

temp = []
child = []
cnt = 0

for i in range(len(spy)):
    if spy[i] == ">":
        temp.pop()
    elif spy[i] != "<":
        cnt = len(temp)
        k = i
        while spy[k] != '<' and spy[k] != '>':
            k += 1
        if len(child) >= 1 and spy[i:k] not in child[-1][1] and cnt == int(N):
            child.append([cnt, spy[i:k]])
        elif i == 0:
            child.append([cnt, spy[i]])
    elif spy[i] == "<":
        temp.append(spy[i])


for i in range(len(child)):
    if child[i][0] == int(N):
        print(int(child[i][1]), end=' ')