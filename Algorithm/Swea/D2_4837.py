import sys
sys.stdin = open("D2_4837_input.txt", "r")

# 이전 풀이
# T = int(input())
# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# n = len(A)
#
# for test_case in range(1, T+1):
#     N, K = map(int, input().split())
#     count = 0
#     for i in range(1, 1 << n):  # 1<<n : 부분 집합의 갯수
#         sum = 0
#         count_1 = 0
#         for j in range(n + 1):  # # 원소의 수만큼 비트를 비교
#             if i & (1 << j):  # i의 j번째 비트가 1이면 j번째 원소 출력 10진수를 2진수로
#                 sum += A[j]
#                 count_1 += 1
#         if sum == K and count_1 == N:
#             count += 1
#     print("#{} {}".format(test_case, count))

A = list(range(1, 13))
T = int(input())
for test_case in range(T):
    N, K = map(int, input().split())
    count = 0
    for i in range(1, 1 << 12):
        ans, cnt = 0, 0
        for j in range(13):
            if i & (1 << j):
                ans += A[j]
                cnt += 1
        if ans == K and cnt == N:
            count += 1
    print("#{} {}".format(test_case + 1, count))