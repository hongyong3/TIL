import sys
sys.stdin = open("D3_15612_input.txt", "r")

T = int(input())
for test_case in range(T):
    arr = [list(input()) for _ in range(8)]
    arrT = list(zip(*arr))
    ans = "yes"
    for i in range(8):
        cnt, cntT = 0, 0
        for j in range(8):
            if arr[i][j] == 'O':
                cnt += 1
            if arrT[i][j] == 'O':
                cntT += 1
        if cnt > 1 or cntT > 1:
            ans = "no"
            break
    print("#{} {}".format(test_case + 1, ans))