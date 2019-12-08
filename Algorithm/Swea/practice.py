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


dx = [- 1, 1, 0, 0]
dy = [0, 0, - 1, 1]

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

dx = [- 1, 1, 0, 0]
dy = [0, 0, - 1, 1]

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    result = [0] * (N ** 2)
    for x in range(N):
        for y in range(N):
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if (0 <= nx < N and 0 <= ny < N) and (data[nx][ny] == data[x][y] + 1):
                    result[data[x][y] - 1] = 1

    for i in range((N ** 2) - 1, - 1, - 1):
        if result[i]:
            result[i] = result[i + 1] + 1
        else:
            result[i] = 1

    answer = max(result)
    for i in range((N ** 2) + 1):
        if result[i] == answer:
            print("#{} {} {}".format(test_case + 1, i + 1, result[i]))
            break