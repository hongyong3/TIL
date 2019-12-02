import sys
sys.stdin = open("[TST] 최소의 합(s)_input.txt", "r")

# N = int(input())
# data = [list(map(int, input().split())) for _ in range(N)]
# chk, rec = [0] * N, [0] * N
# sumss = 0

# for i in range(N):
#     sumss += min(data[i])
# print(sumss)

# 중복 가능한 0~2순열 (중복순열)
# def dfs2(no, a, b):
#     global sums
#     if b >= sums:
#         return
#     if no >= N:
#         sums = min(sums, b)
#         return
#     for i in range(N):
#         rec[no] = i
#         dfs2(no + 1, a + 1, b + data[a][i])
#
#
# # 중복 없는 0~2 순열 (순열)
# def dfs(no, a, b):
#     global sums
#     if b >= sums:
#         return
#     if no >= N:
#         sums = min(sums, b)
#         return
#     for i in range(N):
#         if chk[i]:
#             continue
#         chk[i] = 1
#         rec[no] = i
#         dfs(no + 1, a + 1, b + data[a][i])
#         chk[i] = 0
#
#
# sums = float('inf')
# dfs2(0, 0, 0)
# print(sums)
# sums = float('inf')
# dfs(0, 0, 0)
# print(sums)

# ----------------------------------------------------------------------------------------------------------------------

def DFS1(no, nsum): # 현재 행에서 모든 열을 사용하는 경우의 수
    global nmin
    if nsum > nmin:
        return  # 가지치기: 합이 min을 초과시 return 가지치기의 위치는 어디든 상관없다. 하지만 제일 위에 넣는 경우 가장 빠르다.
    if no >= N:
        for i in range(N): print(rec[i], end = " ") # 지워도 됨
        print(nsum) # 지워도 됨
        if nsum < nmin: nmin = nsum
        return
    for i in range(N):  # 열
        rec[no] = arr[no][i] # 고른 값을 기록
        DFS1(no+1, nsum + arr[no][i])

def DFS2(no, nsum): # 현재 행에서 모든 열을 사용하는 경우의 수
    global nmin
    if nsum > nmin:
        return  # 가지치기: 합이 min을 초과시 return 가지치기의 위치는 어디든 상관없다. 하지만 제일 위에 넣는 경우 가장 빠르다.
    if no >= N:
        for i in range(N): print(rec[i], end = " ") # 지워도 됨
        print(nsum) # 지워도 됨
        if nsum < nmin: nmin = nsum
        return
    for i in range(N):  # 열
        if chk[i]:
            continue
        chk[i] = 1
        rec[no] = arr[no][i] # 고른 값을 기록
        DFS2(no+1, nsum + arr[no][i])
        chk[i] = 0

N = int(input())
arr = []
rec = [0] * N   # 고른 값을 기록배열(디버깅용)
chk = [0] * N   # 열 체크배열
for i in range(N):
    arr.append(list(map(int, input().split())))
# 첫번째 방법 : 열의 중복을 허용한 중복순열
nmin = 10**10
DFS1(0, 0)
print(nmin)

# 두번째 방법 : 열의 중복을 허용하지 않는 순열
nmin = 10**10
DFS2(0, 0)
print(nmin)