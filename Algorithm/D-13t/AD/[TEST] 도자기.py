import sys
sys.stdin = open("[TEST] 도자기_input.txt", "r")

def DFS(idx, count, start): # 중복조합
    global ans
    if count >= M:
        answer = sorted(check)
        if answer not in ans:
            ans.append(answer[:])
        return

    if idx >= N:
        return

    for i in range(start, N):
        check[idx] = data[i]
        DFS(idx + 1, count + 1, i + 1)

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    check = [0] * N
    ans = []
    answer = []

    DFS(0, 0, 0)
    print(len(ans))

###############################################################################################
# 선생님 풀이

# def DFS(start, cnt):
#     global sol
#     if cnt == M:
#         # for i in range(cnt): print(rec[i], end = " ")
#         # print()
#         sol += 1
#         return
#     back = 0
#     for i in range(start, N):   # 흙의 재료
#         if back == arr[i]: continue
#         back = arr[i]
#         # if rec[cnt] == arr[i]: continue # 같은재료이면 스킵
#         # rec[cnt] = arr[i]
#         DFS(i + 1, cnt + 1)
#     rec[cnt] = 0
#
#
# T = int(input())
# for test_case in range(T):
#     N, M = map(int, input().split())
#     arr = list(map(int, input().split()))
#     arr.sort()
#     rec = [0] * N
#     sol = 0
#     DFS(0, 0)   # 0번요소부터 시작, 개수는 0개
#     print(sol)