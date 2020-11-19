import sys
sys.stdin = open("D3_7510_input.txt", "r")

'''
N = x + (x + 1) + (x + 2) + ... + (x + y) -> (y + 1)개의 항
N = (y + 1) * x + (1 + 2 + ... + y)
N = (y + 1)x + y(y + 1) / 2
(y + 1)x = N - y(y + 1) / 2
x = (2N - y^2 - y) / 2(y + 1)
'''

T = int(input())
for test_case in range(T):
    N = int(input())
    ans = 0

    for y in range(N + 1):
        A = 2 * N - y ** 2 - y  # 분자
        B = 2 * (y + 1) # 분모
        if A <= 0:
            break
        if not A % B:
            ans += 1
    print(ans)