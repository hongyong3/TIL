import sys
sys.stdin = open("D3_12741_input.txt", "r")

# T = int(input())
# for test_case in range(T):
#     A, B, C, D = map(int, input().split())
#     ans = 0
#     if B <= C:
#         ans = 0
#     elif A <= C and C < B and B <= D:
#         ans = B - C
#     elif A <= C and D <= B:
#         ans = D - C
#
#     elif D <= A:
#         ans = 0
#     elif C <= A and A < D and D <= B:
#         ans = A - D
#     elif C <= A and B <= D:
#         ans = B - A
#     print("#{} {}".format(test_case + 1, ans))

# Runtime Error
# T = int(input())
# ans = []
# for test_case in range(T):
#     A, B, C, D = map(int, input().split())
#     arr = [0] * max(A, B, C, D)
#     for i in range(A, B):
#         arr[i] += 1
#     for j in range(C, D):
#         arr[j] += 1
#     ans.append("#{} {}".format(test_case + 1, arr.count(2)))
# for i in ans:
#     print(i)

# Runtime Error..
# T = int(input())
# ans = []
# for test_case in range(T):
#     A, B, C, D = map(int, input().split())
#     if B <= C:
#         ans.append("#{} {}".format(test_case + 1, 0))
#     elif A <= C and C < B and B <= D:
#         ans.append("#{} {}".format(test_case + 1, B - C))
#     elif A <= C and D <= B:
#         ans.append("#{} {}".format(test_case + 1, D - C))
#     elif D <= A:
#         ans.append("#{} {}".format(test_case + 1, 0))
#     elif C <= A and A < D and D <= B:
#         ans.append("#{} {}".format(test_case + 1, A - D))
#     elif C <= A and B <= D:
#         ans.append("#{} {}".format(test_case + 1, B - A))
# for i in ans:
#     print(i)

T = int(input())
ans = []
for test_case in range(T):
    A, B, C, D = map(int, input().split())
    time = min(B, D) - max(A, C)
    if time < 0:
        time = 0
    ans.append(("#{} {}".format(test_case + 1, time)))
for i in ans:
    print(i)