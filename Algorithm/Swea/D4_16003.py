import sys
sys.stdin = open("D4_16003_input.txt", "r")

'''
<1>
1, 10, 100, ..... 즉 10^0, 10^1, 10^2 , .... 10^n 
<2>
10^n + 1 ~ 10^n + 9
<3>
11
<4>
10^n + 10^(n-1) + 1 ~ 10^n + 10^(n-1) + 9
'''

# T = int(input())
# for test_case in range(T):
#     N, K = map(int, input().split())
#     arr = sorted(list(map(int, input().split())))
#     total = sum(arr)
#     if K < arr[0] or K + total < arr[- 1] * 2:
#         ans = - 1
#     elif K >= total:
#         ans = 0
#     else:
#         ans, idx = 0, 1
#         while idx < N:
#             if K < arr[idx]:
#                 K += arr[idx - 1]
#                 total -= arr[idx - 1]
#                 arr.pop(idx - 1)
#                 N -= 1
#                 ans += 1
#             else:
#                 idx += 1
#         jdx = - 2
#         while K < arr[- 1]:
#             if K >= arr[jdx]:
#                 K += arr[jdx]
#                 total -= arr[jdx]
#                 ans += 1
#                 arr.pop(jdx)
#
#             else:
#                 jdx -= 1
#
#         while K < total:
#             ans += 1
#             K += arr[- 1]
#             total -= arr[- 1]
#             arr.pop(- 1)
#     print("#{} {}".format(test_case + 1, ans))

# 50 // 117 Fail
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     if N <= 1000:
#         arr = [str(i) + '.png' for i in range(1, N + 1)]
#         print("#{}".format(test_case + 1), * sorted(arr)[:min(50, N)])
#     else:
#         ans = 0
#         arr = []
#         l = len(str(N))
#
#         # 1, 10, 100, ...
#         for i in range(l):
#             arr.append(str(10 ** i) + '.png')
#             ans += 1
#
#         for i in range(1, 44):
#             if ans == 50:
#                 break
#             arr.append(str(10 ** (l - 1) + i) + '.png')
#             ans += 1
#
#         print("#{}".format(test_case + 1), * sorted(arr)[:min(50, N)])

# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     if N < 143:
#         arr = [str(i) + '.png' for i in range(1, N + 1)][:min(50, N)]
#     else:
#         ans = l = len(str(N)) - 1
#         arr = [str(10 ** i) + '.png' for i in range(l)] # 1, 10, 100, 10^(n - 1)...
#         num, chk1, chk2 = 0, 0, 0   # 자릿수, 50개 chk, 최댓값 chk
#
#         while ans <= 50:
#             for i in range(10):
#                 x = 10 ** l + num * 10 ** (l - 1) + i
#                 if ans == 50:
#                     chk1 = 1
#                     break
#                 if x > N:
#                     chk2 = 1
#                     break
#                 if str(x) + '.png' not in arr:
#                     arr.append(str(x) + '.png')
#                     ans += 1
#             else:
#                 num += 1
#                 if ans < 50:
#                     for i in range(l):
#                         arr.append(str((10 + num) * 10 ** i) + '.png')
#                         ans += 1
#                         if ans == 50:
#                             break
#                 continue
#             if chk1:
#                 break
#             if chk2:
#                 l -= 1
#
#     print("#{}".format(test_case + 1), * sorted(arr))
#     print(len(arr))

T = int(input())
for test_case in range(T):
    N = int(input())
    l = len(str(N))
    if N < 143:
        arr = sorted([str(i) + '.png' for i in range(1, N + 1)])[:min(50, N)]
    else:
        arr = []
        for i in range(l):
            x = 10 ** i
            arr.append(str(x) + '.png')
        cnt = len(arr)
        if cnt < 50:
            for i in range(x + 1, N + 1):
                arr.append(str(i) + '.png')
                if cnt == 50:
                    break

    print("#{}".format(test_case + 1), *arr)