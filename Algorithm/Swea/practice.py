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

# def decimal():
#     global arr
#     for i in range(2, int(1001 ** 0.5) + 1):
#         if arr[i]:
#             for j in range(i + i, 1001, i):
#                 arr[j] = 0
#     return
#
# arr = [0, 0] + [1] * 999
# decimal()
# print(arr)
# n = [1, 3, 5, 7, 997]
# cnt = 0
# for i in n:
#     if arr[i]:
#         cnt += 1
# print(cnt)

# N = int(input())
# data = list(map(int, input().split()))
# ans = 0
# for i in range(N - 2):
#     for j in range(i + 1, N - 1):
#         for k in range(j + 1, N):
#             if data[j] - data[i] == data[k] - data[j]:
#                 ans += 1
#                 arr.append((i, j, k))
# print(ans)

# 진수변환
# number = 36
# n = 8
#
# answer = ""
#
# while number // n >= 1:
#     remain = number % n
#     number = number // n
#     answer = str(remain) + answer
#     if number < n :
#         answer = str(number) + answer
#
# print("변환 값: %s(%s)" % (answer, n))

# n = int(input())
# s = [list(map(int, input().split())) for _ in range(n)]
# dp = [[0] * n for _ in range(n)]
# print(s)
# print(dp)
# for i in range(1, n):
#     for j in range(n - i):
#         x = i + j
#         dp[j][x] = float('inf')
#         for k in range(j, x):
#             dp[j][x] = min(dp[j][x], dp[j][k] + dp[k + 1][x] + s[j][0] * s[k][1] * s[x][1])

# print(dp[0][n - 1])
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     data = list(map(int, input().split()))
#     dd = {}
#     # for i in range(1, N + 1):
#     #     dd[i] = 0
#     for idx, val in enumerate(data):
#         dd[val] = idx + 1
#         # dd[idx + 1] += val
#     print(dd)

# # 문제 12
# class Employee:
#     name = 'Kim'
#     idNum = 17001
#     salary = 4500000
#     sex = True
# a = Employee()
# print(a.name)
# print(a.idNum)
# print(a.salary)
# print(a.sex)
#
# '''
# Kim
# 17001
# 4500000
# True
# '''
#
# # 문제 27
# hap1 = 10 + 10 % 4 - 10 % 9
# hap2 = 10 * 10 % 4 - 10 % 9 + 5
# print("%d, %d" % (hap1, hap2))
# '''
# 11, 4
# '''
#
# # 문제 30
# a, c = 32, -3
# b = a << 2
# a >>= 3
# c = c << 2  # 음수 shift 연산 공부하기..
# print(a, b, c)
# '''
# 4, 128, -12
# '''
#
# # 문제 34
# i, hap = 0, 0
# while 1:
#     i += 1
#     hap += i
#     if i >= 100:
#         break
# print(hap)
# '''
# 5050
# hap = 100 * 101 // 2
# '''
#
# # 문제 35
# def change():
#     global i, j
#     temp = i
#     i = j
#     j = temp
# i, j = 10, 20
# change()
# print(f"i={i}, j={j}")
# '''
# swap
# i=20, j=10
# '''
#
# # 문제 40
# str = 'Sinagong'
# n = len(str)
# st = list()
# for k in range(n):
#     st.append(str[k])
# for k in range(n-1, -1, -1):
#     print(st[k], end = '')
# '''
# gnoganiS
# '''
#
# # 문제 41
# i, hap = 1, 0
# while i <= 6:
#     hap += i
#     i += 2
# print(f"i={i}, hap={hap}")
# '''
# i=7, hap=9
# '''
#
# # 문제 43
# a = [[1, 1, 0, 1, 0],
#      [1, 0, 1, 0]]
# tot, totsu = 0, 0
# for i in a:
#     for j in i:
#         tot += j
#     totsu = totsu + len(i)
# print(totsu, tot)
# '''
# 9, 5
# '''
#
# # 문제 49
# a, b = 1, 1
# y = a + b
# n = int(input())
# for k in range(3, n + 1):
#     c = a + b
#     y = y + c
#     a = b
#     b = c
# print(y)
# '''
# if n = 8:
#     y = (4, 7, 12, 20, 33, 54) 순
# 54
# '''

# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     mat = 0
#
#     for b in range(2, N + 1):
#         num = N % b
#         x = N
#         chk = 1
#         while x:
#             if x % b != num:
#                 chk = 0
#                 break
#             x //= b
#         if chk:
#             mat = b
#             break
#
#     if not mat:
#         for i in range(1, N + 1):
#             if i * i <= N:
#                 if N % i:
#                     continue
#                 x = i
#                 base = N // x - 1
#                 if base > x:
#                     mat = base
#         mat = N + 1
#     print("#{} {}".format(test_case + 1, mat))

# import itertools
#
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     ans = "NO"
#     data = list(map(int, input().split()))
#     a = list(itertools.combinations(data, 1))

# for _ in range(3):
#     A, B = map(int, input().split())
#     print(abs(A - B))

# 1)
# T = int(input())
# for test_case in range(T):
#     data = sorted(list(map(str, input())))
#     while True:
#         for i in range(len(data) - 1):
#             if data[i] == data[i + 1]:
#                 data.pop(i)
#                 data.pop(i)
#                 break
#         else:
#             break
#
#     if data:
#         print("#{} {}".format(test_case + 1, ''.join(data)))
#     else:
#         print("#{} {}".format(test_case + 1, 'Good'))


# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     data = list(map(int, input().split()))
#     ans = []
#     for i in data:
#         ans.append(abs(i))
#     ans.sort()
#     print("#{} {} {}".format(test_case + 1, ans[0], ans.count(ans[0])))

# Dynamic Programming

# def cutRod(n):
#     for j in range(1, n + 1):
#         q = - 1
#         for i in range(1, j + 1):
#             q = max(q, p[i] + r[j - i])
#         r[j] = q
#     return r[n]
#
# p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
# r = [0] * 11
# cutRod(10)
# print(r[3])

# def zerooneknapsack(item, cap):
#     memo = [[0] * (cap + 1) for _ in range(len(item))]
#     for i in range(len(item)):
#         for j in range(cap + 1):
#             if i == 0 or j == 0:
#                 memo[i][j] = 0
#             elif item[i - 1][2] > j:
#                 memo[i][j] = memo[i - 1][j]
#             else:
#                 memo[i][j] = max(memo[i - 1][j], memo[i - 1][j - item[i - 1][2]] + item[i - 1][1])
#     return memo[len(item)][cap + 1]
#
# item = [[1, 60, 1], [2, 100, 2], [3, 120, 3]]
# zerooneknapsack(item, 5)


# T = int(input())
# for test_case in range(T):
#     D, L, N = map(int, input().split())
#     i,ans = 0, 0
#     for i in range(N):
#         ans += D * (1 + i * L * 0.01) * N
#     print(int(ans))

# T = int(input())
# for test_case in range(T):
#     P = input()
#     Q = input()

# 프로그래머스 문제
# def build(arr):
#     for x, y, a in arr:
#         if a:  # 보
#             if (x, y - 1, 0) not in arr:
#                 if (x + 1, y - 1, 0) not in arr:
#                     if (x - 1, y, 1) not in arr:
#                         if (x + 1, y, 1) not in arr:
#                             return True
#         else:  # 기둥
#             if y:
#                 if (x, y - 1, 0) not in arr:
#                     if (x - 1, y, 1) not in arr:
#                         if (x, y, 1) not in arr:
#                             return True
#     return False
#
#
# def solution(n, build_frame):
#     arr = set()
#     for x, y, a, b in build_frame:
#         val = (x, y, a)
#         if b:  # 설치
#             arr.add(val)
#             if build(arr):
#                 arr.remove(arr)
#         else:  # 삭제
#             if val in arr:  # 만약 있다면 삭제
#                 arr.remove(val)
#                 if build(arr):
#                     arr.add(val)
#
#     ans = map(list, arr)
#     return sorted(ans, key=lambda x: (x[0], x[1], x[2]))

