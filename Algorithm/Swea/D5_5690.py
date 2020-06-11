import sys
sys.stdin = open("D5_5690_input.txt", "r")

def solve():
    global ans
    before, mod, cnt, chk = 0, 0, 0, False
    for i in range(N):
        mod = ((10 * before) + int(num[i])) % M
        if not mod :
            cnt += 1
            if i == N - 1:
                chk = True
        before = mod

    if chk:
        cnt -= 1
        for i in range(cnt):
            ans = (ans * 2) % 1000000007
    else:
        ans = 0

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    num = str(input())
    ans = 1
    solve()
    print("#{} {}".format(test_case + 1, ans))