import sys
sys.stdin = open("D4_10581_input.txt", "r")

# def binary(a, b):
#     while a < b:
#         mid = (b - a) // 2
#         a += mid // 2
#         b -= mid // 2
#

T = int(input())
for test_case in range(T):
    L, P, C = map(int, input().split())
    start = L + 1
    end = P // C if P / C == P // C else P // C + 1
    ans = 0
    while start < end:
        bitween = (end - start) // 2
        start += bitween
        end -= bitween
        ans += 1
    print(ans)