# 프로그래머스 문제 베스트앨범
# def solution(genres, plays):
#     arr = {}  # 각 장르별 재생 횟수
#     for genre, play in zip(genres, plays):
#         if genre not in arr:
#             arr[genre] = play
#         else:
#             arr[genre] += play
#
#     idxDicts = {}
#     for idx, data in enumerate(zip(genres, plays)):
#         genre, play = data[0], data[1]
#         genre_cnt = arr[genre]
#         if genre in idxDicts:
#             idxDicts[genre].append([genre_cnt, play, idx])
#             idxDicts[genre] = sorted(idxDicts[genre], key=lambda x: -x[1])[:2]
#         else:
#             idxDicts[genre] = [[genre_cnt, play, idx]]
#
#     answer = sum(idxDicts.values(), [])
#     answer = sorted(answer, key=lambda x: (-x[0], -x[1], x[2]))
#
#     return [i[2] for i in answer]
#
#
# genres = list(map(str, input().split()))
# plays = list(map(int, input().split()))
# solution(genres, plays)

# 프로그래머스 문제 기능개발
# def solution(progresses, speeds):
#     answer = []
#     idx = 0
#     while progresses:
#         if progresses[0] < 100:
#             cnt = (100 - progresses[0]) // speeds[0]
#         for i in range(len(speeds)):
#             progresses[i] += speeds[i] * cnt
#         answer.append(0)
#         while True and progresses:
#             if progresses[0] >= 100:
#                 answer[idx] += 1
#                 progresses.pop(0)
#                 speeds.pop(0)
#             else:
#                 break
#         idx += 1
#     return answer
#
# T = int(input())
# for test_case in range(T):
#     progresses = list(map(int, input().split()))
#     speeds = list(map(int, input().split()))
#     print(solution(progresses, speeds))

# def solution(progresses, speeds):
#     answer = []
#     for progresse, speed in zip(progresses, speeds):
#         if len(answer) == 0 or answer[- 1][0] < - ((progresse - 100) // speed):
#             answer.append([-((progresse - 100) // speed), 1])
#         else:
#             answer[- 1][1] += 1
#     return [i[1] for i in answer]
#
# T = int(input())
# for test_case in range(T):
#     progresses = list(map(int, input().split()))
#     speeds = list(map(int, input().split()))
#     print(solution(progresses, speeds))

# ????..
# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     return answer
#
# T = int(input())
# for test_case in range(T):
#     bridge_length = int(input())
#     weight = int(input())
#     truck_weight = list(map(int, input().split()))
#     solution(bridge_length, weight, truck_weight)

# 프로그래머스 모의고사
# def solution(answers):
#     answer = []
#     student1, cnt1 = [1, 2, 3, 4, 5], 0
#     student2, cnt2 = [2, 1, 2, 3, 2, 4, 2, 5], 0
#     student3, cnt3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5], 0
#     for i in range(len(answers)):
#         if answers[i] == student1[i % 5]:
#             cnt1 += 1
#         if answers[i] == student2[i % 8]:
#             cnt2 += 1
#         if answers[i] == student3[i % 10]:
#             cnt3 += 1
#     cnt = max(cnt1, cnt2, cnt3)
#     if cnt == cnt1:
#         answer.append(1)
#     if cnt == cnt2:
#         answer.append(2)
#     if cnt == cnt3:
#         answer.append(3)
#     return answer

# 프로그래머스 카펫
# def solution(brown, yellow):
#     x = int((brown + 4 + ((brown + 4) ** 2 - 16 * (brown + yellow)) ** 0.5)) // 4
#     y = (brown + yellow) // x
#     return [max(x, y), min(x, y)]
#
# T = int(input())
# for test_case in range(T):
#     B, Y = map(int, input().split())
#     print(solution(B, Y))

# boj 소수 찾기
# def prime():
#     sieve = [True] * 1001
#     for i in range(2, int(1001 ** 0.5) + 1):
#         if sieve[i]:
#             for j in range(2 * i, 1001, i):
#                 sieve[j] = False
#     return [i for i in range(2, 1001) if sieve[i]]
#
# N = int(input())
# data = list(map(int, input().split()))
# num = prime()
# ans = 0
# for i in data:
#     if i in num:
#         ans += 1
# print(ans)

# A, B = map(int, input().split())
# print(A + B)

# def prime():
#     sieve = [True] * 10001
#     for i in range(2, int(10001 ** 0.5) + 1):
#         if sieve[i]:
#             for j in range(2 * i, 10001, i):
#                 sieve[j] = False
#     return [i for i in range(2, 10001) if sieve[i]]
#
# N, M = int(input()), int(input())
# num = prime()
# ans = float('inf')
# total = 0
# for i in range(N, M + 1):
#     if i in num:
#         total += i
#         if ans > i:
#             ans = i
# if total:
#     print(total)
#     print(ans)
# else:
#     print(- 1)

# N = int(input())
#
# while N > 1:
#     for i in range(2, N + 1):
#         if (N / i) == int(N / i):
#             print(i)
#             N //= i
#             break

# xlist, ylist = [], []
# for i in range(3):
#     x, y = map(int, input().split())
#     xlist.append(x) if x not in xlist else xlist.pop(xlist.index(x))
#     ylist.append(y) if y not in ylist else ylist.pop(ylist.index(y))
# print(xlist[0], ylist[0])

# while True:
#     data = sorted(list(map(int, input().split())))
#     if sum(data) == 0:
#         break
#     else:
#         x, y, z = data
#         if x * x + y * y == z * z:
#             print("right")
#         else:
#             print("wrong")

# x, y, w, h = map(int, input().split())
# print(min(x, y, w - x, h - y))

# def prime():
#     # sieve = [1] * 10001
#     for i in range(2, int(10001 ** 0.5) + 1):
#         if sieve[i]:
#             for j in range(2 * i, 10001, i):
#                 sieve[j] = 0
#     # return [i for i in range(2, 10001) if sieve[i]]
#
#
# sieve = [1] * 10001
# prime()
# for _ in range(int(input())):
#     N = int(input())
#     idx = 0
#
#     while True:
#         if sieve[N // 2 - idx] and sieve[N // 2 + idx]:
#             print(N // 2 - idx, N // 2 + idx)
#             break
#         idx += 1

# n, m = 2, 10
# a = n ** 0.5
# a = int(a) if a == int(a) else int(a) + 1
# b = int(m ** 0.5)
# c = b - a + 1
# print(m - n - b + a)

# T = int(input())
# for test_case in range(T):
#     D, N = map(int, input().split())
#     time = 0
#     for _ in range(N):
#         K, S = map(int, input().split())
#         if time < (D - K) / S:
#             time = (D - K) / S
#     print("#{} {}".format(test_case + 1, D / time))


# import itertools
# T = int(input())
# for test_case in range(T):
#     S = input()
#     arr = sorted(list(set(map(''.join, itertools.permutations(list(S))))))
#     for i in arr:
#         print(i)
    # print(len(arr))
    # print("#{} {}".format(test_case + 1, arr.index(S)))

    # print(S)
    # S = input()
    # a = [0] * 26
    # for i in S:
    #     a[ord(i) - 65] += 1
    # print(a)

# T = int(input())
# for test_case in range(1, T+1):
#     K, N, M = list(map(int, input().split()))
#     station = list(map(int, input().split()))
#     charge = 0
#     position = 0
#
#     while position < N:
#         if position + K >= N:
#             print('#{} {}'.format(test_case, charge))
#             break
#
#         for i in range(position + K, position, - 1):
#             found_station = False
#             if i in station:
#                 position = i
#                 charge += 1
#                 found_station = True
#                 break
#
#         if found_station == False:
#             print('#{} 0'.format(test_case))
#             break

