import sys
sys.stdin = open("D2_5174_input.txt", "r")

# 이전 풀이
# def Searchtree(node):
#     global count
#     if node != 0:
#         count += 1
#         Searchtree(tree[node][0])
#         Searchtree(tree[node][1])
#     return count
#
# T = int(input())
# for test_case in range(T):
#     V, E = map(int, input().split())
#     temp = list(map(int, input().split()))
#     tree = [[0 for _ in range(3)] for _ in range(V+2)]
#     count = 0
#     for i in range(V):
#         n1 = temp[i * 2]        # 왼쪽
#         n2 = temp[i * 2 + 1]    # 오른쪽
#         if not tree[n1][0]:
#             tree[n1][0] = n2    # 왼쪽
#         else:
#             tree[n1][1] = n2    # 오른쪽
#         tree[n2][2] = n1        # 부모
#     print("#{} {}".format(test_case + 1, Searchtree(E)))

def search(n):
    global count
    if n:
        count += 1
        search(tree[n][1])
        search(tree[n][2])
    return count

T = int(input())
for test_case in range(T):
    E, N = map(int, input().split())
    data = list(map(int, input().split()))
    tree = [[0] * 3 for _ in range(E + 2)]  # 1 <= V <= e + 1   => e + 2
    count = 0

    for i in range(E):
        p = data[i * 2]         # 부모
        c = data[i * 2 + 1]     # 자식
        tree[c][0] = p          # 부모가 누구인가 정의
        if not tree[p][1]:      # 왼쪽부터
            tree[p][1] = c
        else:                   # 오른쪽
            tree[p][2] = c
    print("#{} {}".format(test_case + 1, search(N)))