import sys
sys.stdin = open("D5_14452_input.txt", "r")

'''
1. 소수 구하기
2. 소수를 제외한 수,,, ex 6
----------------------------------------------
2.
ex) X, N, Y, M = 31, 41, 59, 26
    1. x == y == 1
        ans += N * M
        ans += 41 * 26 -> 1066
    
    2. x == y (x, y >= 2) 
        ans += (min(X, Y) - 1) * min(N, M)
        ans += min(31, 59) - 1) * min(41, 26) -> 780
    
    3. x가 y의 제곱꼴 or y가 x의 제곱꼴 
        2 : 4(20, 13) 8(13, 8) 16(10, 6) 32(8, 0)   -> 51, 27, 78
        4 : 8(13, 8) 16(20, 13) 32(8, 0)    -> 41, 21, 62
        8 : 16(8, 6) 32(8, 0)   -> 16, 6, 22
        16 : 32(6, 0)   -> 6, 0, 6
        
        3 : 9(20, 13) 27(13, 8) -> 33, 21, 54
        9 : 27(13, 8)   -> 13, 8, 21
        
        5 : 25(20, 13)  -> 20, 13, 33
        
        6 : 36(20, 0)   -> 20
        
        7 : 49(20, 0)   -> 20

'''

# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a
#
# def prime(n, m):
#     global primeArr
#     sieve = [True] * m
#     sieve[0] = sieve[1] = 0
#     for i in range(2, m):
#         if sieve[i]:
#             for j in range(2 * i, m, i):
#                 sieve[j] = False
#
#     for i in range(n, m):
#         if sieve[i]:
#             primeArr.append(i)
#
#
# T = int(input())
# for test_case in range(1):
#     X, N, Y, M = map(int, input().split())
#     primeArr = []
#     prime(2, int(max(X, Y) ** 0.5) + 1)
#     ans = N * M     # x == y == 1
#     ans += (min(X, Y) - 1) * min(N, M)  # x == y (x, y > 1)
#     asd = []
#     for i in primeArr:
#         x = i
#         xsq = 1
#         while x <= X:
#             xx = x * i
#             xxsq = xsq + 1
#             temp = 0
#             while xx <= Y:
#                 g = gcd(xsq, xxsq)
#                 temp += min(N // (xxsq // g), M // (xsq // g))
#                 xx *= i
#                 xxsq += 1
#             asd.append([x, xx // i, temp])
#             x *= i
#             xsq += 1
#             ans += temp
#     # print(ans)
#     print(primeArr)
#     print(asd)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

T = int(input())
for test_case in range(T):
    X, N, Y, M = map(int, input().split())
    ans = N * M  # x == y == 1
    ans += (min(X, Y) - 1) * min(N, M)  # x == y (x, y > 1)
    asd = []
    numChk = []
    tt = 0

    for i in range(2, int(max(X, Y) ** 0.5) + 1):
        if i * i > max(X, Y):
            break
        x = i
        xsq = 1
        if x in numChk:
            continue
        while x <= X:
            y = x * i
            ysq = xsq + 1
            temp1 = 0
            while y <= Y:
                g = gcd(xsq, ysq)
                temp1 += min(N // (ysq // g), M // (xsq // g))
                y *= i
                ysq += 1
            asd.append([x, y // i, temp1])
            if x not in numChk:
                numChk.append(x)
            x *= i
            xsq += 1
            # if X <= x <= Y:
            #     tt += min(M // (ysq // g), N // (xsq // g))
            ans += temp1
    print(ans + temp1)
    print(ans)