# T = int(input())
# for test_case in range(T):
#     s = input()
#     a, b = 1, 1
#     for i in s:
#         if i == 'L':
#             b += a
#         else:
#             a += b
#     print("#{} {} {}".format(test_case + 1, a, b))

# def calkinWilfSequence(number):
#     def fractions():
#         a = b = 1
#         while True:
#             yield [a, b]
#             a, b = b, 2 * (a - a % b) + b - a
#
#     gen = fractions()
#     res = 0
#     while next(gen) != number:
#         res += 1
#     return res
#
# print(calkinWilfSequence([6, 5]))

# from collections import Counter as Multiset
#
#
# def multiset_combinations(ms, n):
#     assert sum(ms.values()) >= n
#     def f(ms_res, curr_val, ms_rem):
#         nonlocal n
#         if sum(ms_res.values()) == n:  #ideally len would return the number of total elements
#             yield ms_res
#         else:
#             for val in set(ms_rem):
#                 if val >= curr_val:
#                     val_ms = Multiset((val,))  # ideally I wouldn't need to wrap a singleton multiset
#                     # add that value to the result multiset and remove it from remaining multiset
#                     yield from f(ms_res + val_ms, val, ms_rem - val_ms)
#                     # recurse
#     yield from f(Multiset(), sorted(ms.keys())[0], ms)
#
# for m in multiset_combinations(Multiset((3, 3, 4, 4, 4, 5)), 3):
#     print(list(m.elements()))
# for _ in range(int(input())):
#     n, l = map(int, input().split())
#     if n % 2 == 0 and l == 2:
#         l = 3
#     for i in range(l, 101):
#         if i % 2:
#             k = n // i
#             if n % i:
#                 continue
#             c = k - i // 2
#         else:
#             k = n // i
#             if n % i != i // 2:
#                 continue
#             c = k - (i - 1) // 2
#
#         if c >= 0:
#             for j in range(i):
#                 print(c + j, end = ' ')
#             print()
#             break
#     else:
#         print( - 1)

# def dfs(y, x):
#     if not (0 <= y < N and 0 <= x < M) or not arr[y][x]:
#         return
#     arr[y][x] = 0
#     dfs(y + 1, x)
#     dfs(y - 1, x)
#     dfs(y, x + 1)
#     dfs(y, x + 1)
#
# T = int(input())
# for test_case in range(T):
#     M, N, K = map(int, input().split())
#     arr = [[0] * M for _ in range(N)]
#
#     for _ in range(K):
#         x, y = map(int, input().split())
#         arr[y][x] = 1
#
#     ans = 0
#
#     for y in range(N):
#         for x in range(M):
#             if arr[y][x]:
#                 dfs(y, x)
#                 ans += 1
#     print(ans)

# n = int(input())
# a = sorted(list(map(int, input().split())))
# b = sorted(list(map(int, input().split())), reverse = True)
# ans = 0
# for x, y in zip(a, b):
#     ans += x * y
# print(ans)

# for _ in range(int(input())):
#     n = int(input())
#     f = int(input())
#     n -= n % 100
#     ans = 0
#     while True:
#         if not (n + ans) % f:
#             break
#         ans += 1
#     print('0' + str(ans)) if ans < 10 else print(ans)

# color = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
# ohm = str(color.index(input())) + str(color.index(input()))
# ohm = int(ohm) * pow(10, color.index(input()))
# print(ohm)

# ans = 0
# for i in range(8):
#     data = input()
#     if i % 2:
#         for j in range(8):
#             if j % 2:
#                 if data[j] == 'F':
#                     ans += 1
#     else:
#         for j in range(8):
#             if not j % 2:
#                 if data[j] == 'F':
#                     ans += 1
# print(ans)

# a, b = input().split()
#
# ans = 0
# if len(a) == len(b):
#     for i in range(len(a)):
#         if a[i] == b[i]:
#             ans += 1
# print(ans)

# n, k = map(int, input().split())
# coin = list(int(input()) for _ in range(n))
# dp = [0] * (k + 1)
# dp[0] = 1
#
# for i in coin:
#     for j in range(i, k + 1):
#         if j >= i:
#             dp[j] += dp[j - i]
# print(dp[k])

# for _ in range(int(input())):
#     n = int(input())
#     num = sorted(list(int(input()) for _ in range(n)))
#     ans = 0
#     for i in range(n - 2):
#         for j in range(i + 1, n - 1):
#             for k in range(j + 1, n):
#                 if num[i] + num[j] + num[k] in num[k + 1:]:
#                     if num[i] + num[j] + num[k] > ans:
#                         ans = num[i] + num[j] + num[k]
#     print(ans)

# n = int(input())
# word = input()
#
# for _ in range(n - 1):
#     s = ''
#     file = input()
#     for i in range(len(word)):
#         if word[i] == file[i]:
#             s += word[i]
#         else:
#             s += '?'
#     word = s
# print(word)

# x = bin(int(input()))[2:]
# print(x.count('1'))
# stick, ans = 64, 0
# x = int(input())
#
# while x:
#     if stick > x:
#         stick //= 2
#     else:
#         ans += 1
#         x -= stick
# print(bin(int(input()))[2:].count('1'))

# num = 100
# total = 0
# for _ in range(7):
#     n = int(input())
#     if n % 2:
#         total += n
#         if n < num:
#             num = n
# if num == 100:
#     print(- 1)
# else:
#     print(total)
#     print(num)
#
#
# from collections import deque
# dz = [- 1, 1, 0, 0, 0, 0]
# dx = [0, 0, - 1, 1, 0, 0]
# dy = [0, 0, 0, 0, - 1, 1]
#
# def bfs():
#     q = deque()
#     q.append([sz, sx, sy])
#     visited[sz][sx][sy] = 1
#
#     while q:
#         z, x, y = q.popleft()
#         for k in range(6):
#             nz = z + dz[k]
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if not (0 <= nz < l and 0 <= nx < r and 0 <= ny < c):
#                 continue
#             if visited[nz][nx][ny]:
#                 continue
#             if arr[nz][nx][ny] == '.' or arr[nz][nx][ny] == 'E':
#                 dp[nz][nx][ny] = dp[z][x][y] + 1
#                 visited[nz][nx][ny] = 1
#                 q.append([nz, nx, ny])
#
# while True:
#     l, r, c = map(int, input().split()) # 층, 행, 열
#     if not l:
#         break
#     arr = [[[] for _ in range(r)] for _ in range(l)]
#     dp = [[[0] * c for _ in range(r)] for _ in range(l)]
#     visited = [[[0] * c for _ in range(r)] for _ in range(l)]
#     for i in range(l):
#         for j in range(r):
#             arr[i][j] = input()
#         input()
#
#     for z in range(l):
#         for x in range(r):
#             for y in range(c):
#                 if arr[z][x][y] == 'S':
#                     sz, sx, sy = z, x, y
#                 elif arr[z][x][y] == 'E':
#                     ez, ex, ey = z, x, y
#     bfs()
#     if dp[ez][ex][ey]:
#         print("Escaped in {} minute(s).".format(dp[ez][ex][ey]))
#     else:
#         print("Trapped!")

