import sys
sys.stdin = open("D3_5189_input.txt", "r")

# 이전 풀이
# T = int(input())
# def perm(n, k, sum):
#     global ans
#     if sum > ans:
#         return
#
#     if n == k:
#         sum += data[A[k - 1]][A[k]]
#         if ans > sum:
#             ans = sum
#
#     for i in range(k, n):
#         A[k], A[i] = A[i], A[k]
#         perm(n, k + 1, sum + data[A[k - 1]][A[k]])
#         A[k], A[i] = A[i], A[k]
#
# for test_case in range(T):
#     N = int(input())
#     data = [list(map(int, input().split())) for _ in range(N)]
#     ans = float('inf')
#     A = [_ for _ in range(N)] + [0]
#     perm(N, 1, 0)
#
#     print("#{} {}".format(test_case+1, ans))

def perm(k, total):
    global mat
    if total > ans:
        return

    if k == N:
        total += data[road[k - 1]][road[k]]
        if ans > total:
            ans = total

    for i in range(k, N):
        road[i], road[k] = road[k], road[i]
        perm(k + 1, total + data[road[k - 1]][road[k]])
        road[i], road[k] = road[k], road[i]
    return ans

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    mat = float('inf')
    road = list(range(N)) + [0]
    print("#{} {}".format(test_case + 1, perm(1, 0)))