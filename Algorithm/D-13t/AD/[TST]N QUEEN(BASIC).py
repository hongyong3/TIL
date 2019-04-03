import sys
sys.stdin = open("[TST]N QUEEN(BASIC)_input.txt", "r")

dr = [-1, -1, -1]
dc = [-1, 0, 1]
def check(r, c):
    # 현재좌표에 퀸을 놓을 수 있는지 여부 체크
    for i in range(3):  # 3방향
        for k in range(1, N):   # 1배, 2배, .... 증감치의 배수 계산
            nr = r + dr[i] * k
            nc = c + dc[i] * k
            if nr < 0 or nr >= N or nc < 0 or nc >= N: break
            if arr[nr][nc] == 1: return 0   # 놓을 수 없음. 실패
    return 1    # 퀸 놓을 수 있음 성공

def DFS(no):    # 현재 행에서 모든 열에 퀸을 놓아보는 경우
    global sol
    if no >= N:
        sol += 1
        return
    for i in range(N):
        if chk1[i]: continue # 세로방향 체크
        if chk2[no + i]: continue # 오른쪽 대각선방향 체크
        if chk3[(N - 1) - (no - i)]: continue # 왼쪽 대각선방향 체크
        chk1[i] = chk2[no + i] = chk3[(N - 1) - (no - i)] = 1
        DFS(no + 1)
        chk1[i] = chk2[no + i] = chk3[(N - 1) - (no - i)] = 0

    # for i in range(N):  # 열
        # if check(no, i):    #  퀸을 놓을 수 있으면
        #     arr[no][i] = 1 # 퀸 놓기
        #     DFS(no + 1)
        #     arr[no][i] = 0  # 퀸 뺴기



N = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]
chk1 = [0] * N
chk2 = [0] * N * 2
chk3 = [0] * N * 2
sol = 0
DFS(0)  # 0행부터 시작
print(sol)

########################################################

# prec = [(행1, 0), (행2, 1) , ...   ] 퀸 위치 저장
# 순열로 행을 저장하니까 행, 열 중복 없음

# def perm(no):
#     global n, flag, cnt
#     if no >= n:
#         cnt += 1
#         return
#     for i in range(n):
#         if a[i]: continue
#
#         if no:
#             flag = True
#             # 대각선 체크
#             # 지금까지 넣은 순열 / 앞으로 넣을 순열 (no, i) 차이 같으면 대각선
#             for j in range(no):
#                 if abs(prec[j][0] - no) == abs(prec[j][1] - i):
#                     flag = False
#
#                 # 대각선 아니면 순열 레코드에 저장
#             if flag:
#                 prec[no] = (no, i)
#                 a[i] = 1
#                 perm(no + 1)
#                 a[i] = 0
#
#             # 레코드 맨 처음값 저장
#         else:
#             prec[no] = (no, i)
#             a[i] = 1
#             perm(no + 1)
#             a[i] = 0
#
#
# # main-------------------------
# n = int(input())
# prec = [0] * n
# cnt = 0
# a = [0] * n
# perm(0)
# print(cnt)