# n, l = map(int, input().split())
# hole = sorted(list(map(int, input().split())))
# ans, r = 0, 0
# for i in hole:
#     if i <= r:
#         continue
#     ans += 1
#     r = i + l - 1
# print(ans)
#
# from itertools import combinations
#
# n, m = map(int, input().split())
# num = [i for i in range(1, n + 1)]
# for i in list(combinations(num, m)):
#     print(*i)
#
# def combi(arr, m):
#     ret = []
#     if m > len(arr):
#         return ret
#     if m == 1:
#         for i in arr:
#             ret.append([i])
#     else:
#         for i in range(len(arr) - m + 1):
#             for j in combi(arr[i + 1:], m - 1):
#                 ret.append([arr[i]] + j)
#     return ret
#
# n, m = map(int, input().split())
# arr = [i for i in range(1, n + 1)]
# for i in combi(arr, m):
#     print(*i)
#
# a = [sum(map(int, x.split('+'))) for x in input().split('-')]
# print(a[0] - sum(a[1:]))
# a = input().split('-')
# n = eval(a[0])
# for i in a[1:]:
#     n -= eval(i)
# print(n)
# def S(N):
#     s = 0
#     while N > 0:
#         s += N % 10
#         N //= 10
#     return s
#
# while True:
#     N = int(input())
#     if not N:
#         break
#     A, p = S(N), 11
#
#     while S(N * p) != A:
#         p += 1
#     print(p)
#
# n = int(input())
# memo = [0, 1, 1]
# i = 3
# while i <= n:
#     memo.append(memo[i - 1] + memo[i - 2])
#     i += 1
# print(memo[n])

# while True:
#     a, b, c = map(int, input().split())
#     if a == b == c == 0:
#         break
#     ans, idx = 'X', 1
#     for i in range(a, c + b, b):
#         if i == c:
#             ans = idx
#             break
#         idx += 1
#     print(ans)

# while True:
#     a, b, c = map(int, input().split())
#     if a == b == c == 0:
#         break
#     x = (c - a) // b
#     y = (c - a) % b
#     print('X' if y or x < 0 else x + 1)

# print("Leading the Way to the Future" if int(input()) else "YONSEI")
# dx = [- 1, 1, 0, 0, - 1, - 1, 1, 1]
# dy = [0, 0, - 1, 1, - 1, 1, - 1, 1]
# def bfs(x, y):
#     q = [(x, y)]
#     while q:
#         x, y = q.pop(0)
#         for k in range(8):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if not (0 <= nx < H and 0 <= ny < W):
#                 continue
#             if not arr[nx][ny]:
#                 continue
#             arr[nx][ny] = 0
#             q.append((nx, ny))
#
# while True:
#     W, H = map(int, input().split())
#     if W == H == 0:
#         break
#     arr = [list(map(int, input().split())) for _ in range(H)]
#     ans = 0
#     for x in range(H):
#         for y in range(W):
#             if arr[x][y]:
#                 bfs(x, y)
#                 ans += 1
#     print(ans)

# n = int(input())
# p = [list(map(int, input().split())) for _ in range(n)]
# p.append(p[0])
#
# ans = 0
# for i in range(n):
#     ans += p[i][0] * p[i + 1][1] - p[i][1] * p[i + 1][0]
# print(ans / 2 if ans > 0 else - ans / 2)


# K = int(input())
# arr = []
# for _ in range(K):
#     n = int(input())
#     arr.append(n) if n else arr.pop()
# print(sum(arr))

# n = int(input())
# memo = [0, 1, 1]
# for i in range(3, 21):
#     memo.append(memo[i - 1] + memo[i - 2])
# print(memo[n])

# N = int(input())
# for i in range(N):
#     K = int(input())
#     print("odd") if K % 2 else print("even")

# from itertools import permutations
# n = int(input())
# arr = permutations(sorted(list(map(int, input().split()))))
# ans = 0
# for a in arr:
#     temp = 0
#     for i in range(n - 1):
#         temp += abs(a[i] - a[i + 1])
#     if ans < temp:
#         ans = temp
# print(ans)

# print(max(map(int, input().split())))

# T = int(input())
# for _ in range(T):
#     n = int(input())
#     memo = [0, 1, 1]
#     for i in range(2, n + 1):
#         memo.append(memo[i - 2] + memo[i - 1] + memo[i])
#     print(memo[- 1])

# n = int(input())
# arr = sorted(list(map(int, input().split())))
# ans = 0
# for i in range(1, n + 1):
#     ans += sum(arr[:i])
# print(ans)

# n = int(input())
# arr = sorted(list(map(int, input().split())) for _ in range(n))
# for i in arr:
#     print(*i)

# arr = ["6 = 1 + 2 + 3", "28 = 1 + 2 + 4 + 7 + 14", "496 = 1 + 2 + 4 + 8 + 16 + 31 + 62 + 124 + 248", "8128 = 1 + 2 + 4 + 8 + 16 + 32 + 64 + 127 + 254 + 508 + 1016 + 2032 + 4064"]
# while True:
#     n = int(input())
#     if n == - 1:
#         break
#     if n == 6:
#         print(arr[0])
#     elif n == 28:
#         print(arr[1])
#     elif n == 496:
#         print(arr[2])
#     elif n == 8128:
#         print(arr[3])
#     else:
#         print("{} is NOT perfect.".format(n))

# from collections import deque
# n = int(input())
# q = deque(range(1, n + 1))
# while len(q) != 1:
#     q.popleft()
#     q.append(q.popleft())
# print(q[0])

# T = int(input())
# for _ in range(T):
#     n = int(input())
#     memo = [1, 1, 1]
#     for i in range(2, n - 1):
#         memo.append(memo[i - 2] + memo[i - 1])
#     print(memo[- 1])

# N = int(input())
# for i in range(1, N + 1):
#     print("Hello World, Judge {}!".format(i))

# def dfs(n):
#     global ans
#     if visited[n]:
#         return
#     visited[n] = True
#     ans += 1
#     for i in range(1, N + 1):
#         if arr[n][i]:
#             dfs(arr[n][i])
#
#
# N = int(input())
# k = int(input())
# arr = [[0] * (N + 1) for _ in range(N + 1)]
#
# visited = [False] * (N + 1)
# ans = 0
# for _ in range(k):
#     n, v = map(int, input().split())
#     arr[n][v] = arr[v][n] = 1
# print(arr)
# dfs(1)
# print(ans)
# print(visited)

# r, b = map(int, input().split())
# p = (r + 4) // 2
# for w in range(1, p + 1):
#     l = p - w
#     if l * w == r + b:
#         break
# print(l, w)

# N, b = input().split()
# ans, idx = 0, 0
# for i in N[:: - 1]:
#     if i.isalpha():
#         ans += (ord(i) - 55) * pow(int(b), idx)
#     else:
#         ans += int(i) * pow(int(b), idx)
#     idx += 1
# print(ans)

# s = input()
# ans = ''
# for i in s:
#     if ord(i) >= 97:
#         ans += i.upper()
#     else:
#         ans += i.lower()
# print(ans)

# N = int(input())
# A = list(map(int, input().split()))
# B, C = map(int, input().split())
# ans = N
# for i in A:
#     if i > B:
#         temp = (i - B) / C
#         if temp == int(temp):
#             ans += int(temp)
#         else:
#             ans += int(temp) + 1
# print(ans)
# from itertools import combinations
# n, m = map(int, input().split())
# arr = sorted(list(map(int, input().split())))
# for i in combinations(arr, m):
#     print(*i)

# def game(batting):
#     score, batter, out = 0, 0, 0
#     for i in range(N):
#         out = 0
#         runner = [0] * 3
#         while out < 3:
#             if data[i][batting[batter]] == 0:
#                 out += 1
#             else:
#                 for j in range(2, - 1, - 1):
#                     if runner[j]:
#                         if j + data[i][batting[batter]] >= 3:
#                             score += 1
#                         else:
#                             runner[j + data[i][batting[batter]]] = 1
#                         runner[j] = 0
#                 if data[i][batting[batter]] == 4:
#                     score += 1
#                 else:
#                     runner[data[i][batting[batter]] - 1] = 1
#             batter = (batter + 1) % 9
#     return score
#
# def backTraking(batting, chk):
#     global ans
#     if len(batting) == 9:
#         if batting[3] == 0:
#             ans = max(ans, game(batting))
#         return
#     for i in range(9):
#         if not chk[i]:
#             batting.append(i)
#             chk[i] = 1
#             backTraking(batting, chk)
#             chk[i] = 0
#             batting.pop()
#
# N = int(input())
# data = [list(map(int, input().split())) for _ in range(N)]
# ans = - 1
# chk = [0] * 9
# batting = []
# for i in range(9):
#     batting.append(i)
#     chk[i] = 1
#     backTraking(batting, chk)
#     batting.pop(- 1)
#     chk[i] = 0
# print(ans)

