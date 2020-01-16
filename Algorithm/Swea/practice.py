import sys
sys.stdin = open("practice_input.txt", "r")

## 가장 큰 수

# def solution(numbers):
#     answer = ''
#     number = []
#     numbers = list(map(str, numbers))
#     for i in numbers:
#         if len(i) == 4:
#             number.append([i, i * 3])
#         if len(i) == 3:
#             number.append([i, i * 4])
#         if len(i) == 2:
#             number.append([i, i * 6])
#         if len(i) == 1:
#             number.append([i, i * 12])
#     number.sort(key = lambda x:x[1], reverse = True)
#     for i in number:
#         answer += i[0]
#     print(answer)
#     return answer
#
# def solution(numbers):
#     numbers = list(map(str, numbers))
#     answer = ""
#     number = []
#     for i in numbers:
#         number.append((i * 12, i))
#     number = sorted(number, reverse = True)
#     for i in number:
#         answer += i[1]
#     return answer
#
# def solution(numbers):
#     numbers = list(map(str, numbers))
#     answer = ""
#     number = []
#     for i in numbers:
#         number.append((i * 12, i))
#     numbers.sort(key =  lambda x : x * 12, reverse = True)
#     for i in numbers:
#         answer += i
#     return answer
#
# def solution(numbers):
#     numbers = list(map(str, numbers))
#     answer = ""
#     numbers.sort(key =  lambda x : x * 12, reverse = True)
#     for i in numbers:
#         answer += i
#     return answer
#
#
#
#
# numbers1 = [6, 10, 2]
# print(solution(numbers1))
# numbers2 = [3, 30, 34, 5, 9]
# print(solution(numbers2))
# numbers3 = [12, 121]
# print(solution(numbers3))
# numbers4 = [21, 212]
# print(solution(numbers4))

## 주식가격

# def solution(prices):
#     answer = [0] * len(prices)
#     for i in range(len(prices)):
#         j = i + 1
#         while j < len(prices):
#             if prices[i] > prices[j]:
#                 answer[i] = j - i
#                 break
#             if j == len(prices) - 1:
#                 answer[i] = j - i
#             j += 1
#     return answer

###################################################################

# def solution(prices):
#     answer = [0] * len(prices)
#     for i in range(len(prices)):
#         for j in range(i + 1, len(prices)):
#             if prices[i] > prices[j]:
#                 answer[i] = j - i
#                 break
#             if j == len(prices) - 1:
#                 answer[i] = j - i
#     return answer
#
# prices1 = [1, 2, 3, 2, 3]
# print(solution(prices1))
# prices2 = [4, 7, 2, 5, 3]
# print(solution(prices2))
# prices3 = [4, 1, 2, 7, 7]
# print(solution(prices3))

## 완주하지 못한 선수

# def solution(participant, completion):
#     answer = ''
#     for i in completion:
#         if i in participant:
#             participant.remove(i)
#     answer += participant[0]
#     return answer
#
# import collections
#
# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]
#
#
#
# participant1 = ["leo", "kiki", "eden"]
# completion1 = ["eden", "kiki"]
# print(solution(participant1, completion1))
# participant2 = ["marina", "josipa", "nikola", "vinko", "filipa"]
# completion2 = ["josipa", "filipa", "marina", "nikola"]
# print(solution(participant2, completion2))
# participant3 = ["mislav", "stanko", "mislav", "ana"]
# completion3 = ["stanko", "ana", "mislav"]
# print(solution(participant3, completion3))


## 전화번호 목록

# def solution(phone_book):
#     answer = True
#     for i in range(len(phone_book)):
#         for j in range(i + 1, len(phone_book)):
#             if phone_book[i] in phone_book[j]:
#                 answer = False
#                 break
#     return answer

###########################################################################

# def solution(phone_book):
#     answer = True
#     phone_book.sort()
#     for i in range(len(phone_book)):
#         for j in range(i + 1, len(phone_book)):
#             if phone_book[i] in phone_book[j]:
#                 answer = False
#                 break
#     return answer

###########################################################################

# def solution(phone_book):
#     answer = True
#     phone_book.sort()
#     for i in range(len(phone_book) - 1):
#         if phone_book[i] in str(phone_book[i + 1:]):
#             answer = False
#             break
#     return answer
#
# phone_book1 = ["119", "97674223", "1195524421"]
# print(solution(phone_book1))
# phone_book2 = ["123", "456", "789"]
# print(solution(phone_book2))
# phone_book3 = ["12", "123", "1235", "567", "88"]
# print(solution(phone_book3))


