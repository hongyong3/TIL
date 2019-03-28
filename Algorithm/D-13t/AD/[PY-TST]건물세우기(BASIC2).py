import sys
sys.stdin = open("[PY-TST]건물세우기(BASIC2)_input.txt", "r")
def DFS(no, nsum): # 현재 행에서 모든 열을 사용하는 경우의 수
    global nmin
    if nsum > nmin:
        return  # 가지치기: 합이 min을 초과시 return 가지치기의 위치는 어디든 상관없다. 하지만 제일 위에 넣는 경우 가장 빠르다.
    if no >= N:
        if nsum < nmin: nmin = nsum
        return
    for i in range(N):  # 열
        if chk[i]:
            continue
        chk[i] = 1
        rec[no] = arr[no][i] # 고른 값을 기록
        DFS(no+1, nsum + arr[no][i])
        chk[i] = 0

N = int(input())
arr = []
rec = [0] * N   # 고른 값을 기록배열(디버깅용)
chk = [0] * N   # 열 체크배열
for i in range(N):
    arr.append(list(map(int, input().split())))
nmin = 10**10
DFS(0, 0)
print(nmin)