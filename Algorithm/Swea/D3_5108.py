import sys
sys.stdin = open("D3_5108_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M, L = map(int, input().split())
    data = list(map(int, input().split()))
    for _ in range(M):
        idx, val = map(int, input().split())
        data.insert(idx, val)
    print("#{} {}".format(test_case + 1, data[L]))