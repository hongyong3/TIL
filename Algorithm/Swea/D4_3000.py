import sys
sys.stdin = open("D4_3000_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    data = M
    ans = 0
    for _ in range(N):
        x, y = map(int, input().split())
        mid = M
        if (x >= mid and y >= mid):
            data += 1
        elif (x >= mid and y <= mid):
            data -= 1
        elif (x <= mid and y >= mid):
            data -= 1
        elif (x <= mid and y <= mid):
            data -= 1
        ans += (data % 20171109)
    print("#{} {}".format(test_case + 1, ans))