# from itertools import permutations
# N = int(input())
# data = [list(map(int, input().split())) for _ in range(N)]
# ans = 0
#
# for perm in permutations(range(1, 9)):
#     batting = list(perm)[:3] + [0] + list(perm)[3:]
#     batter, score = 0, 0
#     for inning in data:
#         b1, b2, b3, out = 0, 0, 0, 0
#         while True:
#             hit = inning[batting[batter]]
#             if hit == 0:
#                 out += 1
#             elif hit == 1:
#                 score += b3
#                 b1, b2, b3 = 1, b1, b2
#             elif hit == 2:
#                 score += b2 + b3
#                 b1, b2, b3 = 0, 1, b1
#             elif hit == 3:
#                 score += b1 + b2 + b3
#                 b1, b2, b3 = 0, 0, 1
#             elif hit == 4:
#                 score += b1 + b2 + b3 + 1
#                 b1, b2, b3 = 0, 0, 0
#
#             batter = (batter + 1) % 9
#             if out >= 3:
#                 break
#     if score > ans:
#         ans = score
# print(ans)

# t = int(input())
# for _ in range(t):
#     n, m = map(int, input().split())
#     nf, mf, mnf = 1, 1, 1,
#     for i in range(2, n + 1):
#         nf *= i
#     for i in range(2, m + 1):
#         mf *= i
#     for i in range(2, m - n + 1):
#         mnf *= i
#     print(mf // nf // mnf)

# t = int(input())
# memo0 = [1, 0]
# memo1 = [0, 1]
# for i in range(2, 41):
#     memo0.append(memo0[i - 1] + memo0[i - 2])
#     memo1.append(memo1[i - 1] + memo1[i - 2])
# for _ in range(t):
#     n = int(input())
#     print(memo0[n], memo1[n])

# t = int(input())
# for _ in range(t):
#     x1, y1, x2, y2 = map(int, input().split())
#     n = int(input())
#     ans = 0
#     for _ in range(n):
#         cx, cy, r = map(int, input().split())
#         d1 = ((cx - x1) ** 2 + (cy - y1) ** 2) ** 0.5
#         d2 = ((cx - x2) ** 2 + (cy - y2) ** 2) ** 0.5
#         if d1 < r and d2 < r:
#             pass
#         elif d1 < r:
#             ans += 1
#         elif d2 < r:
#             ans += 1
#     print(ans)

# t = int(input())
# for _ in range(t):
#     a, b = map(int, input().split())
#     a %= 10
#     if a in [1, 5, 6, 0]:
#         if a == 0:
#             print(10)
#         else:
#             print(a)
#     else:
#         b = 4 + b % 4
#         a = str(a ** b)
#         print(a[- 1])

# from itertools import permutations
# n, m = map(int, input().split())
# arr = list(range(1, n + 1))
# for i in permutations(arr, m):
#     print(*i)

# n = int(input())
# for _ in range(n):
#     print(sorted(list(map(int, input().split())))[- 3])

# import sys
# n = int(input())
# for _ in range(n):
#     n = int(sys.stdin.readline())
#     ans = "YES"
#     num = []
#     for _ in range(n):
#         num
#         .append(sys.stdin.readline().strip('\n'))
#     num.sort()
#     for i, j in zip(num, num[1:]):
#         if i == j[:len(i)]:
#             ans = "NO"
#             break
#     print(ans)

# n = int(input())
# for _ in range(n):
#     s = input()
#     s = s[0].upper() + s[1:]
#     print(s)

# def solve(n):
#     end = 666
#     while n != 0:
#         if '666' in str(end):
#             n -= 1
#         end += 1
#     return end
# n = int(input())
# ans = 666
# print(solve(n) - 1)

# import sys
# from collections import deque
# n = int(input())
# q = deque()
# for _ in range(n):
#     cmd = list(sys.stdin.readline().split())
#     if cmd[0] == "push_front":
#         q.appendleft(cmd[1])
#     elif cmd[0] == "push_back":
#         q.append(cmd[1])
#     elif cmd[0] == "pop_front":
#         if not q:
#             print(- 1)
#         else:
#             print(q.popleft())
#     elif cmd[0] == "pop_back":
#         if not q:
#             print(- 1)
#         else:
#             print(q.pop())
#     elif cmd[0] == "size":
#         print(len(q))
#     elif cmd[0] == "empty":
#         if not q:
#             print(1)
#         else:
#             print(0)
#     elif cmd[0] == "front":
#         if not q:
#             print(- 1)
#         else:
#             print(q[0])
#     elif cmd[0] == "back":
#         if not q:
#             print(- 1)
#         else:
#             print(q[- 1])

# import sys
# s = sys.stdin.readline()
# a, b = 0, 0
# for i in range(len(s) - 2):
#     if s[i] == 'J':
#         if s[i + 1] == 'O' and s[i + 2] == 'I':
#             a += 1
#     if s[i] == 'I':
#         if s[i + 1] == 'O' and s[i + 2] == 'I':
#             b += 1
# print(a)
# print(b)

# n, k = map(int, input().split())
# nf = 1
# kf = 1
# nkf = 1
# for i in range(2, n + 1):
#     nf *= i
# for i in range(2, k + 1):
#     kf *= i
# for i in range(2, n - k + 1):
#     nkf *= i
#
# print(nf // kf // nkf)

# n = int(input())
# ans = 0
# for _ in range(n):
#     n, k = map(int, input().split())
#     ans += k % n
# print(ans)

# x, y = map(int, input().split())
# ans = 1
# while True:
#     if (y - x) * ans < y:
#         ans += 1
#     else:
#         break
# print(ans)

# t = int(input())
# for _ in range(t):
#     n, m = map(int, input().split())
#     arr = list(map(int, input().split()))
#     chk = [0] * n
#     chk[m] = 1
#     cnt = 0
#
#     while arr:
#         if arr[0] == max(arr):
#             if chk[0]:
#                 print(cnt + 1)
#                 break
#             else:
#                 arr.pop(0)
#                 chk.pop(0)
#                 cnt += 1
#         else:
#             arr.append(arr.pop(0))
#             chk.append(chk.pop(0))

# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
# ans = 0
# l, r, total = 0, 0, 0
# while True:
#     if total >= m:
#         total -= arr[l]
#         l += 1
#     else:
#         if r == n:
#             break
#         total += arr[r]
#         r += 1
#     if total == m:
#         ans += 1
# print(ans)
# from collections import deque
#
# def solve(cnt):
#     global ans, arr
#     if cnt == 5:
#         for i in range(n):
#             ans = max(ans, max(arr[i]))
#         return
#     temp = [x[:] for x in arr]
#     for k in range(4):
#         move(k)
#         solve(cnt + 1)
#         arr = [x[:] for x in temp]
#
#
# def move(k):
#     if k == 0:  # 상
#         for x in range(n):
#             for y in range(n):
#                 get(y, x)
#             merge(0, x, 1, 0)
#
#     elif k == 1:    # 하
#         for x in range(n):
#             for y in range(n - 1, - 1, - 1):
#                 get(y, x)
#             merge(n - 1, x, - 1, 0)
#
#     elif k == 2:    # 좌
#         for x in range(n):
#             for y in range(n):
#                 get(x, y)
#             merge(x, 0, 0, 1)
#
#     else:   # 우
#         for x in range(n):
#             for y in range(n - 1, - 1, - 1):
#                 get(x, y)
#             merge(x, n - 1, 0, - 1)
#
#
# def get(x, y):
#     if arr[x][y]:
#         q.append(arr[x][y])
#         arr[x][y] = 0
#
#
# def merge(x, y, dx, dy):
#     while q:
#         val = q.popleft()
#
#         if not arr[x][y]:
#             arr[x][y] = val
#
#         elif arr[x][y] == val:
#             arr[x][y] *= 2
#             x += dx
#             y += dy
#
#         else:
#             x += dx
#             y += dy
#             arr[x][y] = val
#
#
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# q = deque()
# ans = 0
# solve(0)
# print(ans)

