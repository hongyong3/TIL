import sys
sys.stdin = open("최대 상금_input.txt", "r")
T = int(input())

# def myprint(n):
#     for i in range(n):
#         print(" %d" % (a[i]), end =  "")
#     print()
#
# def perm(n, k):
#     if n == k:
#         myprint(n)
#     else:
#         for i in range(k, n):
#             a[i], a[k] = a[k], a[i]
#             perm(n, k + 1)
#             a[i], a[k] = a[k], a[i]
#
# for test_case in range(T):
#     N, M = list(map(int, input().split()))
#     a = str(N)
#
#     perm(3, 0)
#     # print(ans)






    # count = 0
    # for i in range(len(ans)):
    #     if ans[-i] == max(ans) and ans[i] < ans[-i]:
    #         ans[i], ans[-i] = ans[-i], ans[i]
    #         count += 1
            # if count == N:
