import sys
sys.stdin = open("D3_7087_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    chk = [0] * 26
    ans = 0
    for _ in range(N):
        data = input()[0]
        chk[ord(data) - 65] = 1

    for i in chk:
        if i:
            ans += 1
        else:
            break
    print("#{} {}".format(test_case + 1, ans))