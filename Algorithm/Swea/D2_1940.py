import sys
sys.stdin = open("D2_1940_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    ans, speed = 0, 0
    for i in range(len(data)):
        if len(data[i]) == 2:
            if data[i][0] == 1:
                speed += data[i][1]
                ans += speed
            else:
                if speed == 0:
                    continue
                speed -= data[i][1]
                ans += speed
        else:
            ans += speed
    print("#{} {}".format(test_case + 1, ans))