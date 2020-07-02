import sys
sys.stdin = open("2477_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M, K, A, B = map(int, input().split())
    adata = list(map(int, input().split()))
    bdata = list(map(int, input().split()))
    tdata = list(map(int, input().split()))
    print(adata, bdata, tdata)