import sys
sys.stdin = open("어디에 단어가 들어갈 수 있을까_input.txt", "r")
# T = int(input())
# for test_case in range(T):
#     N, K = list(map(int, input().split()))
#     data = [list(map(int, input().split())) for _ in range(N)]
#     count = 0
#
#     for i in range(N+1-K):
#         for j in range(N+1-K):
#             ans = [0] * K
#             s, k = 0, 0
#             while s <= K-1:
#                 s += 1
#                 if data[i][j] == 1:
#                     if data[i][j+s] == 1:
#                     ans[k] = 5
#                     continue
#                 k += 1
#
T = int(input())
for test_case in range(T):
    N, K = list(map(int, input().split()))
    data = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    visit = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if data[i][j] == 0 or visit[i][j] ==1:
                continue
            count = 0
            k = j
            while k < N and data[i][k] == 1:
                visit[i][k] = 1
                count += 1
                k += 1
            if count == K:
                ans += 1

    visit = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if data[j][i] == 0 or visit[j][i] == 1:
                continue
            count = 0
            k = j
            while k < N and data[k][i] == 1:
                visit[k][i] = 1
                count += 1
                k += 1
            if count == K:
                ans += 1

    print("#{} {}".format(test_case+1,ans))