## D4_1861 dfs 좀더 공부하기


# dx = [- 1, 1, 0, 0]
# dy = [0, 0, - 1, 1]
#
# def dfs(x, y, n):
#     global count, ans, number
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if not (0 <= nx < N and 0 <= ny < N):
#             continue
#         if data[nx][ny] == data[x][y] + 1:
#             count += 1
#             dfs(nx, ny, n)
#             count -= 1
#
#     if count >= ans:
#         ans = count
#         number = min(number, n)
#
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     data = [list(map(int, input().split())) for _ in range(N)]
#     ans, number = 0, float('inf')
#     for x in range(N):
#         for y in range(N):
#             count = 1
#             dfs(x, y, data[x][y])
#     print("#{} {} {}".format(test_case + 1, number, ans))


# dx = [- 1, 1, 0, 0]
# dy = [0, 0, - 1, 1]

# def solve(x, y, subNumber):
#     global ans, number, count
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if not (0 <= nx < N and 0 <= ny < N):
#             continue
#         if data[nx][ny] == data[x][y] + 1:
#             count += 1
#             solve(nx, ny, subNumber)
#             count -= 1
#
#     if count >= ans:
#         ans = count
#         number = min(number, subNumber)
#
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     data = [list(map(int, input().split())) for _ in range(N)]
#     ans = 0
#     count = 0
#     number = float('inf')
#
#     for i in range(N):
#         for j in range(N):
#             solve(i, j, data[i][j])
#
# dx = [- 1, 1, 0, 0]
# dy = [0, 0, - 1, 1]
#
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     data = [list(map(int, input().split())) for _ in range(N)]
#     result = [0] * (N ** 2)
#     for x in range(N):
#         for y in range(N):
#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#                 if (0 <= nx < N and 0 <= ny < N) and (data[nx][ny] == data[x][y] + 1):
#                     result[data[x][y] - 1] = 1
#
#     for i in range((N ** 2) - 1, - 1, - 1):
#         if result[i]:
#             result[i] = result[i + 1] + 1
#         else:
#             result[i] = 1
#
#     answer = max(result)
#     for i in range((N ** 2) + 1):
#         if result[i] == answer:
#             print("#{} {} {}".format(test_case + 1, i + 1, result[i]))
#             break
#
# BAEKJOON star - 11
#
# import math
# def solve(n):
#     for i in range(len(s)):
#         s.append(s[i] + s[i])
#         s[i] = ("   " * n + s[i] + "   " * n)
#
# s = ['  *   ', ' * *  ', '***** ']
# N = int(input())
# K = int(math.log(N // 3, 2))
# for i in range(K):
#     solve(2 ** i)
# for i in range(N):
#     print(s[i])


# BAEKJOON 타임머신
# from collections import deque
# inf = 987654321
#
# def SPFA(start):
#     d = [inf for _ in range(N)]             # 최소 비용 거리
#     on = [False for _ in range(N)]          # 큐에 넣었는지 아닌지
#     cycle = [0 for _ in range(N)]           # 무한으로 cycle이 도는지 아닌지
#     d[start] = 0
#     on[start] = True
#     q = deque([start])
#     while q:
#         now = q.popleft()
#         on[now] = False
#         for next, val in edge[now]:         # 다음 간선에 대해
#             if d[next] > d[now] + val:      # 큐에 넣었는지 아닌지
#                 d[next] = d[now] + val      # 갱신
#                 if not on[next]:            # 큐에 넣었는지 아닌지
#                     cycle[next] += 1        # cycle check
#                     if cycle[next] >= N:    # Node의 개수만큼 queue에 방문했으면
#                         print(-1)           # 무한 cycle이므로 답을 구할 수 없음
#                         return
#                     on[next] = True
#                     q.append(next)          # queue에 넣기
#     for val in d[1 :]:
#         print(-1) if val == inf else print(val)
#
# T = int(input())
# for test_case in range(T):
#     N, M = map(int, input().split())
#     edge = [[] for _ in range(N)]
#     for _ in range(M):
#         u, v, w = map(int, input().split())
#         edge[u - 1].append((v - 1, w))
#     SPFA(0)

