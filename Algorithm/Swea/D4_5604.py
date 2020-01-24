import sys
sys.stdin = open("D4_5604_input.txt", "r")

# T = int(input())
# for test_case in range(T):
#     A, B = map(int, input().split())
#     data = list(map(str, list(range(A, B + 1))))
#     ans = 0
#     for i in data:
#         for j in range(len(i)):
#             ans += int(i[j])
#     print("#{} {}".format(test_case + 1, ans))

T = int(input())
for test_case in range(3):
    A, B = map(int, input().split())
    ansA, ansB = 0, 0
    arrA, arrB = [0] * 20, [0] * 20
    indexA, indexB = 0, 0
    countA, countB = 0, 0

    while A > 0:
        arrA[indexA] = int(A % 10)
        indexA += 1
        A = A // 10

    while B > 0:
        arrB[indexB] = int(B % 10)
        indexB += 1
        B = B // 10