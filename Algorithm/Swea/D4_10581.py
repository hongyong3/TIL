import sys
sys.stdin = open("D4_10581_input.txt", "r")

'''
l명이 접속이 가능하고 p명이 접속이 불가능한것을 알지만 이것이 접속자의 하한과 상한이 아닙니다.
따라서 x명이 접속이 가능한지 부하를 테스트하는겁니다.
여기서 a명은 접속이 가능하고 ac명은 접속이 불가한걸 확정하기위해 부하테스트를 진행해야하는 최소 횟수를 구하는것이 문제입니다.

예를들어 설명해보겠습니다. L = 100, P = 1000, C = 2라고 해보죠
최소 100명은 접속가능하지만 1000명은 접속이 안되는 것이 주어진 정보입니다.
여기서 c가 2 라는것은 가령, 250명은 접속가능하지만 500명은 접속불가능하구나. 같은 접속가능자와 접속불가능자가 c배 차이나는 두 수를 확정하고 싶은것입니다.
...?
'''

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

# T = int(input())
# for test_case in range(T):
#     L, P, C = map(int, input().split())
#     ans = []
#     K = P // C if P / C == P // C else P // C + 1
#     print(K - L)

T = int(input())
for test_case in range(T):
    L, P, C = map(int, input().split())
    mat = P // C // L
    # print(ans)
    if mat <= 1:
        mat = 0
    elif len(str(mat)) <= 3:
        mat = len(str(mat)) + 1
    else:
        mat = 5
    print("#{} {}".format(test_case + 1, mat))