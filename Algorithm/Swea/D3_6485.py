import sys
sys.stdin = open("D3_6485_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    C = [int(input()) for _ in range(P)]
    ans = [0] * P

    for i in data:
        for j in range(P):
            if i[0] <= C[j] <= i[1]:
                ans[j] += 1
    print("#{}".format(test_case + 1), *ans)