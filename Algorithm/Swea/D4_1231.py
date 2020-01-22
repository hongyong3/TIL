import sys
sys.stdin = open("D4_1231_input.txt", "r")

def inorder(n):
    if n:
        inorder(tree[n][2])
        inorderAns.append(tree[n][1])
        inorder(tree[n][3])

for test_case in range(10):
    N = int(input())
    tree = [[0] * 4 for _ in range(N + 1)]
    for i in range(N):
        data = input().split()
        index = int(data[0])
        tree[index][0] = index
        tree[index][1] = data[1]
        if len(data) == 3:
            tree[index][2] = int(data[2])
        elif len(data) == 4:
            tree[index][2], tree[index][3] = int(data[2]), int(data[3])
    inorderAns = []
    inorder(1)
    print("#{} {}".format(test_case + 1, ''.join(inorderAns)))