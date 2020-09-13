import sys, time
sys.stdin = open("D3_1215_input.txt", "r")

start = time.time()
# 이전 풀이
# def Xcount(data):
#     global count, X, flag
#     for i in range(X):
#         for j in range(X-N+1):
#             flag = 1
#             for k in range(N//2):
#                 if data[i][j+k] != data[i][j+N-1-k]:
#                     flag = 0
#                     break
#             if flag:
#                 count += 1
#
# def Ycount(data):
#     global count, X, flag
#     for i in range(X):
#         for j in range(X-N+1):
#             flag = 1
#             for k in range(N//2):
#                 if data[j+k][i] != data[j+N-1-k][i]:
#                     flag = 0
#                     break
#             if flag:
#                 count += 1
#
# for test_case in range(10):
#     N = int(input())
#     X= 8
#     stack_a = []
#     stack_b = []
#     data = [input() for _ in range(X)]
#     count = 0
#     flag = 0
#     Xcount(data)
#     Ycount(data)
#     print("#{} {}".format(test_case + 1, count))


for test_case in range(10):
    N = int(input())
    # data = [list(map(str, input())) for _ in range(8)]
    # dataT = [[*i] for i in zip(*data)]
    data = [input() for _ in range(8)]
    dataT = [''.join([*i]) for i in zip(*data)]

    mat = 0
    for i in range(8):
        for j in range(9 - N):
            if data[i][j : j + N] == data[i][j : j + N][:: - 1]:
                mat += 1
            if dataT[i][j: j + N] == dataT[i][j: j + N][::- 1]:
                mat += 1
    print("#{} {}".format(test_case + 1, mat))

print(time.time() - start)