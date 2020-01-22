import sys
sys.stdin = open("D4_1219_input.txt", "r")

for test_case in range(1):
    N, L = map(int, input().split())
    data = list(map(int, input().split()))
    # graph = [[0] * 100 for _ in range(100)]
    graph = {}
    for i in range(L):
        graph[data[2 * i]] = data[2 * i + 1]
    print(graph)