import sys
sys.stdin = open("D4_1232_input.txt", "r")

def postorder(n):
    if n:
        postorder(tree[n][2])
        postorder(tree[n][3])
        postAns.append(tree[n][1])


for test_case in range(2):
    N = int(input())
    tree = [[0] * 4 for _ in range(N + 1)]
    ans = 0
    for _ in range(N):
        data = list(input().split())
        index = int(data[0])
        tree[index][0] = index
        tree[index][1] = data[1]
        if len(data) == 3:
            tree[index][2] = int(data[2])
        elif len(data) == 4:
            tree[index][2], tree[index][3] = int(data[2]), int(data[3])

    postAns = []
    postorder(1)

    # 어떻게 계산을 해야하지..

    print(postAns)