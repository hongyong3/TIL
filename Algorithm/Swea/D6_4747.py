import sys
sys.stdin = open("D6_4747_input.txt", "r")

# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     data = sorted(list(map(int, input().split())))
#     avg = sum(data) // 3
#     # ans = [[data.pop(- 3)], [data.pop(- 2)], [data.pop(- 1)]]
#     ans = [[], [], []]
#     idx, start = 0, 0
#     total = sum(ans[idx])
#
#     # while문은 노답인듯..
#     # 재귀로 가자
#     while idx < 2:
#         if total == avg:
#
#             idx += 1
#             start = 0
#         total = sum(ans[idx])
#         for i in range(start, len(data)):
#             if start > len(data):
#                 idx -= 1
#                 data.aooend(ans[idx].pop())
#                 break
#             if total + data[i] > avg:
#                 total -= ans[idx][- 1]
#                 data.insert(start, ans[idx].pop())
#                 start += 1
#                 break
#             temp = data.pop(i)
#             ans[idx].append(temp)
#             total += temp
#             start = i
#             break

# 201 / 300 Runtime Error
# def solve(idx, total, start):
#     global ans, chk
#     if chk:
#         return
#     if idx == 3:
#         print("#{}".format(test_case + 1))
#         for i in ans:
#             print(*i)
#         chk = True
#     if total == avg:
#         solve(idx + 1, 0, 0)
#     for i in range(start, len(data)):
#         if chk or total + data[i] > avg:
#             return
#         temp = data.pop(i)
#         ans[idx].append(temp)
#         solve(idx, total + temp, i)
#         data.insert(i, ans[idx].pop())
#
#
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     data = sorted(list(map(int, input().split())))
#     avg = sum(data) // 3
#     chk = False
#     ans = [[], [], []]
#     solve(0, 0, 0)

# reverse하닌까 풀림..
def solve(idx, total, start):
    global ans, chk
    if chk:
        return
    if idx == 3:
        print("#{}".format(test_case + 1))
        for i in ans[:: - 1]:
            print(*i[:: - 1])
        chk = True
    if total == avg:
        solve(idx + 1, 0, 0)
    for i in range(start, len(data)):
        if chk or total + data[i] > avg:
            return
        temp = data.pop(i)
        ans[idx].append(temp)
        solve(idx, total + temp, i)
        data.insert(i, ans[idx].pop())


T = int(input())
for test_case in range(T):
    N = int(input())
    data = sorted(list(map(int, input().split())), reverse = True)
    avg = sum(data) // 3
    chk = False
    ans = [[], [], []]
    solve(0, 0, 0)