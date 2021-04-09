import sys
sys.stdin = open("D5_11689_input.txt", "r")

# Runtime Error..?
# arr = []
'''
분모/분자를 한번씩 빼면 연산량이 많이 들어가게 됩니다.

어차피 계속 빼고 빼다보면 분모 or 분자 중 큰 수 = a, 작은 수 = b라고 치면
a <= a/b
b <= b

'''
# T = int(input())
# for test_case in range(T):
#     a, b = map(int, input().split())
#     ans = 0
#
#     if a == 1 or b == 1:
#         ans = max(a, b) - 1
#
#     else:
#         while a != b:
#             if a == 1 or b == 1:
#                 ans += max(a, b) - 1
#                 break
#
#             if a > b:
#                 a -= b
#             else:
#                 b -= a
#             ans += 1
#
#     print("#{} {}".format(test_case + 1, ans))
#     arr.append("#{} {}".format(test_case + 1, ans))
# for i in arr:
#     print(i)

T = int(input())
arr = []
for test_case in range(T):
    a, b = map(int, input().split())
    ans = 0
    if b > a:
        a, b = b, a

    while b > 1:
        cnt, a = divmod(a, b)
        ans += cnt
        a, b = b, a

    else:
        if b == 1:
            ans += a - 1
        else:
            ans -= 1
    arr.append("#{} {}".format(test_case + 1, ans))

for i in arr:
    print(i)