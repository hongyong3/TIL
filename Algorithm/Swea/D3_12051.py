import sys
sys.stdin = open("D3_12051_input.txt", "r")

# 1493 / 2000
T = int(input())
for test_case in range(T):
    N, pd, pg = map(int, input().split())
    ans = "Possible"
    if (pg == 0 and pd != 0) or (pg == 100 and pd != 100):
        ans = "Broken"
    else:
        chk = True
        while N:
            x = pd * N / 100
            if int(x) == x:
                chk = False
                break
            N -= 1
        if chk:
            ans = "Broken"
    print("#{} {}".format(test_case + 1, ans))