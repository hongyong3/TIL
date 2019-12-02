import sys
sys.stdin = open("스도쿠 검증_input.txt", "r")

# T = int(input())
# for test_case in range(T):
#     flag = 1
#     data = [list(map(int, input().split())) for _ in range(9)]
#
#     for i in range(len(data)):
#         for j in range(len(data)):
#             m = j+1
#             while m <= 8:
#                 if data[i][j] == data[i][m] and data[j][i] == data[m][i]:
#                     print("#{} {}".format(test_case+1, 0))
#                     break
#                 m += 1
#
#     for i in range(0, 9, 3):
#         for j in range(0, 9, 3):
#             for x in range(3):
#                 for y in range(3):
#                     if data[i][j] == data[i+x][j+y]:
#                         print("#{} {}".format(test_case + 1, 0))

T = int(input())
for test_case in range(T):
    flag = 1
    data = [list(map(int, input().split())) for _ in range(9)]

    for i in range(len(data)):
        visit = [0] * 10
        for j in range(len(data)):
            visit[data[i][j]] += 1
            if visit[data[i][j]] > 1:
                flag = 0
                break

    for i in range(len(data)):
        visit = [0] * 10
        for j in range(len(data)):
            visit[data[j][i]] += 1
            if visit[data[j][i]] > 1:
                flag = 0
                break

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            visit = [0] * 10
            for x in range(3):
                for y in range(3):
                    visit[data[i+x][j+y]] += 1
                    if visit[data[j][i]] > 1:
                        flag = 0
                        break

    print("#{} {}".format(test_case + 1, flag))