# arr = [(idx, int(input())) for idx in range(1, 9)]
# arr = sorted(sorted(arr, key = lambda x : x[1])[3:])
# print(sum(i[1] for i in arr))
# for i in arr:
#     print(i[0], end = ' ')
# print()

# n, k = map(int, input().split())
# coin = [int(input()) for _ in range(n)]
# ans = 0
# while k:
#     for i in range(n):
#         if coin[i] > k:
#             ans += k // coin[i - 1]
#             k %= coin[i - 1]
#             break
#     else:
#         ans += k // coin[i]
#         k %= coin[i]
# print(ans)

# n, k = map(int, input().split())
# coin = sorted([int(input()) for _ in range(n)])
# dp = [0] * (k + 1)
#
# for i in range(1, k + 1):
#     a = []
#     for j in coin:
#         if j <= i and dp[i - j] != - 1:
#             a.append(dp[i - j])
#     if a:
#         dp[i] = min(a) + 1
#     else:
#         dp[i] = - 1
# print(dp[k])
# from itertools import permutations
# num = list(permutations(range(1, 10), 3))
# n = int(input())
# for _ in range(n):
#     base, s, b = map(int, input().split())
#     base = list(str(base))
#     removeCnt = 0
#     lenNum = len(num)
#
#     for i in range(lenNum):
#         scnt, bcnt = 0, 0
#         i -= removeCnt
#
#         for j in range(3):
#             base[j] = int(base[j])
#             if base[j] in num[i]:
#                 if j == num[i].index(base[j]):
#                     scnt += 1
#                 else:
#                     bcnt += 1
#         if scnt != s or bcnt != b:
#             num.remove(num[i])
#             removeCnt += 1
# print(len(num))

# import hashlib
# s = input()
# sha = hashlib.sha256(s.encode()).hexdigest()
# print(sha)

# n = int(input())
# ans = 1
# for i in range(1, n + 1):
#     ans *= i
# print(ans)

# n = int(input())
# memo = [1, 1]
# for i in range(2, n + 1):
#     memo.append(memo[i - 1] + 2 * memo[i - 2])
# print(memo[n] % 10007)

# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# print(*sorted(a + b))

# n = int(input())
# for i in range(1, n + 1):
#     print(' ' * (n - i) + '*' * i)
# def ccw(x1, y1, x2, y2, x3, y3):
#     res = (x1 * y2 + x2 * y3 + x3 * y1) - (y1 * x2 + y2 * x3 + y3 * x1)
#     if res < 0:
#         return - 1
#     elif res > 0:
#         return 1
#     else:
#         return 0
#
#
# x1, y1, x2, y2 = map(int, input().split())
# x3, y3, x4, y4 = map(int, input().split())
# ans, chk = 0, 0
# abc = ccw(x1, y1, x2, y2, x3, y3)
# abd = ccw(x1, y1, x2, y2, x4, y4)
# cda = ccw(x3, y3, x4, y4, x1, y1)
# cdb = ccw(x3, y3, x4, y4, x2, y2)
#
# if abc * abd == 0 and cda * cdb == 0:
#     chk = 1
#     if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
#         ans = 1
# if abc * abd <= 0 and cda * cdb <= 0:
#     if not chk:
#         ans = 1
# print(ans)

# n = int(input())
# memo = [1, 1]
# for i in range(2, n + 1):
#     memo.append((memo[i - 1] + memo[i - 2]) % 15746)
# print(memo[n])

# n = int(input())
# arr = sorted(int(input()) for _ in range(n))[:: - 1]
# ans = 0
# for i in range(n):
#     temp = arr[i] * (i + 1)
#     if ans < temp:
#         ans = temp
# print(ans)

# s1, s2, s3 = map(int, input().split())
# arr = [0] * (s1 + s2 + s3 + 1)
#
# for i in range(1, s1 + 1):
#     for j in range(1, s2 + 1):
#         for k in range(1, s3 + 1):
#             arr[i + j + k] += 1
# for i in range(4, s1 + s2 + s3):
#     if arr[i] == max(arr):
#         print(i)
#         break
# from collections import deque
# n, k = map(int, input().split())
# q = deque(range(1, n + 1))
# print('<', end = '')
# while q:
#     for i in range(k - 1):
#         q.append(q.popleft())
#     if len(q) != 1:
#         print(q.popleft(), end = ', ')
#     else:
#         print(q.popleft(), end = '>')
# s = 0
# for _ in range(4):
#     s += int(input())
# print(s // 60)
# print(s % 60)

# c3 = int(input())
# c2 = int(input())
# c1 = c2 + (c2 - c3)
# print(c1)

# import sys
# n = int(input())
# q = []
# for _ in range(n):
#     cmd = list(sys.stdin.readline().split())
#     if cmd[0] == "push":
#         q.append(cmd[1])
#     elif cmd[0] == "pop":
#         if not q:
#             print(- 1)
#         else:
#             print(q.pop(0))
#     elif cmd[0] == "size":
#         print(len(q))
#     elif cmd[0] == "empty":
#         if not q:
#             print(1)
#         else:
#             print(0)
#     elif cmd[0] == "front":
#         if not q:
#             print(- 1)
#         else:
#             print(q[0])
#     elif cmd[0] == "back":
#         if not q:
#             print(- 1)
#         else:
#             print(q[- 1])

# n = int(input())
# arr = sorted(int(input()) for _ in range(n))
# for i in arr:
#     print(i)

# n = int(input())
# dp = [[0] * 10 for _ in range(n + 1)]
# for i in range(1, 10):
#     dp[1][i] = 1
#
# for i in range(2, n + 1):
#     for j in range(10):
#         if j == 0:
#             dp[i][j] = dp[i - 1][1]
#         elif j == 9:
#             dp[i][j] = dp[i - 1][8]
#         else:
#             dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
#
# print(sum(dp[n]) % 1000000000)

# s = input()
# if s == s[:: - 1]:
#     print(1)
# else:
#     print(0)

# laser = input()
# stack = []
# ans = 0
# for i in range(len(laser)):
#     if laser[i] == '(':
#         stack.append(i)
#     else:
#         if stack[- 1] + 1 == i:
#             stack.pop()
#             ans += len(stack)
#         else:
#             stack.pop()
#             ans += 1
# print(ans)

# n, m = map(int, input().split())
# arr = sorted(list(map(int, input().split())))
# minNum = m
# chk = False
#
# for i in range(n - 2):
#     if chk:
#         break
#     for j in range(i + 1, n - 1):
#         if chk:
#             break
#         for k in range(j + 1, n):
#             num = arr[i] + arr[j] + arr[k]
#             if num <= m:
#                 if minNum > m - num:
#                     minNum = m - num
#                     ans = num
#                 if minNum == 0:
#                     chk = True
# print(ans)

# n = int(input())
# for _ in range(n):
#     a, b = map(int, input().split(','))
#     print(a + b)

