import sys
sys.stdin = open("D2_9588_input.txt", "r")

T = int(input())
for test_case in range(T):
    P, V = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(P)]
    ans = []
    for i in range(P):
        for j in range(V):
            if data[i][j]:
                ans.append((i, j))
    print("#{}".format(test_case + 1))
    for i in range(len(ans) // 2):
        print("좌표:({},{}), ({},{}), 길이:{}".format(ans[2 * i][0], ans[2 * i][1], ans[2 * i + 1][0], ans[2 * i + 1][1], ans[2 * i + 1][1] - ans[2 * i][1] + 1))