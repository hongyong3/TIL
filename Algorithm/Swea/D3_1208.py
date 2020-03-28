import sys
sys.stdin = open("D3_1208_input.txt", "r")

# 이전 풀이
# T = 10
# for test_case in range(1, T+1):
#     dump = 0
#     N = int(input())
#     dump = list(map(int, input().split()))
#     count = 0
#
#     for i in range(len(dump) - 1, 0, -1):
#         for j in range(0, i):
#             if dump[j] > dump[j + 1]:
#                 dump[j], dump[j + 1] = dump[j + 1], dump[j]
#
#     while N > 0:
#         dump[0] = dump[0]+1
#         dump[-1] = dump[-1]-1
#
#         for i in range(len(dump) - 1, 0, -1):
#             for j in range(0, i):
#                 if dump[j] > dump[j + 1]:
#                     dump[j], dump[j + 1] = dump[j + 1], dump[j]
#         N -= 1
#         count = dump[-1] - dump[0]
#     print("#{} {}".format(test_case, count))

# 방법 1
# import time
# start = time.time()
#
# # 16.84862780570984s
# for test_case in range(10):
#     N = int(input())
#     data = list(map(int, input().split()))
#
#     for i in range(len(data) - 1, 0, - 1):
#         for j in range(0, i):
#             if data[j] > data[j + 1]:
#                 data[j], data[j + 1] = data[j + 1], data[j]
#
#     while N > 0:
#         data[0], data[- 1] = data[0] + 1, data[- 1] - 1
#         for i in range(99, 0, - 1):
#             for j in range(0, i):
#                 if data[j] > data[j + 1]:
#                     data[j], data[j + 1] = data[j + 1], data[j]
#         N -= 1
#     print("#{} {}".format(test_case + 1, data[- 1] - data[0]))
#
# print(time.time() - start)

# 방법 2
# 0.08579182624816895s
import time
start = time.time()

for test_case in range(10):
    N = int(input())
    data = sorted(list(map(int, input().split())))

    while N > 0:
        data[0], data[- 1] = data[0] + 1, data[- 1] - 1
        data = sorted(data)
        N -= 1
    print("#{} {}".format(test_case + 1, data[- 1] - data[0]))

print(time.time() - start)