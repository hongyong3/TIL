import sys
sys.stdin = open("D3_4831_input.txt", "r")

# T = int(input())
# for test_case in range(T):
#     K, N, M = map(int, input().split())
#     data = list(map(int, input().split()))
#
#     mat = [0] * (N + 1)
#     for i in data:
#         mat[i] = 1
#
#     start, end, count = 0, K, 0
#
#     while True:
#         distance = K
#         for i in range(start + 1, end + 1):
#             if mat[i]:
#                 start = i
#             else:
#                 distance -= 1
#         if distance == 0:
#             count = 0
#             break
#
#         count += 1
#         end = start + K
#         if end >= N:
#             break
#     print("#{} {}".format(test_case + 1, count))

T = int(input())
for test_case in range(T):
    K, N, M = list(map(int, input().split()))
    station = list(map(int, input().split()))

    ans, idx = 0, 0

    while idx < N:
        if idx + K >= N:
            break

        for i in range(idx + K, idx, -1):
            chk = False
            if i in station:
                idx = i
                ans += 1
                chk = True
                break

        if not chk:
            ans = 0
            break
    print("#{} {}".format(test_case + 1, ans))