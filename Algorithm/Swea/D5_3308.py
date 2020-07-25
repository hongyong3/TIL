import sys
sys.stdin = open("D5_3308_input.txt", "r")

# 5 / 10 runtime error
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     data = list(map(int, input().split()))
#     cnt, maxCount = [0] * N, 0
#     for i in range(N):
#         ans = data[i]
#         count = cnt[i]
#         for j in range(i + 1, N):
#             if ans > data[j]: continue
#             if count + 1 <= cnt[j]: continue
#             cnt[j] = count + 1
#             if count + 1 > maxCount:
#                 maxCount = count + 1
#     print("#{} {}".format(test_case + 1, maxCount + 1))

def solve(idx, val):
    low = 0
    high = idx - 1
    while low <= high:
        mid = (low + high) // 2
        if visited[mid] < val:
            low = mid + 1
        elif visited[mid] > val:
            high = mid - 1
        else:
            return mid
    return low

T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    visited = [0] * N
    ans = 1
    visited[0] = data[0]
    for i in range(1, N):
        idx = solve(ans, data[i])
        visited[idx] = data[i]
        if ans <= idx:
            ans += 1
    print("#{} {}".format(test_case + 1, ans))