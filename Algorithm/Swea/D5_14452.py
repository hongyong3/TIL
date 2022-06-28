import sys
sys.stdin = open("D5_14452_input.txt", "r")

'''
1. x == y == 1
    ans += N * M

2. x == y (x, y >= 2) 
    ans += (min(X, Y) - 1) * min(N, M)

3. x가 y의 제곱꼴 or y가 x의 제곱꼴 
    2 : 4(20, 13) 8(13, 8) 16(10, 6) 32(8) 
    3 : 9(20, 13) 27(13, 8)
    4 : 8(13, 8) 16(20, 13) 32(8)
    5 : 25(20, 13)
    6 : 36(20)
    7 : 49(20)
    8 : 16(8, 6) 32(8)
    9 : 27(13, 8)

'''
# print(1846 + 33 + 21 + 16 + 8 + 33 + 21 + 21 + 33 + 8 + 33 + 33 + 33 + 14 + 13 + 21)
T = int(input())
for test_case in range(T):
    X, N, Y, M = map(int, input().split())
    ans = N * M     # 1인 경우
    ans += (min(X, Y) - 1) * min(N, M)
    print(ans)

'''


'''
# print(41 * 26)
# print(30 * 26 + 41 * 26)
