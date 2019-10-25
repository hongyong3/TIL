import sys
sys.stdin = open("D4_7701_input.txt", "r")
# def solve(data):
#     return sorted(sorted(data), key = lambda x : x[0])
#
# T = int(input())
# for test_case in range(T):
#     N, data = int(input()), []
#     for i in range(N):
#         data += list(map(str, input().split()))
#     data = list(set(data))
#     ans = solve(data)
#     print("#{}".format(test_case + 1))
#     for i in ans:
#         print(i)`

T = int(input())
for test_case in range(1):
    N = int(input())
    data = []
    for i in range(N):
        data += list(map(str, input().split()))
    data = sorted(list(set(data)))
    data.sort(key=len, reverse=True)