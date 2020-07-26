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

def solve(n, r, p):
    if arr[n][r] != - 1:
        return arr[n][r]
    if r == 0 or r == n:
        arr[n][r] = 1
        return arr[n][r]
    arr[n][r] = (solve(n - 1, r - 1, p) + solve(n - 1, r, p)) % p
    return arr[n][r]

arr = [0] * 100000
arr[0] = 1
T = int(input())
for test_case in range(1):
    n, r, p = map(int, input().split())
    solve(n, r, p)