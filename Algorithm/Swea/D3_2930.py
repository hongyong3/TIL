import sys
sys.stdin = open("D3_2930_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    ans, answer = [], []
    for i in range(N):
        if len(data[i]) == 2:
            ans.append(data[i][1])
        else:
            if len(ans) == 0:
                answer.append(-1)
            else:
                answer.append(ans.pop(ans.index(max(ans))))
    print("#{}".format(test_case + 1), *answer)


# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     data = [list(map(int, input().split())) for _ in range(N)]
#     ans, answer = [], []
#     for i in range(N):
#         if len(data[i]) == 2:
#             ans.append(data[i][1])
#         else:
#             if len(ans) == 0:
#                 answer.append(-1)
#             else:
#                 answer.append(ans.pop(ans.index(max(ans))))
#     print("#{}".format(test_case + 1), *answer)