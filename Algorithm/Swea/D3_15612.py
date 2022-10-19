import sys
sys.stdin = open("D3_15612_input.txt", "r")

T = int(input())
for test_case in range(T):
    arr = [input() for _ in range(8)]
    arrT = list(zip(*arr))
    ans = "yes"

    for i in range(8):
        cnt = 0
        for j in range(8):
            if arrT[i][j] == 'O':
                cnt += 1
        if cnt > 1:
            ans = "no"
            break
    for i in arr:
        if arr.count('O') > 1:
            ans = "no"
            break
    print("#{} {}".format(test_case + 1, ans))