# bracket = input()
# stack = []
#
# for i in bracket:
#     if i in "([":
#         stack.append(i)
#
#     elif i == ')':
#         temp = 0
#         while stack:
#             val = stack.pop()
#             if val == '[':
#                 print(0)
#                 exit(0)
#             elif val == '(':
#                 if temp == 0:
#                     stack.append(2)
#                 else:
#                     stack.append(2 * temp)
#                 break
#             else:
#                 temp += val
#
#     else:
#         temp = 0
#         while stack:
#             val = stack.pop()
#             if val == '(':
#                 print(0)
#                 exit(0)
#             elif val == '[':
#                 if temp == 0:
#                     stack.append(3)
#                 else:
#                     stack.append(3 * temp)
#                 break
#             else:
#                 temp += val
#
# ans = 0
# for i in stack:
#     if i == '(' or i == '[':
#         ans = 0
#         break
#     else:
#         ans += i
# print(ans)

# print(int((- 1 + (1 + 8 * int(input())) ** 0.5) * 0.5))

# import sys
# sys.setrecursionlimit(10000)
#
# dx = [- 1, 1, 0, 0]
# dy = [0, 0, - 1, 1]
#
# def dfs(y, x):
#     for k in range(4):
#         ny = y + dy[k]
#         nx = x + dx[k]
#         if not (0 <= ny < N and 0 <= nx < M) or not arr[ny][nx]:
#             continue
#         if arr[ny][nx]:
#             arr[ny][nx] = 0
#             dfs(ny, nx)
#
# T = int(input())
# for _ in range(T):
#     M, N, K = map(int, input().split())
#     arr = [[0] * M for _ in range(N)]
#
#     for _ in range(K):
#         x, y = map(int, input().split())
#         arr[y][x] = 1
#
#     ans = 0
#     for y in range(N):
#         for x in range(M):
#             if arr[y][x]:
#                 arr[y][x] = 0
#                 dfs(y, x)
#                 ans += 1
#     print(ans)

# import sys
# sys.setrecursionlimit(10000)
#
# dx = [- 1, 1, 0, 0]
# dy = [0, 0, - 1, 1]
#
# def game(x, y):
#     global chk
#     if not (0 <= x < n and 0 <= y < m) or arr[x][y] == 10:
#         return 0
#     if visited[x][y]:
#         chk = True
#         return - 1
#     if memo[x][y] != - 1:
#         return memo[x][y]
#
#     visited[x][y] = 1
#     move = arr[x][y]
#     for k in range(4):
#         nx = x + dx[k] * move
#         ny = y + dy[k] * move
#         memo[x][y] = max(memo[x][y], game(nx, ny) + 1)
#         if chk:
#             return - 1
#     visited[x][y] = 0
#
#     return memo[x][y]
#
# n, m = map(int, input().split())
# arr = [[10] * m for _ in range(n)]
# visited = [[0] * m for _ in range(n)]
# memo = [[- 1] * m for _ in range(n)]
# chk = False
#
# for i in range(n):
#     data = input()
#     for j in range(m):
#         if data[j] != 'H':
#             arr[i][j] = int(data[j])
# print(game(0, 0))

# a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# s = input()
# for i in a:
#     s = s.replace(i, '*')
# print(len(s))

# import sys
# n = int(sys.stdin.readline())
# arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# arr = sorted(arr, key = lambda x : (x[1], x[0]))
# for i in arr:
#     print(*i)

# n = int(input())
# memo = [0, 1]
# for i in range(2, n + 1):
#     memo.append(memo[i - 1] + memo[i - 2])
# print(memo[n])

# a, b, c = map(int, input().split())
# ans = pow(a, b, c)
# print(ans)

# fact = [1]
# for i in range(1, 101):
#     fact.append(fact[i - 1] * i)
# n, m = map(int, input().split())
# print(fact[n] // fact[m] // fact[n - m])

# n = int(input())
# arr = list(map(int, input().split()))
# ans, temp = 0, 0
# for i in range(1, n):
#     if arr[i] > arr[i - 1]:
#         temp += arr[i] - arr[i - 1]
#     else:
#         temp = 0
#     if ans < temp:
#         ans = temp
# print(ans)

# n = int(input())
# data = list(map(int, input().split()))
# delNode = int(input())
# tree = {}
# for i in range(n):
#     if i == delNode or data[i] == delNode:
#         continue
#     if data[i] in tree:
#         tree[data[i]].append(i)
#     else:
#         tree[data[i]] = [i]
#
# if - 1 in tree:
#     q = [- 1]
# else:
#     q = []
# ans = 0
# while q:
#     node = q.pop()
#     if node not in tree:
#         ans += 1
#     else:
#         q += tree[node]
# print(ans)

# n = int(input())
# for _ in range(n):
#     s = input()
#     if s[: 11] == 'Simon says ':
#         print(s[10:])

# from itertools import permutations
# n = int(input())
# for i in permutations(range(1, n + 1)):
#     print(*i)


# t = int(input())
# for _ in range(t):
#     a, b = map(int, input().split())
#     ans = 0
#     if 1 <= a <= 21:
#         if a <= 1:
#             ans += 500
#         elif a <= 3:
#             ans += 300
#         elif a <= 6:
#             ans += 200
#         elif a <= 10:
#             ans += 50
#         elif a <= 15:
#             ans += 30
#         else:
#             ans += 10
#
#     if 1 <= b <= 31:
#         if b <= 1:
#             ans += 512
#         elif b <= 3:
#             ans += 256
#         elif b <= 7:
#             ans += 128
#         elif b <= 15:
#             ans += 64
#         else:
#             ans += 32
#     print(ans * 10000)
# import math, sys
# def solve(arr):
#     m = sum(arr) / len(arr)
#     sigma = 0
#     for i in arr:
#         sigma += (i - m) ** 2
#     return sigma / len(arr)
#
# n, k = map(int, input().split())
# data = list(map(int, input().split()))
# ans = []
# for i in range(n - k + 1):
#     for j in range(n - k - i + 1):
#         temp = data[i: i + j + k]
#         ans.append(solve(temp))
# print(math.sqrt(min(ans)))
# s, ans, idx, j = [], '', 0, 0
#
# for _ in range(5):
#     temp = input()
#     idx = max(idx, len(temp))
#     s.append(temp)
#
# while j < idx:
#     for i in range(5):
#         if j < len(s[i]):
#             ans += s[i][j]
#     j += 1
# print(ans)

# n = int(input())
# dp = [0] * (n + 1)
# for i in range(2, n + 1):
#     dp[i] = dp[i - 1] + 1
#     if not i % 2:
#         dp[i] = min(dp[i], dp[i // 2] + 1)
#     if not i % 3:
#         dp[i] = min(dp[i], dp[i // 3] + 1)
# print(dp[n])

# n, k = map(int, input().split())
# idx = 0
# for i in range(1, n + 1):
#     if not n % i:
#         idx += 1
#     if idx == k:
#         print(i)
#         break
# else:
#     print(0)
# print("""     /~\\
#     ( oo|
#     _\=/_
#    /  _  \\
#   //|/.\|\\\\
#  ||  \ /  ||
# ============
# |          |
# |          |
# |          |""")
# a = int(input())
# b = int(input())
# print(a + b)
# print(a - b)
# print(a * b)

# T = int(input())
# for test_case in range(T):
#     S = sorted(list(input()))
#     ans = "No"
#     if S[0] == S[1] and S[1] != S[2] and S[2] == S[3]:
#         ans = "Yes"
#     print("#{} {}".format(test_case +1, ans))

# nums = {'c': 26, 'd': 10}
# s = input()
# ans = nums[s[0]]
# for i in range(1, len(s)):
#     val = nums[s[i]]
#     if s[i] == s[i - 1]:
#         val -= 1
#     ans *= val
# print(ans)

