import sys
sys.stdin = open("practice_input.txt", "r")

# 가장 큰 수
#
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
#
# # 주식가격
#
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
#
# ##################################################################
#
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
#
# # 완주하지 못한 선수
#
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
#
#
# # 전화번호 목록
#
# def solution(phone_book):
#     answer = True
#     for i in range(len(phone_book)):
#         for j in range(i + 1, len(phone_book)):
#             if phone_book[i] in phone_book[j]:
#                 answer = False
#                 break
#     return answer
#
# ##########################################################################
#
# def solution(phone_book):
#     answer = True
#     phone_book.sort()
#     for i in range(len(phone_book)):
#         for j in range(i + 1, len(phone_book)):
#             if phone_book[i] in phone_book[j]:
#                 answer = False
#                 break
#     return answer
#
# ##########################################################################
#
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
#
#
# # D4_1861 dfs 좀더 공부하기
#
#
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
#
#
# dx = [- 1, 1, 0, 0]
# dy = [0, 0, - 1, 1]
#
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
#
#
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
#
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
#
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
#
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
#
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
#
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
#
#
# T = int(input())
# for test_case in range(1):
#     M, N = map(int, input().split())
#     ans = [1] * M
#     ans = [N - M + 1] + [1] * (N - M - 2)
#
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
#
# def inorder(n):
#     if n:
#         inorder(tree[n][2])
#         formula.append(tree[n][1])
#         inorder(tree[n][3])
#
# for test_case in range(11):
#     N = int(input())
#     tree = [[0] * 4 for _ in range(N + 1)]
#     ans = 1
#
#     for _ in range(N):
#         data = list(input().split())
#         index = int(data[0])
#         tree[index][0] = index
#         tree[index][1] = data[1]
#         if len(data) == 3:
#             tree[index][2] = int(data[2])
#         elif len(data) == 4:
#             tree[index][2], tree[index][3] = int(data[2]), int(data[3])
#
#     formula = []
#     inorder(1)
#     for i in range(len(formula)):
#         if not i % 2 and not 48 <= ord(formula[i]) <= 57:
#             ans = 0
#             break
#         elif i % 2 and formula[i] not in ['-', '+', '*', '/']:
#             ans = 0
#             break
#     print("#{} {}".format(test_case + 1, ans))
#
# def solve(num, n):
#     arr, idx, count = [0] * 20, 0, 0
#
#     while num:
#         arr[idx] = num % 10
#         idx += 1
#         num //= 10
#
#     for i in range(idx - 1, - 1, - 1):
#         if i:
#             ans[n] += int(45 * (i) * pow(10, (i) - 1) * arr[i] + ((arr[i] * (arr[i] - 1)) // 2) * pow(10, i) + count * arr[i] * pow(10, i))
#             # ans[n] += int(45 * (i) * pow(10, (i) - 1) * arr[i])
#             # ans[n] += int(((arr[i] * (arr[i] - 1)) // 2) * pow(10, i))
#             # ans[n] += int(count * arr[i] * pow(10, i))
#             count += arr[i]
#
#     ans[n] += count * (arr[0] + 1) + (arr[0] * (arr[0] + 1) // 2)
#
#     if ans[0] == 67500000000000009:
#         ans[0] -= 9
#
#     return ans[n]
#
# T = int(input())
# for test_case in range(T):
#     A, B = map(int, input().split())
#     ans = [0, 0]
#
#     if A:
#         A -= 1
#
#     print("#{} {}".format(test_case + 1, solve(B, 1) - solve(A, 0)))
#
# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)
#
# # print(gcd(33, 100))
#
# def diophantine(a, b, c):
#     r1, r2 = a, b
#     s1, s2 = 1, 0
#     t1, t2 = 0, 1
#
#     while r2 != 0:
#         q = r1 // r2
#         r1, r2 = r2, r1 % r2
#         s1, s2 = s2, s1 - q * s2
#         t1, t2 = t2, t1 - q * t2
#
#     return (c // r1 * s1, c // r1 * t1)
# print(diophantine(21, 14, 35))
#
# def is_divide_pt(x1, y1, x2, y2, x3, y3, x4,y4):
#     f1= (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
#     f2= (x2 - x1) * (y4 - y1) - (y2 - y1) * (x4 - x1)
#     if f1 * f2 < 0 :
#       return True
#     else:
#       return False
#
# def is_cross_pt(x1, y1, x2, y2, x3, y3, x4,y4):
#     b1 = is_divide_pt(x1, y1, x2, y2, x3, y3, x4, y4)
#     b2 = is_divide_pt(x3, y3, x4, y4, x1, y1, x2, y2)
#     if b1 and b2:
#         return True
#     return False
#
# # ans = []
# rectangle = [[0, 0, 8, 0], [0, 0, 4, 0], [0, 4, 8, 4], [8, 0, 8, 4]]
# line = [0, 0, 4, 4]
# # line = [0, 4, 9, 4]
# for i in rectangle:
#     print(is_cross_pt(line[0], line[1], line[2], line[3], i[0], i[1], i[2], i[3]))
# print(ans)
#
# def intersection(x1, y1, x2, y2, x3, y3, x4, y4):
#     px = (x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)
#     py = (x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)
#     p = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
#
#     if not p:
#         # print("parallel")
#         return
#
#     x, y = px / p, py / p
#     if line[0] <= x <= line[2] and line[1] <= y <= line[3] and [x, y] not in ans:
#         ans.append([x, y])
#     return
#
# ans = []
# rectangleLine = []
# meet = 0
#
# rectangle = [0, 0, 8, 4]
# line = [3, 5, 6, 6]
#
# xmin, ymin, xmax, ymax = int(rectangle[0]), int(rectangle[1]), int(rectangle[2]), int(rectangle[3])
# if xmin > xmax:
#     xmin, ymin, xmax, ymax = xmax, ymax, xmin, ymin
# rectangleLine = [[xmin, ymin, xmax, ymin], [xmin, ymin, xmin, ymax], [xmin, ymax, xmax, ymax], [xmax, ymin, xmax, ymax]]
#
#
# x1, y1, x2, y2 = int(line[0]), int(line[1]), int(line[2]), int(line[3])
# if x1 > x2:
#     x1, y1, x2, y2 = x2, y2, x1, y1
#
#
# if y1 == y2:
#     if ymin < y1 < y2 < ymax:
#         if x1 <= xmin < x2 < xmax or xmin < x1 < xmax <= x2:
#             meet = 1
#         elif xmin <= x1 < x2 <= xmax or x1 <= xmin < xmax <= x2:
#             meet = 2
#     elif ymin == y1 or ymax == y1:
#         if xmin == x2 or xmax == x1:
#             meet = 1
#         elif xmin <= x1 <= xmax or xmin <= x2 <= xmax:
#             meet = 4
#
# elif x1 == x2:
#     if xmin < x1 < x2 < xmax:
#         if ymin <= y1 < y2 < ymax or ymin < y1 < y2 <= ymax or y1 < y2 <= ymin < ymax or ymin < ymax <= y1 < y2:
#             meet = 1
#         elif ymin <= y1 < y2 <= ymax or y1 <= ymin < ymax <= y2:
#             meet = 2
#     elif xmin == x1 or xmax == x2:
#         if ymin == y2 or ymax == y1:
#             meet = 1
#         elif ymin <= y1 <= ymax or ymin <= y2 <= ymax:
#             meet = 4
#
# else:
#     for i in rectangleLine:
#         intersection(i[0], i[1], i[2], i[3], line[0], line[1], line[2], line[3])
#     meet = len(ans)
# print(meet)
#
# def dfs(v):
#     visited[v] = 1
#     nv = s[v]
#     if not visited[nv]:
#         p[nv] = v
#         dfs(nv)
#     else:
#         if not final[nv]:
#             cycle(v, s[v])
#     final[v] = 1
#
# def cycle(v, nv):
#     global count
#     count += 1
#     if v == nv:
#         return
#     cycle(p[v], nv)
#
#
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     s = list(map(int, input().split()))
#     s = [0] + s
#     p = [0] * (N + 1)
#     print(s)
#     visited = [0] * (N + 1)
#     final = [0] * (N + 1)
#     count = 0
#     for i in range(N):
#         if not visited[i]:
#             dfs(i)
#     print(count)
# data_set = set(range(0, 11, 2))
# print(data_set)
#
# for item in data_set:
#     print(item, end = " ")
#
# print()
#
# for key, value in enumerate(data_set):
#     print(key, value)
#
# data_set = {1, 2, 3, 4, 5}
#
# data_set1  = {x * y for x in data_set if x % 2 for y in data_set if not y % 2}
# print(data_set1)
#
# data_dict1 = {"홍길동": 20,
#               "이순신": 45,
#               "강감찬": 35}
#
# # 각 항목의 키는 변수 key에 저장되며, data_dict[key]로 해당 키에 대응하는 값을 읽음.
# for key in data_dict1:
#     print("data_dict1 =>", key)
# print()
#
# # 매 반복에서 각 항목의 키가 변수 key에 저장되고, data_dict[key]로 해당 키에 대응하는 값을 읽음.
# for key in data_dict1.keys():
#     print("data_dict.keys() =>", key)
# print()
#
# # 반복될 때 각 항목이 변수 item에 저장되고, item[0] : 키, item[1] : 값을 읽어옴.
# for item in data_dict1.items():
#     print("data_dict.items() =>", item, item[0], item[1])
# print()
#
# # 매 반복에서 각 항목의 키, 값이 변수 key, value에 저장되어 읽어옴.
# for key, value in data_dict1.items():
#     print("data_dict.items() =>", key, value)
# print()
#
# # 매 반복에서 각 항목의 값이 변수 value에 저장되어 읽어옴.
# for value in data_dict1.values():
#     print("data_dict.values() =>", value)
# print()
#
# data_set1 = {item for item in data_dict1.items()}
# print(data_set1)
#
# scores = []
# count = int(input("총 학생의 수를 입력하세요: "))
#
# for i in range(1, count + 1):
#     score = {}
#     score["name"] = input("학생의 이름을 입력하세요: ")
#     score["kor"] = int(input("{} 학생의 국어 점수를 입력하세요: ".format(score["name"])))
#     score["mat"] = int(input("{} 학생의 수학 점수를 입력하세요: ".format(score["name"])))
#     score["eng"] = int(input("{} 학생의 영어 점수를 입력하세요: ".format(score["name"])))
#     scores.append(score)
#
# for score in scores:
#     total = 0
#     for key in score:
#         if key != "name":
#             total += score[key]
#     print("{} => 총점 : {}, 평균 : {0.2F}".format(score["name"], total, total / 3))
#
# for i in range(1, 4):
#     for j in range(1, 4):
#         if i != j:
#             for k in range(1, 4):
#                 if k != i and k != j:
#                     print(i, j, k)
#
# N = int(input())
# textlist = [list(map(str, input().split())) for _ in range(N)]
#
# newdict = {}
# for s in textlist:
#     print()
#     key, value = s.split()
#     # k, v = s[0], s[1]
#     # newdict[k] = v
# print(newdict)
#
# 전치행렬 만들기
# data = [input() for _ in range(8)]
# dataT = [''.join([*i]) for i in zip(*data)]
#
# def dfs(s, order):
#     if not graph[s][order]:
#         return 0
#     else:
#         return 1
#     # if graph[s][order] == 99:
#     #     return 1
#     ans = dfs(graph[s][order], 0)
#     if ans:
#         return ans
#     return dfs(graph[s][order], 1)
#
# graph = [[1, 2], [4, 3], [9, 5], [7, 7], [8, 3], [6, 7], [10, 10], [99, 9], [0, 0], [8, 10], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
# print(dfs(0, 0))
#
# for a in range(1, 5):
#     for b in range(1, 6 - a):
#         if a + b < 6:
#             for c in range(1, 6 - b):
#                 if a + b + c == 6:
#                     print(a, b, c)
#
# a, b, n = map(int, input().split())
# data = list(range(a, b + 1))
# temp = 0
# for i in data[:n]:
#     temp ^= i
# print(temp)
# ans = temp
# i = 0
# while n <= b - a:
#     temp ^= data[i]
#     temp ^= data[n]
#     print(temp)
#     if ans < temp:
#         ans = temp
#     i += 1
#     n += 1
#
# print(ans)
#
# a = 1.5
#
# ans = int(a) if a == int(a) else int(a) + 1
# print(ans)
#
# print(8 & 10)
# print(8 and 10)
# print(7 << 1)
# print(8 | 10)
# print(5 & 7)
#
# data = [[0, 0, 1, 0, 1, 0, 0, 1], [0, 1, 0, 0, 0, 1, 1, 1], [0, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 1], [0, 1, 1, 0, 1, 0, 0, 1], [1, 0, 1, 0, 1, 1, 0, 1]]
#
# for i in data:
#     print(i)
#
# print()
#
# for i in zip(*data):
#     print(i)
#     a = list(i)
#     print(a)
#     print()
#
# print(pow(0.8, 18))
# print(pow(0.9, 18))
#
# copy
# test1 = 1
# print("함수 전")
# print(test1)
# print(id(test1))
# print('==========')
# def returnTwo(num):
#     test1 = 2
#     print("함수 안")
#     print(test1)
#     print(id(test1))
#     print('==========')
# returnTwo(2)
# print("함수 후")
# print(test1)
# print(id(test1))
# print('==========')
#
# test2 = [99, 100, 101]
# print("함수 전")
# print(test2)
# print(id(test2))
# print('==========')
# def returnTwo2(num):
#     print("함수 안")
#     print(test2)
#     print(id(test2))
#     test2[0] = 2
#     print(test2)
#     print(id(test2))
#     print('==========')
# returnTwo2(test2)
# print("함수 후")
# print(test2)
# print(id(test2))
# print('==========')
#
# a = 1
# b = a
# print("변경 전")
# print(id(a))
# print(id(b))
# print(a)
# print(b)
# if id(a) == id(b):
#     print(True)
# else:
#     print(False)
#
# print("변경 후")
# b = 3
# print(id(a))
# print(id(b))
# print(a)
# print(b)
# if id(a) == id(b):
#     print(True)
# else:
#     print(False)

# T = int(input())
# for test_case in range(T):
#     N, L = map(int, input().split())
#     cal_info = [[[0, 0]] for _ in range(N + 1)]
#     # cal_info[0].append([0, 0])
#     for i in range(N):
#         T, K = map(int, input().split())
#         # cal_info[원하는 값]의 길이만큼
#         for j in range(len(cal_info[i])):
#             # 메뉴 추가해도 괜찮으면 넣고 아니면 그냥 넘어가자
#             if K + cal_info[i][j][1] <= L:
#                 cal_info[i + 1].append([cal_info[i][j][0] + T, K + cal_info[i][j][1]])
#
#             cal_info[i + 1].append([cal_info[i][j][0], cal_info[i][j][1]])
#
#     result = 0
#     for info in cal_info[-1]:
#         if info[0] > result:
#             result = info[0]
    # print('#{} {}'.format(test_case + 1, result))
