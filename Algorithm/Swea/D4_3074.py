import sys
sys.stdin = open("D4_3074_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    data = [int(input()) for _ in range(N)]
    time1, time2, minTime = 0, max(data) * M, max(data) * M
    while time1 <= time2:
        mid, ans = (time1 + time2) // 2, 0
        for i in data:
            ans += mid // i
        if ans < M:
            time1 = mid + 1
        else:
            if minTime > mid:
                minTime = mid
            time2 = mid - 1
    print("#{} {}".format(test_case + 1, minTime))