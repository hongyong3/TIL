import sys
sys.stdin = open("D5_1248_input.txt", "r")

def preorder(node):
    global count
    if node:
        count += 1
        preorder(tree[node][0])
        preorder(tree[node][1])
    return count

def parent(n):
    if tree[n][2]:
        L.append(tree[n][2])
        parent(tree[n][2])
    return L

def Search(L1, L2):
    for i in L2:
        if i in L1:
            return i

T = int(input())
for test_case in range(T):
    V, E, N, M = map(int, input().split())
    data = list(map(int, input().split()))
    tree = [[0] * 3 for _ in range(V + 1)]
    count = 0

    for i in range(E):
        n1 = data[i * 2]
        n2 = data[i * 2 + 1]
        if not tree[n1][0]:
            tree[n1][0] = n2
        else:
            tree[n1][1] = n2
        tree[n2][2] = n1

    L = []
    NParent = parent(N)
    L = []
    MParent = parent(M)
    n = Search(NParent, MParent)
    print("#{} {} {}".format(test_case + 1, n, preorder(n)))