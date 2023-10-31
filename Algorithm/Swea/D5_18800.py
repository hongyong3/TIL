import sys
sys.stdin = open("D5_18800_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    chk = [0, 0, 0] # r, b, g
    tot = [0, 0, 0]

    for _ in range(N):
        arr = list(map(int, input().split()))
        for i in range(3):
            if arr[i]:
                chk[i] = 1
            tot[i] += arr[i]

    if N < len(chk):    # except
        ans = - 1
    else:
        # 제일 작은 것을 옮기는 게 좋은가?