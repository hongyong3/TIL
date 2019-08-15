import sys
sys.stdin = open("D3_6190_input.txt", "r")

def solve(n):
    n, x = n // 10, n % 10
    while n != 0:
        if n % 10 > x:
            return False
        n, x = n // 10, n % 10
    return True


T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    ans = -1
    for i in range(N):
        for j in range(i + 1, N):
            if ans < data[i] * data[j]:
                if solve(data[i] * data[j]):
                    ans = data[i] * data[j]
    print("#{} {}".format(test_case + 1, ans))

# import sys
# sys.stdin = open("D3_6190_input.txt", "r")
#
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     data = list(map(int, input().split()))
#     ans, answer = [], []
#     for i in range(N):
#         j = i + 1
#         while j < N:
#             ans.append(data[i]*data[j])
#             j += 1
#
#     for i in range(len(ans)):
#         j = 1
#         while j < len(str(ans[i])):
#             if ans[i] // 10 ** j >= ans[i] % 10 ** j:
#                 break
#                 print("#{} {}".format(test_case + 1, -1))
#             else:
#                 j += 1
#                 answer.append(ans[i])
#     print("#{} {}".format(test_case + 1, max(answer)))