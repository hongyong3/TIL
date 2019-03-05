import sys
sys.stdin = open("서브 트리_input.txt", "r")

def Searchtree(node):
    global count
    if node != 0:
        count += 1
        Searchtree(tree[node][0])
        Searchtree(tree[node][1])
    return count

T = int(input())
for test_case in range(1):
    V, E = map(int, input().split())
    temp = list(map(int, input().split()))
    tree = [[0 for _ in range(3)] for _ in range(V+2)]
    count = 0
    print(temp)
    for i in range(V):
        n1 = temp[i * 2]        # 왼쪽
        n2 = temp[i * 2 + 1]    # 오른쪽
        if not tree[n1][0]:
            tree[n1][0] = n2    # 왼쪽
        else:
            tree[n1][1] = n2    # 오른쪽
        tree[n2][2] = n1        # 부모
    print("#{} {}".format(test_case + 1, Searchtree(E)))
