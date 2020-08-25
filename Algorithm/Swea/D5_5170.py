import sys
sys.stdin = open("D5_5170_input.txt", "r")

# 방법1 list
# def solve(p1, p2):
#     if p1[0] == p2[0]:
#         return 9999
#     return (p2[1] - p1[1]) / (p2[0] - p1[0])
#
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     data = sorted([list(map(int, input().split())) for _ in range(N)])
#     arr = []
#     for i in range(N):
#         for j in range(i + 1, N):
#             arr.append(solve(data[i], data[j]))
#     print("#{} {}".format(test_case + 1, len(set(arr))))

# 방법2 set
# def solve(p1, p2):
#     if p1[0] == p2[0]:
#         return 9999
#     return (p2[1] - p1[1]) / (p2[0] - p1[0])
#
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     data = sorted([list(map(int, input().split())) for _ in range(N)])
#     arr = set()
#     for i in range(N):
#         for j in range(i + 1, N):
#             arr.add(solve(data[i], data[j]))
#     print("#{} {}".format(test_case + 1, len(arr)))

# 방법3 재귀없이
T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    arr = set()
    check = False
    for i in range(N):
        for j in range(i + 1, N):
            if data[i][0] == data[j][0]:
                check = True
                continue
            else:
                arr.add((data[j][1] - data[i][1]) / (data[j][0] - data[i][0]))
    print("#{} {}".format(test_case + 1, len(arr) + check))