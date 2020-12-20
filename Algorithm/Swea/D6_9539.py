import sys
sys.stdin = open("D6_9539_input.txt", "r")

def solve(week, day, total):
    global ans
    if day > 6:
        if week == N - 1:
            ans = max(ans, total)
        else:
            solve(week + 1, 0, total)
    else:
        solve(week, day + 1, total)
        if week == 0:
            chk[week][day] = 1
            solve(week, day + 2, total + data[week * 7 +day])
            chk[week][day] = 0
        elif not chk[week - 1][day]:
            chk[week][day] = 1
            solve(week, day + 2, total + data[week * 7 + day])
            chk[week][day] = 0


T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    chk = [[0] * 7 for _ in range(N)]
    ans = 0
    solve(0, 0, 0)
    print("#{} {}".format(test_case + 1, ans))