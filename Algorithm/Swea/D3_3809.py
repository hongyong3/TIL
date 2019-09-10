import sys
sys.stdin = open("D3_3809_input.txt", "r")

# 1. runtime error
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     data = []
#     if N < 20:
#         data = list(map(int, input().split()))
#     else:
#         ans = [list(map(int, input().split())) for _ in range(N // 20)]
#         for i in ans:
#             for j in range(len(i)):
#                 data.append(i[j])
#     number10 = []
#     for i in range(10):
#         number10.append(i)
#     for i in range(len(data)):      # 1의 자리
#         if data[i] in number10:
#             number10.remove(data[i])
#     if len(number10) != 0:
#         print("#{} {}".format(test_case + 1, number10[0]))
#         continue
#     number100 = []
#     for i in range(10, 100):
#         number100.append(i)
#     for i in range(len(data) - 1):
#         if (data[i] * 10 + data[i + 1]) in number100:
#             number100.remove(data[i] * 10 + data[i + 1])
#     if len(number100) != 0:
#         print("#{} {}".format(test_case + 1, number100[0]))
#         continue
#     number1000 = []
#     for i in range(100, 1000):
#         number1000.append(i)
#     for i in range(len(data) - 2):
#         if (data[i] * 10 + data[i + 1] + data[i + 2] * 100) in number1000:
#             number1000.remove(data[i] * 10 + data[i + 1] + data[i + 2] * 100)
#     if len(number1000) != 0:
#         print("#{} {}".format(test_case + 1, number1000[0]))
#         continue
T = int(input())
for test_case in range(T):
    N = int(input())
    number, ans, data = "", 0, []
    while len(data) != N:
        data.extend(input().split())
    for i in data:
        number += i
    while str(ans) in number:
        ans += 1
    print("#{} {}".format(test_case + 1, ans))