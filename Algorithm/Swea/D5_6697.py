import sys
sys.stdin = open("D5_6697_input.txt", "r")

# 방법 1
# dp를 이용하여 모든 등차수열의 값 계산
#
# arr = [0] * 44722
# arr[1] = 1
# for i in range(2, 44722):
#     arr[i] = arr[i - 1] + i
#
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     e = 44722
#     for i in range(e):
#         if N <= arr[i]:
#             e = i
#             break
#     s = arr[e] - N
#     ans = ')' * (e - s) + '(' + ')' * s + '(' * (e - 1)
#     print("#{} {}".format(test_case + 1, ans))


# 방법 2
# dp를 이용하지 않고 값을 직접 계산

# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     D = (- 1 + (1 + 8 * N) ** 0.5) * 0.5
#     if int(D) < D:
#         D = int(D) + 1
#     else:
#         D = int(D)
#     s = D * (D + 1) // 2 - N
#     ans = ')' * (D - s) + '(' + ')' * s + '(' * (D - 1)
#     print("#{} {}".format(test_case + 1, ans))

# 방법 3
# 방법 2와 동일하지만 if문을 한줄로

T = int(input())
for test_case in range(T):
    N = int(input())
    D = (- 1 + (1 + 8 * N) ** 0.5) * 0.5    # 판별식
    D = int(D) + 1 if int(D) < D else int(D)
    s = D * (D + 1) // 2 - N    # sigma
    mat = ')' * (D - s) + '(' + ')' * s + '(' * (D - 1)
    print("#{} {}".format(test_case + 1, mat))