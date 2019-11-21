import sys
sys.stdin = open("D4_3064_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    calc = [list(map(int, input().split())) for _ in range(M)]
    ans, i = [], 0
    while i < M:
        if calc[i][0] == 1:
            data[calc[i][1] - 1] += calc[i][2]
        else:
            ans.append(sum(data[calc[i][1] - 1: calc[i][2]]))
        i += 1
    print("#{}".format(test_case + 1), *ans)