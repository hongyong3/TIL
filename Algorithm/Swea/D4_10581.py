import sys
sys.stdin = open("D4_10581_input.txt", "r")

# def binary(a, b):
#     cnt = 0
#     while a < b:
#         mid = (b - a) // 2
#         if not mid:
#             mid = 1
#         a += mid
#         b -= mid
#         cnt += 1
#     return cnt
#
# T = int(input())
# for test_case in range(T):
#     L, P, C = map(int, input().split())
#     start = L
#     end = P // C if P / C == P // C else P // C + 1
#     ans = binary(start, end)
#     # while start < end:
#     #     between = (end - start) // 2
#     #     start += between
#     #     end -= between
#     #     ans += 1
#     print(ans)

# T = int(input())
# for test_case in range(T):
#     L, P, C = map(int, input().split())
#     start = L + 1
#     end = P // C if P / C == P // C else P // C + 1
#     ans = 0
#
#     while start < end:
#         mid = (end - start) // 2
#         start = mid - mid // 2
#         end = mid + mid // 2
#         ans += 1
#     print(ans)

def binary(a, b):
    cnt = 0
    while a < b:
        mid = (b - a) // 2
        if not mid:
            mid = 1
        a += mid
        b -= mid
        cnt += 1
    return cnt

T = int(input())
for test_case in range(T):
    L, P, C = map(int, input().split())
    start1, start2 = L, L + 1
    end1, end2 = P // C, P // C + 1
    ans = binary(start1, end1)
    ans += binary(start2, end2)
    print("#{} {}".format(test_case + 1, ans))