# from collections import deque
# inf = 9876543210
#
# def SPFA(n):
#     d = [inf for _ in range(N)]
#     on = [0 for _ in range(N)]
#     cycle = [0 for _ in range(N)]
#     d[n] = 0
#     on[n] = 1
#     q = deque([n])
#     while q:
#         now = q.popleft()
#         on[now] = 0
#         for next, value in edge[now]:
#             if d[next] > d[now] + value:
#                 d[next] = d[now] + value
#                 if not on[next]:
#                     cycle[next] += 1
#                     if cycle[next] >= N:
#                         print(-1)
#                         return
#                     on[next] = 1
#                     q.append(next)
#     for value in d[1:]:
#         print(-1) if value == inf else print(value)
#
# N, M = map(int, input().split())
# edge = [[] for _ in range(N)]
# for _ in range(M):
#     u, v, w = map(int, input().split())
#     edge[u - 1].append((v - 1, w))
# SPFA(0)

# def memoize(func):
#     tempMemo = dict()
#     def wrapped(n):
#         if n in tempMemo:
#             return tempMemo[n]
#         result = func(n)
#         tempMemo[n] = result
#         return result
#     return wrapped
#
# @memoize
# def fib(n):
#     if n in (1, 2):
#         return 1
#     return fib(n - 1) + fib(n - 2)
# fib = memoize(fib)
# print(fib(64))

# def fib2(n):
#     if n in memo:
#         return memo[n]
#     if n in (1, 2):
#         memo[n] = 1
#         return 1
#     result = fib2(n - 1) + fib2(n - 2)
#     memo[n] = result
#     return result
#
# memo = dict()
# print(fib2(64))

# def paper(n):
#     if n in memo:
#         return memo[n]
#     if n in (0, 1):
#         memo[n] = 1
#         return 1
#     result = 2 ** n - paper(n - 1)
#     memo[n] = result
#     return result
#
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     memo = dict()
#     print("#{} {}".format(test_case + 1, paper(N // 10)))

# people = {"A" : 3, "B" : 2, "C" : 1, "D" : 0}
#
# T = int(input())
# for test_case in range(T):
#     S = input()
#     case = [[] for _ in range(len(S))]
#     answer = 0
#
#     if S[0] == "A":
#         for i in range(1, 16):
#             if i & (1 << 3):
#                 case[0].append([i, 1])
#     else:
#         for i in range(1, 16):
#             if i & (1 << 3) and i & (1 << people[S[0]]):
#                 case[0].append([i, 1])
#
#     for i in range(1, len(S)):
#         temporary = []
#         for j in range(1, 16):
#             if j & (1 << people[S[i]]):
#                 temporary.append([j, 0])
#
#         for x in case[i - 1]:
#             for y in temporary:
#                 if x[0] & y[0]:
#                     y[1] = (x[1] + y[1]) % 1000000007
#         case[i] = temporary[:]
#
#     for i in case[- 1]:
#         answer += i[1]
#         answer %= 1000000007
#
#     print("#{} {}".format(test_case + 1, answer))


# T = int(input())
# for test_case in range(1):
#     M, N = map(int, input().split())
#     ans = [1] * M
#     ans = [N - M + 1] + [1] * (N - M - 2)

# def partition_memo(n, m):
#     global memo
#     if n == m or m == 1:
#         memo[n][m] = 1
#     if not memo[n][m]:
#         memo[n][m]= partition_memo(n - 1, m) + partition_memo(n - 1, m - 1)
#         return memo[n][m]
#
# memo = [[0] * 101 for _ in range(101)]
# partition_memo(5, 3)

def inorder(n):
    if n:
        inorder(tree[n][2])
        formula.append(tree[n][1])
        inorder(tree[n][3])

for test_case in range(11):
    N = int(input())
    tree = [[0] * 4 for _ in range(N + 1)]
    ans = 1

    for _ in range(N):
        data = list(input().split())
        index = int(data[0])
        tree[index][0] = index
        tree[index][1] = data[1]
        if len(data) == 3:
            tree[index][2] = int(data[2])
        elif len(data) == 4:
            tree[index][2], tree[index][3] = int(data[2]), int(data[3])

    formula = []
    inorder(1)
    for i in range(len(formula)):
        if not i % 2 and not 48 <= ord(formula[i]) <= 57:
            ans = 0
            break
        elif i % 2 and formula[i] not in ['-', '+', '*', '/']:
            ans = 0
            break
    print("#{} {}".format(test_case + 1, ans))