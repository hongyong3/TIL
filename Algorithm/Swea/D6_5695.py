import sys
sys.stdin = open("D6_5695_input.txt", "r")

'''
cycle
tree    ,,?
visited ,,?
'''
T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    arr = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        arr[i][data[i - 1]] = data[i - 1]

    visited = [0] * (N + 1)