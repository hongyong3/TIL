import sys
sys.stdin = open("D2_4880_input.txt", "r")

# 이전 풀이
# def tournament(data, x, y):
#     a = data[x]
#     b = data[y]
#     if a == b:
#         return x
#     elif a == 1 and  b == 2:
#         return y
#     elif a == 1 and b == 3:
#         return x
#     elif a == 2 and b == 1:
#         return x
#     elif a == 2 and b == 3:
#         return y
#     elif a == 3 and b == 1:
#         return y
#     elif a == 3 and b == 2:
#         return x
#
# def game(data, start, end):
#     if end-start >=1:
#         middle = int((start+end) // 2)
#         return tournament(data, game(data, start, middle), game(data, middle+1, end))
#     elif start == end:
#         return start
#
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     data = list(map(int, input().split()))
#     print(f"#{test_case+1} {game(data, 0, N-1) + 1}")

# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     data = [[x + 1, y] for x, y in enumerate(map(int, input().split()))]
#
#     while len(data) > 1:
#         for _ in range(0, len(data), 2):
#             p1, p2 = data.pop(0), data.pop(0)
#             if (p1[1] == 2 and p2[1] == 1) or (p1[1] == 3 and p2[1] == 2) or (p1[1] == 1 and p2[1] == 3) or (p1[0] < p2[0] and p1[1] == p2[1]):
#                 data.append(p1)
#             else:
#                 data.append(p2)
#     print("#{} {}".format(test_case + 1, data[0][0]))


# 실패

# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     data = [[x + 1, y] for x, y in enumerate(map(int, input().split()))]
#     print(data)
#
#     while len(data) > 1:
#         for _ in range(0, len(data), 2):
#             p1, p2 = data.pop(0), data.pop(0)
#
#             if (p1[1] - p2[1] == 1) or (p1[1] - p2[1] == - 2) or (p1[0] < p2[0] and p1[1] == p2[1]):
#                 data.append(p1)
#             elif (p1[1] - p2[1] == - 1) or (p1[1] - p2[1] == 2):
#                 data.append(p2)
#             # else:
#             #     data.append(p2)
#     print("#{} {}".format(test_case + 1, data[0][0]))

def match(x, y):
    if data[x - 1] - data[y - 1] == 1 or data[x - 1] - data[y - 1] == - 2 or data[x - 1] == data[y - 1]:
        return x
    return y

def tournament(start, end):
    if start == end:
        return start
    first = tournament(start, (start + end) // 2)
    second = tournament((start + end) // 2 + 1, end)
    return match(first, second)

T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    print("#{} {}".format(test_case + 1, tournament(1, N)))