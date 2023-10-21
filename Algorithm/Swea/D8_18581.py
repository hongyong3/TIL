import sys
sys.stdin = open("D8_18581_input.txt", "r")

def preorder(n):
    ans.append(n)
    if tree[n][0]:
        preorder(tree[n][0])
    if tree[n][1]:
        preorder(tree[n][1])


def inorder(n):
    if tree[n][0]:
        inorder(tree[n][0])
    ans.append(n)
    if tree[n][1]:
        inorder(tree[n][1])


def postorder(n):
    if tree[n][0]:
        postorder(tree[n][0])
    if tree[n][1]:
        postorder(tree[n][1])
    ans.append(n)

N = int(input())
arr = list(map(int, input().split()))
tree = [[0] * 2 for _ in range(N + 1)]
for i in range(0, (N * 2) - 2 , 2):
    if tree[arr[i]][0] == 0:
        tree[arr[i]][0] = arr[i + 1]
    else:
        tree[arr[i]][1] = arr[i + 1]

ans = []
preorder(1)
print(*ans)
ans = []
inorder(1)
print(*ans)
ans = []
postorder(1)
print(*ans)