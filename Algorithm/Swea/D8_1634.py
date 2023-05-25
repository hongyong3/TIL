import sys
sys.stdin = open("D8_1634_input.txt", "r")

T = int(input())
for test_case in range(T):
    M, N = map(int, input().split())
    # translations = [input().split() for _ in range(M)]
    dic = {}
    for _ in range(M):
        x, y = input().split()
        if x not in dic:
            dic[x] = y
        else:
            dic[x] += y
        if y not in dic:
            dic[y] = x
        else:
            dic[y] += x

    letters = [list(input()) for _ in range(N)]