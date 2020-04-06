import sys
sys.stdin = open("D3_5202_input.txt", "r")

# 이전 풀이
# T = int(input())
# def check(data):
#     visited = [0] * 24
#     count = 0
#     for i in range(N):
#         if 1 in visited[data[i][0]:data[i][1]]:
#             pass
#         else:
#             count += 1
#             for j in range(data[i][0], data[i][1]):
#                 visited[j] += 1
#     return count
#
# for test_case in range(T):
#     N = int(input())
#     data = [list(map(int, input().split())) for _ in range(N)]
#     data.sort(key=lambda x : x[1])
#     print('#{} {}'.format(test_case+1, check(data)))

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    data.sort(key = lambda x: x[1])

    ans = 0
    time = [0] * 24
    for i in data:
        if 1 in time[i[0]:i[1]]:
            pass
        else:
            ans += 1
            for j in range(i[0], i[1]):
                time[j] += 1
    print("#{} {}".format(test_case + 1, ans))