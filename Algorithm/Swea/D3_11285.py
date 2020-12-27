import sys
sys.stdin = open("D3_11285_input.txt", "r")

# RunTime Error...
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     ans = 0
#     for _ in range(N):
#         x, y = map(int, input().split())
#         distance = (x * x + y * y) ** 0.5
#         if distance <= 20:
#             ans += 10
#         elif distance <= 40:
#             ans += 9
#         elif distance <= 60:
#             ans += 8
#         elif distance <= 80:
#             ans += 7
#         elif distance <= 100:
#             ans += 6
#         elif distance <= 120:
#             ans += 5
#         elif distance <= 140:
#             ans += 4
#         elif distance <= 160:
#             ans += 3
#         elif distance <= 180:
#             ans += 2
#         elif distance <= 200:
#             ans += 1
#
#         # ans += int(220 - pow(x ** 2 + y ** 2, 0.5)) // 20
#         # ans += int(220 - (x * x + y * y) ** 0.5) // 20
#     print("#{} {}".format(test_case + 1, ans))

T = int(input())
for test_case in range(T):
    N = int(input())
    ans = 0
    for _ in range(N):
        x, y = map(int, input().split())
        d = (x * x + y * y) ** 0.5
        p = 10 - d / 20
        if int(p) == p:
            ans += int(p)
        else:
            ans += int(p) + 1
    print("#{} {}".format(test_case + 1, ans))