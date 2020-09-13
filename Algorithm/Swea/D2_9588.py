import sys
sys.stdin = open("D2_9588_input.txt", "r")

T = int(input())
for test_case in range(T):
    P, V = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(P)]
    mat = []
    for i in range(P):
        for j in range(V):
            if data[i][j]:
                mat.append((i, j))
    print("#{}".format(test_case + 1))
    for i in range(len(mat) // 2):
        print("좌표:({},{}), ({},{}), 길이:{}".format(mat[2 * i][0], mat[2 * i][1], mat[2 * i + 1][0], mat[2 * i + 1][1], mat[2 * i + 1][1] - mat[2 * i][1] + 1))