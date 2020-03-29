import sys
sys.stdin = open("D3_1216_input.txt", "r")

# 이전 풀이
# def palindrome(M, data):
#     ans = []
#     while M > 0:
#         inverse_ans = []
#
#         # 가로
#         for i in range(len(data)):
#             for j in range(len(data)):
#                 if data[i][j:j + M - 1] == data[i][j + M - 1:j:-1]:
#                     ans.append(data[i][j:j + M])
#
#         # 세로
#         for j in range(len(data)):
#             inverse_str = ''
#             for i in range(len(data)):
#                 inverse_str += data[i][j]
#             inverse_ans.append(''.join(inverse_str))
#
#         for i in range(len(data)):
#             for j in range(len(data)):
#                 if inverse_ans[i][j:j + M - 1] == inverse_ans[i][j + M - 1:j:-1]:
#                     ans.append(inverse_ans[i][j:j + M])
#
#         M -= 1
#     answer = []
#     for i in ans:
#         answer.append(len(i))
#     return max(answer)
#
# for test_case in range(10):
#     N = int(input())
#     data = [input() for _ in range(100)]
#     print("#{} {}".format(test_case + 1, palindrome(100, data)))

for test_case in range(1):
    N = int(input())
    data = [input() for _ in range(100)]
    dataT = [[*i] for i in zip(*data)]

    i = 100
    ans = 0
    while i:
        for j in range(100):
            if data[i - 1][j: j + i - 1] == data[i - 1][j + i - 1: j: - 1]:
                if ans < len(data[i - 1][j: j + i - 1]):
                    ans = len(data[i - 1][j: j + i])
            if dataT[i - 1][j: j + i - 1] == dataT[i - 1][j + i - 1: j: - 1]:
                if ans < len(dataT[i - 1][j: j + i - 1]):
                    ans = len(dataT[i - 1][j: j + i])
        i -= 1
    print(ans)