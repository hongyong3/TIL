import sys
sys.stdin = open("배열 최소 합_input.txt", "r")

# 방법 1
# def permutation(all_arr, count, visited, sum_x):
#     global data, min_x
#     if sum_x > min_x:
#         return
#     if count >= all_arr:
#         min_x = min(min_x, sum_x)
#         return
#     for i in range(all_arr):
#         if visited[i] == 1:
#             continue
#         visited[i] = 1
#         permutation(all_arr, count+1, visited, sum_x + data[count][i])
#         visited[i] = 0
#

#
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     data = [[0 for _ in range(N)] for _ in range(N)]
#     visited = [0] * N   # 중복방지를 위한 check list
#     min_x = 10000000
#     for i in range(N):
#         data[i] = list(map(int,input().split()))
#     permutation(N, 0, visited, 0)
#     print(f'#{test_case+1} {min_x}')

# 방법 2
def MinSum(k):
    global min, sum, N
    if k == N:
        if min > sum:
            min = sum
    for i in range(N):
        if visit[i] == 0:
            if sum > min:
                continue
            else:
                visit[i] = 1
                sum += data[i][k]
                MinSum(k+1)
                visit[i] = 0
                sum -= data[i][k]
T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    visit = [0]*N
    min = 10**10
    sum = 0
    MinSum(0)

    print('#{} {}'.format(test_case+1, min))