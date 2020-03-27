import sys
sys.stdin = open("D2_5176_input.txt", "r")

# 이전 풀이
# def inorder(node):
#     global val, N
#     if node <= N:
#         inorder(node * 2)
#         table[node] = val
#         val += 1
#         inorder(node * 2 + 1)
#
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     table = [0] * (N+1)
#     val = 1
#     inorder(1)
#     print("#{} {} {} ".format(test_case + 1, table[1], table[N//2]))

def inorder(n):
    global val
    if n <= N:
        inorder(2 * n)
        tree[n] = val
        val += 1
        inorder(2 * n + 1)

T = int(input())
for test_case in range(T):
    N = int(input())
    tree = [0] * (N + 1)
    val = 1
    inorder(1)
    print("#{} {} {}".format(test_case + 1, tree[1], tree[N // 2]))