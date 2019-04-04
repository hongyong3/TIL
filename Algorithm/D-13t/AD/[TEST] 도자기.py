import sys
sys.stdin = open("[TEST] 도자기_input.txt", "r")

def DFS(idx, count, start): # 중복조합
    global ans
    if count >= M:
<<<<<<< HEAD
        answer = sorted(check)
        if answer not in ans:
            ans.append(answer[:])
=======
        if check not in ans:
            ans.append(check[:])
>>>>>>> 22c8fcf116150a02774354ae7663c508402b9a89
        return

    if idx >= N:
        return

    for i in range(start, N):
        check[idx] = data[i]
<<<<<<< HEAD
        DFS(idx + 1, count + 1, i + 1)

T = int(input())
for test_case in range(T):
=======
        DFS(idx + 1, count + 1,i + 1)

T = int(input())
for test_case in range(1):
>>>>>>> 22c8fcf116150a02774354ae7663c508402b9a89
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    check = [0] * N
    ans = []
    answer = []

    DFS(0, 0, 0)
<<<<<<< HEAD
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
=======
    print(ans)
    # print(len(ans))

    # [[1, 3, 0, 0, 0], [1, 2, 0, 0, 0], [1, 1, 0, 0, 0], [3, 2, 0, 0, 0], [3, 1, 0, 0, 0], [3, 3, 0, 0, 0], [2, 1, 0, 0, 0], [2, 3, 0, 0, 0]]
>>>>>>> 22c8fcf116150a02774354ae7663c508402b9a89
