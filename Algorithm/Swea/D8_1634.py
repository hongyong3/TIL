import sys
sys.stdin = open("D8_1634_input.txt", "r")

def dfs(s, e):
    if visited[ord(s) - 97] == 1:
        return 0
    visited[ord(s) - 97] = 1
    for i in alpha[ord(s) - 97]:
        if i == e:
            return 1
        else:
            if dfs(i, e):
                return 1
    return 0


T = int(input())
for test_case in range(T):
    M, N = map(int, input().split())
    alpha = [[] for _ in range(26)]

    for _ in range(M):
        x, y = input().split()
        alpha[ord(x) - 97].append(y)

    print("#{}".format(test_case + 1))
    for _ in range(N):
        a, b = input().split()
        if len(a) != len(b):
            print("no")
            continue
        chk = 1
        for i in range(len(a)):
            visited = [0] * 26
            if a[i] != b[i]:
                if not dfs(a[i], b[i]):
                    chk = 0
                    break
        if chk:
            print("yes")
        else:
            print("no")