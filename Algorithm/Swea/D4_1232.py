import sys
sys.stdin = open("D4_1232_input.txt", "r")

def inorder(n):
    if n:
        inorder(tree[n][2])
        formulaAns.append(tree[n][1])
        # if 48 <= ord(tree[n][1]) <= 57:
        #     formulaAns.append(int(tree[n][1]))
        # else:
        #     formulaAns.append(tree[n][1])
        inorder(tree[n][3])

def formula(n):
    for i in range(len(formulaAns)):
        if 48 <= ord(formulaAns[i]) <= 57:
            formulaAns.append(int(formulaAns[i]))
        else:
            formulaAns.append(formulaAns[i])



for test_case in range(10):
    N = int(input())
    tree = [[0] * 4 for _ in range(N + 1)]

    for _ in range(N):
        data = list(input().split())
        index = int(data[0])
        tree[index][0] = index
        tree[index][1] = data[1]
        if len(data) == 3:
            tree[index][2] = int(data[2])
        elif len(data) == 4:
            tree[index][2], tree[index][3] = int(data[2]), int(data[3])
    formulaAns = []
    inorder(1)

    formula(0)