import sys
sys.stdin = open("D5_3238_input.txt", "r")

# 뤼카의 정리(Lucas's Theorem)
'''
음이 아닌 정수 n, k, 소수 p에 대해서
n과 k를 p진법 전개식으로 나타냈을 때
n = n_(m)_ * p ^ (m) + n_(m - 1)_ * p ^ (m - 1) + ... + n_(1)_ * p ^ (1) + n_(0) * p ^ (0)
k = k_(m)_ * p ^ (m) + k_(m - 1)_ * p ^ (m - 1) + ... + k_(1)_ * p ^ (1) + k_(0) * p ^ (0)

n_(i)_ < m_(i)_ 이면 결과는 0 
예를 들어

'''
mat = [0] * 100000
mat[0] = 1
T = int(input())
for test_case in range(T):
    n, r, p = map(int, input().split())
    for i in range(1, p):
        mat[i] = (mat[i - 1] * i) % p
    mat = 1
    while n or r:
        nn = n % p
        rr = r % p
        if nn < rr:
            mat = 0
            break
        mat = (mat * mat[nn]) % p
        for i in range(p - 2):
            mat = ((mat * mat[rr]) % p * mat[nn - rr]) % p
        n //= p
        r //= p
    print("#{} {}".format(test_case + 1, mat))