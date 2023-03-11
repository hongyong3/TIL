import sys
sys.stdin = open("D2_10760_input.txt", "r")

d = [- 1, 0, 1] * 3
T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for x in range(N):
        for y in range(M):
            cnt = 0
            val = arr[x][y]
            if val == 1:
                continue
            for k in range(9):
                nx = x + d[k // 3]
                ny = y + d[k]
                if 0 <= nx < N and 0 <=ny < M and val > arr[nx][ny]:
                    cnt += 1
                if cnt == 4:
                    ans += 1
                    break
    print("#{} {}".format(test_case + 1, ans))