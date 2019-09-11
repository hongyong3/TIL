import sys
sys.stdin = open("D3_3304_input.txt", "r")

# def subsequence(ans1, ans2, cnt, k):
#     if k == len(data1):
#         return cnt
#     for i in range(len(ans1)):
#         k += 1
#         for j in range(len(ans2)):
#             if ans1[i] != ans2[j]: continue
#             else:
#                 cnt += 1
#                 ans1.pop(i)
#                 ans2.pop(j)
#                 subsequence(ans1, ans2, cnt, k)

T = int(input())
for test_case in range(T):
    data1, data2 = map(str, input().split())
    m, n = len(data1), len(data2)
    ans = [[0] * m + 1 for _ in range(n + 1)]
    for i in range(m):
        for j in range(n):
            if (i == 0 or j == 0): continue
            if data1[i - 1] == data2[j - 1]:
                ans[i][j] = ans[i - 1][j - 1] + 1
                continue
            ans[i][j] = max(ans[i - 1][j], ans[i[j - 1]])
    print()
    # data1, data2 = sorted(data1), sorted(data2)
    # subsequence(data1, data2, 0, 0)
