import sys
sys.stdin = open("[PY-TST]그래프 칠하기_input.txt", "r")

N, M = map(int, input().split())
rec = [0] * N   # 색상기록
data = [list(map(int, input().split())) for _ in range(N)]
flag = 1    # 색칠 가능
color = [1]

for i in range(1, N):
    check = [0] * N
    node = list(range(1, N))
    for j in range(len(data[i])):
        if data[i][j] == 1:
            if color[j] in node:
                node.remove(color[j])
    answer = min(node)
    if answer > M:   # 불가능
        flag = 0
        print(-1)
        break
    color.append(answer)

if flag:
    for i in range(len(color)):
        print(color[i], end = " ")

#########################################################################

# 선생님 풀이
# def check(no, color):
#     # 현재노드와 연결된 노드와 중복색상 여부 체크
#     for i in range(no): # 연결된 노드(열)
#         if arr[no][i] and rec[i] == color:  # 연결된 노드와 같은 색이면 실패
#             return 0
#     return 1
#
# def DFS(no):
#     # 현재 노드에게 1~M 색상을 칠해보는 경우의 수
#     global flag
#
#     if no >= N:
#         flag = 1
#         return
#
#     # 현 노드에게 칠할 수 있으면 기록하고 다음 노드로
#     for i in range(1, M+1):
#         if check(no, i):
#             rec[no] = i
#             DFS(no+1)
#             if flag:
#                 return
#
# # main ----------------------------------------------
# N, M = map(int, input().split())
# rec = [0] * N   # 색상기록
# arr = []
# for i in range(N):
#     arr.append(list(map(int, input().split())))
# flag = 0
# DFS(0)
# if flag:
#     for i in range(N):
#         print(rec[i], end=' ')
# else:
#     print(-1)