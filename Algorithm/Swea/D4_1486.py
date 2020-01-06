import sys
sys.stdin = open("D4_1486_input.txt", "r")
# from itertools import combinations
#
# T = int(input())
# for test_case in range(T):
#     N, B = map(int, input().split())
#     data = list(map(int, input().split()))
#     ans = []
#     answer = float('inf')
#     for i in range(2, len(data) + 1):
#         ans.append((list(combinations(data, i))))
#     for i in range(len(ans)):
#         for j in range(len(ans[i])):
#             if sum(ans[i][j]) >= B:
#                 if answer > sum(ans[i][j]):
#                     answer = sum(ans[i][j])
#     print("#{} {}".format(test_case + 1, answer - B))


def combination(count, height):
    global ans
    if count == N:
        if height >= B:
            ans = min(ans, height)
        return
    combination(count + 1, height + data[count])
    combination(count + 1, height)

T = int(input())
for test_case in range(T):
    N, B = map(int, input().split())
    data = list(map(int, input().split()))
    ans = float('inf')
    combination(0, 0)
    print("#{} {}".format(test_case + 1, ans - B))