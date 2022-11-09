import sys
sys.stdin = open("D4_15761_input.txt", "r")

T = int(input())
for test_case in range(T):
    M, N = map(int, input().split())
    m = '1' * M + '0' * N
    n = '1' + '0' * N + '1' * (M - 1)
    print("#{} {}".format(test_case + 1, bin(int(m, 2) * int(n, 2))[2:].count('1')))

# T=int(input())
# for t in range(T):
#     M,N=map(int, input().split())
#     m='1'*M+'0'*N
#     n='1'+'0'*N+'1'*(M-1)
#     print("#{} {}".format(t+1,bin(int(m,2)*int(n,2))[2:].count('1')) )