import sys
sys.stdin = open("D3_9280_input.txt", "r")

def solve(arr):  # 차량, 대기차량 유무
    global ans, chk, wait, order
    for i in arr:
        if i > 0:   # 차량이 들어오면
            for j in range(1, N + 1):
                if not park[j][0]:
                    park[j][0] = W[i]
                    ans += park[j][0] * park[j][1]
                    break
            else:
                wait.append(i)
        else:  # 차량이 나가면
            for j in range(1, N + 1):
                if park[j][0] == W[- i]:
                    park[j][0] = 0
                    break
    order = wait
    wait = []
    chk = 1 if order else 0

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    R = [0] + [int(input()) for _ in range(N)]
    W = [0] + [int(input()) for _ in range(M)]
    order = [int(input()) for _ in range(2 * M)]

    ans, chk, wait = 0, 0, []
    park = [[0, 0] for _ in range(N + 1)]   # park[0] 빈 칸; 주차 여부, 요금

    for i in range(1, N + 1):
        park[i][1] = R[i]
    solve(order)
    while chk:
        chk = 0
        solve(order)
    print(ans)