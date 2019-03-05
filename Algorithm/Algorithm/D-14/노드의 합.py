import sys
sys.stdin = open("노드의 합_input.txt", "r")
T = int(input())
for test_case in range(T):
    N, M, L = map(int, input().split())
    print(N, M, L)
    V, E = map(int, input().split())
    print(V, E)