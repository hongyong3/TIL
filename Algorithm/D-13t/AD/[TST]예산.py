import sys
sys.stdin = open("[TST]예산_input.txt", "r")

N = int(input())
data = list(map(int, input().split()))
budget = int(input())
answer, start, end = 0, 0, max(data)

while start <= end or answer > budget:
    answer = 0
    mid = (start + end) // 2
    for i in data:
        if i < mid:
            answer += i
        else:
            answer += mid
    if answer <= budget:
        start = mid + 1
    else: end = mid - 1
# print(mid)

# --------------------------------------------------------------------------

# 강사님 풀이1 - binarysearch

# N = int(input())
# Z = list(map(int, input().split()))
# Z.sort()    # 정렬한 예산
# M = int(input())

# N, arr, M

# def check(m):
#     # 상한액으로 지방에서 요청액을 배정 락능하면 배정하고 아니면 상한액으로 합계 계산
#     tot = 0
#     for i in range(N):
#         if Z[i] <= m:
#             tot += Z[i]
#         else: tot += m
#     # 합계가 총액 이하이면 성공 아니면 실패 리턴
#     if tot <= M: return 1
#     else: return 0
#
# e = max(Z)
# s = 1
# sol = 0
# while s <= e:
#     m = (s+e) // 2
#     if check(m):    # 성공하면 상한액을 늘리고
#         sol = m
#         s = m+1
#     else:           # 초과하면 상한액을 줄임
#         e = m-1
# print(sol)

# -------------------------------------------------------------------------

# 강사님 풀이2 - greedy

# N = int(input())
# data = list(map(int, input().split()))
# budget = int(input())
# data.sort()
# sol, tot = 0, 0
# for i in range(N):
#     if tot + data[i]*(N-1) <= budget:   # 혀재 예산액으로 배정 가능하면
#         tot += data[i]
#     else:   # 현재 예산액으로 배정 불가능
#         sol = (budget -  tot) // (N-i)
#         break
# if sol:
#     print(sol)
# else:
#     print(data[N-1])
