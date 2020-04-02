import sys
sys.stdin = open("D4_1233_input.txt", "r")

# 이전 풀이
# def inorder(n):
#     if n:
#         inorder(tree[n][2])
#         formula.append(tree[n][1])
#         inorder(tree[n][3])
#
# for test_case in range(10):
#     N = int(input())
#     tree = [[0] * 4 for _ in range(N + 1)]
#
#     for _ in range(N):
#         data = list(input().split())
#         index = int(data[0])
#         tree[index][0] = index
#         tree[index][1] = data[1]
#         if len(data) == 3:
#             tree[index][2] = int(data[2])
#         elif len(data) == 4:
#             tree[index][2], tree[index][3] = int(data[2]), int(data[3])
#
#     ans = 1
#     formula = []
#     inorder(1)
#
#     for i in range(len(formula)):
#         if not i % 2 and not 48 <= ord(formula[i]) <= 57:
#             ans = 0
#             break
#         elif i % 2 and formula[i] not in ['-', '+', '*', '/']:
#             ans = 0
#             break
#     print("#{} {}".format(test_case + 1, ans))

def inorder(n):
    if n:
        inorder(tree[n][2])
        formula.append(tree[n][1])
        inorder(tree[n][3])

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

    formula = []
    inorder(1)
    ans = 1

    for i in range(len(formula)):
        if i % 2 and formula[i] not in '+-*/':
            ans = 0
            break
        elif not i % 2 and not formula[i].isdigit():
            ans = 0
            break
    print("#{} {}".format(test_case + 1, ans))