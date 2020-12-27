import sys
sys.stdin = open("D3_2814_input.txt", "r")

# def solve(v, len, visit):
#     global count
#     visit[v] = 1
#     for i in range(N):
#         if i ==  v: continue
#         if visit[i]: continue
#         if not visited[v][i]: continue
#         solve(i, len + 1, visit)
#         visit[i] = 0
#     if len > count:
#         count = len
#
# T = int(input())
# for test_case in range(T):
#     N, M = map(int, input().split())
#     data = [list(map(int, input().split())) for _ in range(M)]
#     count = 0
#
#     visited = [[0] * (N) for _ in range(N)]
#     for i in range(M):
#         visited[data[i][0] - 1][data[i][1] - 1] = 1
#         visited[data[i][1] - 1][data[i][0] - 1] = 1
#     for i in range(N):
#         solve(i, 1, [0] * (N + 1))
#     print("#{} {}".format(test_case + 1, count))


# def solve(v, l, visit):
#     global ans
#     visit[v] = 1
#     for i in range(N):
#         if i == v or visit[i] or not visited[v][i]:
#             continue
#         solve(i, l + 1, visit)
#         visit[i] = 0
#     if ans < l:
#         ans = l
#
#
# T = int(input())
# for test_case in range(T):
#     N, M = map(int, input().split())
#     ans = 0
#     visited = [[0] * N for _ in range(N)]
#     for i in range(M):
#         x, y = map(int, input().split())
#         visited[x - 1][y - 1] = visited[y - 1][x - 1] = 1
#     for i in range(N):
#         solve(i, 1, [0] * N)
#     print("#{} {}".format(test_case + 1, ans))

def bfs(v,h):
    global maxV
    visited= [0] * (N+1)
    q.append((v,h))
    while q:
        n , depth = q.pop(0)
        visited[n] = 1
        if maxV < depth:
            maxV = depth
        for k in line[n]:
            if not visited[k]:
                q.append((k,depth+1))

for tc in range(1,int(input())+1):
    N,M = map(int, input().split())
    line = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int,input().split())
        line[a].append(b)
        line[b].append(a)
    q = []
    maxV = 0
    for i in range(1, N+1):
        bfs(i,1)
    print('#{} {}'.format(tc,maxV))