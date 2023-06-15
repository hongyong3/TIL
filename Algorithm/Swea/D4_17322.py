import sys
sys.stdin = open("D4_17322_input.txt", "r")

'''
파스칼의 삼각형과 이항계수의 성질
x, y가 가능한 경우 
1. (x + y) // 3 == 0인 경우
만약 x가 y보다 크다면 x == 2y
'''

#Fail 29 // 31
mod = 1000000007
N = 1000001
arr = [1] * N
for i in range(1, N):
    arr[i] = (arr[i - 1] * i) % mod

T = int(input())
for test_case in range(T):
    X, Y = map(int, input().split())
    if X < Y:
        X, Y = Y, X

    if (X + Y) % 3 or X / Y > 2:
        ans = 0
    else:
        n = (X + Y) // 3
        k = Y - n

        A = arr[n]
        B = (arr[k] * arr[n - k]) % mod
        B2 = 1
        expo = mod - 2
        while expo:
            if expo % 2:
                B2 = (B * B2) % mod
            B = (B * B) % mod
            expo //= 2
        ans = (A * B2) % mod
    print("#{} {}".format(test_case + 1, ans))