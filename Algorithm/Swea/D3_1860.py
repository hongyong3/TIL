import sys
sys.stdin = open("D3_1860_input.txt", "r")

# def solve(data):
#     if min(data) < M: ans = 'Impossible'
#     else:
#         if len(data) <= K: return
#         data = [x - M for x in data[K:]]
#         solve(data)
#     return
#
# T = int(input())
# for test_case in range(T):
#     N, M, K = map(int, input().split())
#     data = sorted(list(map(int, input().split())))
#     ans = 'Possible'
#     if min(data) < M:
#         ans = 'Impossible'
#     solve(data)
#     print("#{} {}".format(test_case + 1, ans))

T = int(input())
for test_case in range(T):
    N, M, K = map(int, input().split())
    data = sorted(list(map(int, input().split())))
    mat = 'Possible'
    if min(data) < M:
        print("#{} {}".format(test_case + 1, mat))
        break
    for i in range(N):
        if (data[i] // M) * K - i <= 0:
            mat = 'Impossible'
            break
    print("#{} {}".format(test_case + 1, mat))