import sys
sys.stdin = open("[TST]바이러스_input.txt", "r")

def DFS(no):
    # 현재 컴퓨터에서 방문안한 연결된 컴퓨터를 따라가면서 방문표시하고 카운트
    global count
    if visited[no] == 0:
        visited[no] = 1
        count += 1
        for i in range(1, N + 1):
            if data[no][i] == 1:
                DFS(i)


N = int(input())
M = int(input())
data = [[0] * (N + 1) for _ in range(N + 1)]    # 인접행렬
visited = [0] * (N + 1) # 방문표시
for i in range(M):
    s, e = map(int, input().split())
    data[s][e] = data[e][s] = 1 # 연결체크
count = 0
DFS(1)  # 1번 컴퓨터부터 시작
print(count - 1)

###################################################################################

# 선생님 풀이
def FF(n):
    # 현재 컴퓨터에서 방문안한 연결된 컴퓨터를 따라가면서 방문표시하고 카운트
    global sol
    chk[n] = 1
    sol += 1
    for i in range(1, N+1):     # 연결된 컴퓨터(열)
        if arr[n][i] and chk[i] == 0:
            FF(i)

N = int(input())
M = int(input())
chk = [0]*(N+1)     #방문표시
arr = [[0]*(N+1) for _ in range(N+1)]   #인접행렬
for i in range(M):
    s, e = map(int, input().split())
    arr[s][e] = arr[e][s] = 1   # 연결체크

sol = 0
FF(1)   # 1번 컴퓨터부터 시작
print(sol-1)