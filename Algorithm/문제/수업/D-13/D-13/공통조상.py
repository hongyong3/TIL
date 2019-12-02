def preorder(node):
    global count
    if node != 0:
        count += 1
        preorder(tree[node][0])
        preorder(tree[node][1])
    return count

def SearchParent(n):
    if tree[n][2] != 0:
        L.append(tree[n][2])
        SearchParent(tree[n][2])
    return L

def Search(L1, L2):
    for i in L2:
        if i in L1:
            return i

import sys
sys.stdin = open("공통조상_input.txt", "r")

T = int(input())
for test_case in range(T):
    V, E, N, M = map(int, input().split())
    temp = list(map(int, input().split()))
    tree = [[0]*3 for _ in range(int(V+1))]
    count = 0

    for i in range(E):
        n1 = temp[i * 2]        # 왼쪽
        n2 = temp[i * 2 + 1]    # 오른쪽
        if not tree[n1][0]:
            tree[n1][0] = n2    # 왼쪽
        else:
            tree[n1][1] = n2    # 오른쪽
        tree[n2][2] = n1        # 부모
    # print(tree)

    L = []
    NP = SearchParent(N)
    L = []
    MP = SearchParent(M)
    n = Search(NP, MP)
    print("#{} {} {}".format(test_case + 1, n, preorder(n)))