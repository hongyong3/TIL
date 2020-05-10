import sys
sys.stdin = open("D5_9015_input.txt", "r")

# def solution(index, cut, state):
#     global ans, N, data
#     if index + 1 < N:
#         temp_diff = data[index + 1] - data[index]
#         if state:
#             if temp_diff < 0:
#                 solution(index + 1, cut + 1, not state)
#                 solution(index + 1, cut + 1, state)
#             else:
#                 solution(index + 1, cut, state)
#         else:
#             if temp_diff > 0:
#                 solution(index + 1, cut + 1, not state)
#                 solution(index + 1, cut + 1, state)
#             else:
#                 solution(index + 1, cut, state)
#     else:
#         if cut < ans:
#             ans = cut
#
# T = int(input())
# for testCase in range(T):
#     N = int(input())
#     data = list(map(int, input().split()))
#
#     ans = float('inf')
#     initial_state = - 1
#     initial_index = 0
#
#     while initial_index + 1 < N:
#         diff = data[initial_index + 1] - data[initial_index]
#         if diff == 0:
#             initial_index += 1
#         elif diff > 0:
#             initial_state = True
#             break
#         else:
#             initial_state = False
#             break
#
#     if initial_state != -   1:
#         solution(initial_index + 1, 1, initial_state)
#     else:
#         ans = 1
#
#     print("#{} {}".format(testCase + 1, ans))

T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    ans, before, after = 1, 0, 0

    for now in data:
        if not after:
            after = now
            continue

        if not before:
            before = now
            continue

        if before == now:
            continue

        if (before > after and before > now) or (before < after and before < now):
            ans += 1
            before, after = 0, now
        else:
            before, after = now, before
    print("#{} {}".format(test_case + 1, ans))