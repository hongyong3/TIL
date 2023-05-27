import sys
sys.stdin = open("D8_1634_input.txt", "r")

xy = 'abcdefghijklmnopqrstuvwxyz'
T = int(input())
for test_case in range(1):
    M, N = map(int, input().split())
    alpha = [[0] * 26 for _ in range(26)]

    for _ in range(M):
        x, y = input().split()
        # alpha[ord(x) - 97][ord(y) - 97] = 1
        for i in range(26):
            if alpha[ord(x) - 97][i] == 0:
                alpha[ord(x) - 97][i] = y
                break

    for i in range(26):
        print(xy[i], alpha[i])



    # for _ in range(M):
    #     x, y = input().split()
    #     if x not in dic:
    #         dic[x] = y
    #     else:
    #         dic[x] += y
    #     if y not in dic:
    #         dic[y] = x
    #     else:
    #         dic[y] += x
    #
    # print("#{}".format(test_case + 1))
    # for _ in range(M):
    #     a, b = input().split()
    #     if len(a) != len(b):
    #         print("no")
    #     # else:
    #     #     for i in range(len(a)):