# a, b = map(int, input().split())
# print(b - a, b)
# print(*sorted(list(map(int, input().split()))))

# a, b, c = map(int, input().split())
# print(a + b + c)
# import sys
# n = int(sys.stdin.readline())
# arr = sorted([int(sys.stdin.readline()) for _ in range(n)])
# for i in arr:
#     print(i)

# from itertools import permutations
# n, m = map(int, input().split())
# arr = sorted(list(map(int, input().split())))
#
# for i in permutations(arr, m):
#     print(*i)

# a, b = map(int, input().split())
# print(a + b)
# arr = [0] * 31
# for i in range(28):
#     arr[int(input())] = 1
# for i in range(1, 31):
#     if not arr[i]:
#         print(i)

# n = int(input())
# for _ in range(n):
#     temp = list(map(int, input().split()))
#     a = [0] * 5
#
#     for i in temp[1:]:
#         a[i] += 1
#
#     temp = list(map(int, input().split()))
#     b = [0] * 5
#     for i in temp[1:]:
#         b[i] += 1
#     for i in range(4, 0, - 1):
#         if a[i] != b[i]:
#             if a[i] > b[i]:
#                 print("A")
#             else:
#                 print("B")
#             break
#     else:
#         print("D")

# n = int(input())
# for _ in range(n):
#     s = input().split()
#     ans = 'god'
#     for i in s[1:]:
#         ans += i
#     print(ans)

# a, b = map(int, input().split())
# print(a ** 2 - b ** 2)

# k, n, m = map(int, input().split())
# if k * n < m:
#     print(0)
# else:
#     print(k * n - m)

# from itertools import combinations
#
# while True:
#     data = list(map(int, input().split()))
#     if len(data) == 1:
#         break
#     k, s = data[0], data[1:]
#     for i in combinations(s, 6):
#         print(*i)
#     print()

# t = int(input())
# # dp = [0] * 100001
# # dp[1], dp[2], dp[3], dp[4], dp[5], dp[6] = 1, 2, 2, 3, 3, 6
# dp = [0] + [1, 2, 2, 3, 3, 6] + [0] * 99994
# for i in range(7, 100001):
#     dp[i] = ((dp[i - 2] + dp[i - 4]) % 1000000009 + dp[i - 6]) % 1000000009
# for _ in range(t):
#     n = int(input())
#     print(dp[n])

# from itertools import product
# n, m = map(int, input().split())
#
# for i in product(range(1, n + 1), repeat = m):
#     print(*i)

# people, ans = 0, 0
# for _ in range(4):
#     a, b = map(int, input().split())
#     people += b - a
#     if ans < people:
#         ans = people
# print(ans)

# ay, am, ad = map(int, input().split())
# by, bm, bd = map(int, input().split())
# if ay == by:
#     ans1 = 0
# else:
#     if am == bm:
#         if ad <= bd:
#             ans1 = by - ay
#         else:
#             ans1 = by - ay - 1
#     elif am < bm:
#         ans1 = by - ay
#     else:
#         ans1 = by - ay - 1
# ans2 = by - ay + 1
# ans3 = by - ay
# print(ans1)
# print(ans2)
# print(ans3)

# n = int(input())
# c, nc = 0, 0
# for _ in range(n):
#     a = int(input())
#     if a:
#         c += 1
#     else:
#         nc += 1
# if c > nc:
#     print("Junhee is cute!")
# else:
#     print("Junhee is not cute!")

# n = int(input())
# arr = list(map(int, input().split()))
# print(arr.count(int(input())))

# n = int(input())
# ans, idx = 0, 1
#
# while n:
#     if n >= idx:
#         n -= idx
#         idx += 1
#     else:
#         n -= 1
#         idx = 2
#     ans += 1
# print(ans)

# a, b, c = map(int, input().split())
# x = a * b / c
# y = a / b * c
# if x > y:
#     print(int(x))
# else:
#     print(int(y))

# pi = 3.14159265358979323846
# r = int(input())
# ans1 = pi * r ** 2
# ans2 = r ** 2 * 2
# print("%6f" % ans1)
# print("%6f" % ans2)

# c = [1, 1, 2, 2, 2, 8]
# arr = list(map(int, input().split()))
# ans = [0, 0, 0, 0, 0, 0]
# for i in range(6):
#     ans[i] = c[i] - arr[i]
# print(*ans)

# n = int(input())
# arr = sorted(list(map(int, input().split())))
# x = int(input())
# ans = 0
# l, r, ans = 0, n - 1, 0
# while l < r:
#     if arr[l] + arr[r] > x:
#         r -= 1
#     elif arr[l] + arr[r] < x:
#         l += 1
#     else:
#         l += 1
#         r -= 1
#         ans += 1
# print(ans)

# t = int(input())
# for _ in range(t):
#     arr = input()
#     ans = 0
#     for i in range(16):
#         n = int(arr[i])
#         if not i % 2:
#             n *= 2
#             if n > 9:
#                 ans += n // 10
#                 ans += n % 10
#             else:
#                 ans += n
#         else:
#             ans += n
#     if ans % 10:
#         print('F')
#     else:
#         print('T')

# arr = list(map(int, input().split()))
# ans = 0
# for i in arr:
#     ans += i ** 2
# print(ans % 10)

# n, m = map(int, input().split())
# print(1 if n == m else 0)

# n = int(input())
# sx, sy = map(int, input().split())
# ans = 0
# x, y = sx, sy
# for _ in range(n - 1):
#     nx, ny = map(int, input().split())
#     ans += abs(nx + ny - x - y)
#     x, y = nx, ny
# ans += abs(x + y - sx - sy)
# print(ans)

# b = int(input())
# ans1 = 5 * b - 400
# ans2 = 0
# if b > 100:
#     ans2 = - 1
# elif b < 100:
#     ans2 = 1
# print(ans1)
# print(ans2)

dx = [- 1, 1, 0, 0]
dy = [0, 0, - 1, 1]

T = int(input())
for test_case in range(1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0] * M for _ in range(N)]
    sea = [[0] * M for _ in range(N)]
    z = 1

    for i in range(N):
        for j in range(M):
            if arr[i][j] and not visited[i][j]:
                visited[i][j] = 1
                arr[i][j] = z
                s = [(i, j)]
                while s:
                    x, y = s.pop()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                            if arr[nx][ny]:
                                visited[nx][ny] = 1
                                arr[nx][ny] = z
                                s.append((nx, ny))
                            else:
                                sea[x][y] = 1
                z += 1

    cost = [[float('inf')] * z for _ in range(z)]

    for i in range(N):
        for j in range(M):
            if sea[i][j]:
                z = arr[i][j]
                for k in range(4):
                    cnt = 0
                    x, y = i, j
                    while True:
                        x = x + dx[k]
                        y = y + dy[k]
                        if 0 <= x < N and 0 <= y < M and not arr[x][y]:
                            cnt += 1
                        else:
                            break
                    if 0 <= x < N and 0 <= y < M and arr[x][y] != z and cnt >= 2:
                        nz = arr[x][y]
                        cost[z][nz] = cost[nz][z] = min(cnt, cost[z][nz])

    for i in range(1, z):
        if cost[i] == [float('inf')] * z:
            ans = - 1
            break
    else:
        visited = [0] * z
        key = [float('inf')] * z
        key[1] = 0
        ans = 0
        for _ in range(1, z):
            minKey = float('inf')
            idx = - 1

            for n in range(1, z):
                if not visited[n] and key[n] < minKey:
                    minKey = key[n]
                    idx = n

            visited[minKey] = 1
            ans += minKey

            for i in range(1, z):
                if not visited[i] and cost[idx][i] < key[i]:
                    key[i] = cost[idx][i]

    if ans == float('inf'):
        ans = - 1

    print(ans)