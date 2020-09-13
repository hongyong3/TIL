import sys
sys.stdin = open("D3_5203_input.txt", "r")

# 이전 풀이
# T = int(input())
# for test_case in range(T):
#     data = list(map(int, input().split()))
#     flag = 0
#     A_ans = [0] * 12
#     B_ans = [0] * 12
#
#     for i in range(len(data)//2):
#         A_ans[data[2 * i]] += 1
#         B_ans[data[2 * i + 1]] += 1
#         if i >= 2:
#             # A
#             if A_ans[data[2 * i]] == 3:
#                 flag = 1
#                 break
#             elif A_ans[data[2 * i]] != 0 and A_ans[data[2 * i] - 1] != 0 and A_ans[data[2 * i] + 1] != 0:
#                 flag = 1
#                 break
#             elif A_ans[data[2 * i]] != 0 and A_ans[data[2 * i] + 1] != 0 and A_ans[data[2 * i] + 2] != 0:
#                 flag = 1
#                 break
#             elif A_ans[data[2 * i]] != 0 and A_ans[data[2 * i] - 1] != 0 and A_ans[data[2 * i] - 2] != 0:
#                 flag = 1
#                 break
#
#             # B
#             if B_ans[data[2 * i + 1]] == 3:
#                 flag = 2
#                 break
#             elif B_ans[data[2 * i + 1]] != 0 and B_ans[data[2 * i + 1] - 1] != 0 and B_ans[data[2 * i + 1] + 1] != 0:
#                 flag = 2
#                 break
#             elif B_ans[data[2 * i + 1]] != 0 and B_ans[data[2 * i + 1] + 1] != 0 and B_ans[data[2 * i + 1] + 2] != 0:
#                 flag = 2
#                 break
#             elif B_ans[data[2 * i + 1]] != 0 and B_ans[data[2 * i + 1] - 1] != 0 and B_ans[data[2 * i + 1] - 2] != 0:
#                 flag = 2
#                 break
#
#     print("#{} {}".format(test_case + 1, flag))

T = int(input())
for test_case in range(T):
    data = list(map(int, input().split()))
    a = [0] * 12
    b = [0] * 12
    mat = 0

    for i in range(6):
        a[data[2 * i]] += 1
        b[data[2 * i + 1]] += 1
        if i >= 2:
            if a[data[2 * i]] == 3 or (a[data[2 * i] - 2] != 0 and a[data[2 * i] - 1] != 0 and a[data[2 * i]] != 0) or (a[data[2 * i] - 1] != 0 and a[data[2 * i]] != 0 and a[data[2 * i] + 1] != 0) or (a[data[2 * i]] != 0 and a[data[2 * i] + 1] != 0 and a[data[2 * i] + 2] != 0):
                mat = 1
                break
            if b[data[2 * i + 1]] == 3 or (b[data[2 * i + 1] - 2] != 0 and b[data[2 * i + 1] - 1] != 0 and b[data[2 * i + 1]] != 0) or (b[data[2 * i + 1] - 1] != 0 and b[data[2 * i + 1]] != 0 and b[data[2 * i + 1] + 1] != 0) or (b[data[2 * i + 1]] != 0 and b[data[2 * i + 1] + 1] != 0 and b[data[2 * i + 1] + 2] != 0):
                mat = 2
                break
    print("#{} {}".format(test_case + 1, mat))