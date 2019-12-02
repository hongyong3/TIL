import sys
sys.stdin = open("[TST] 테이프 이어 붙이기_input.txt", "r")

def DFS(no, cnt, hap):
    global sol
    if cnt + (N - no) < N / 2: return
    if cnt == N // 2: # N / 2 개를 고른경우만 기이의 차 비교
        temp = abs(hap - (tot - hap))   # 이등분한 테이프의 차이
        if temp < sol: sol = temp
        return

    if no >= N:
        for i in range(N): print(rec[i], end = ' ')
        print(cnt, hap)
        # 현재 no번 테이프를 붙이거나 붙이지 않는 경우의 시도
        return
    rec[cnt] = arr[no]
    DFS(no + 1, cnt + 1, hap + arr[no])
    rec[cnt] = 0
    DFS(no + 1, cnt, hap)

N = int(input())
arr = list(map(int, input().split()))
rec = [0] * N
sol = 500 * 20
tot = sum(arr)
DFS(0, 0, 0) # 0번째 테이프부터 시작, 고른개수 0개, 테이프길이 합
print(sol)