import sys
sys.stdin = open("D3_16603_input.txt", "r")

T = int(input())
for _ in range(T):
    test_case = int(input())
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    rotate = arr[0]
    print(rotate)
    for i in range(1, N):
        rotate.append(arr[i][- 1])
    print(rotate)
    for i in range(M - 2, - 1, - 1):
        rotate.append(arr[- 1][i])
    print(rotate)