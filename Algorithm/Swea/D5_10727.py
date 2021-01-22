import sys
sys.stdin = open("D5_10727_input.txt", "r")
'''
업데이트 하고 해당셀이, 해당행, 해당열에서 가장 큰값이면 ans += 1
업데이트를 하기 전, 해당행, 열이 값이 작으면 false? 값을 주는 등을 이용해 불필요한 계산을 없애고,
업데이트 후, 해당 셀의 크기를 비교하여 false 값을 만들지를 결정하면???
'''

# # 20 / 29 runtime error
# T = int(input())
# for test_case in range(T):
#     N, M, Q = map(int, input().split())
#     ans = 0
#     data = [list(map(int, input().split())) for _ in range(N)]
#
#     for _ in range(Q):
#         r, c, x = map(int, input().split())
#         data[r - 1][c - 1] = x
#         # 여기에서 가지치기 필요?
#         for i in range(N):
#             chk = True
#             idx = data[i].index(max(data[i]))
#             temp = data[i][idx]
#             for j in range(N):
#                 if temp < data[j][idx]:
#                     chk = False
#                     break
#             if chk:
#                 ans += 1
#     print("#{} {}".format(test_case + 1, ans))

T = int(input())
for test_case in range(1):
    N, M, Q = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    col, row = [0] * N, [0] * M

    for i in range(N):
        col[i] = max(data[i])

    for j in range(M):
        maxRow = 0
        for i in range(N):
            if maxRow < data[i][j]:
                maxRow = data[i][j]
        row[j] = maxRow
    print(col)
    print(row)