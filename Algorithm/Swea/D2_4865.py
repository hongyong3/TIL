import sys
sys.stdin = open("D2_4865_input.txt", "r")

# 이전 풀이
# T = int(input())
# for test_case in range(1, T+1):
#     data_1 = str(input())
#     data_2 = str(input())
#     x = {}
#     for i in data_1:
#         x[i] = 0
#     for i in data_2:
#         if i in data_1:
#             x[i] += 1
#     # ans = max(list(x.values()))
#     ans = max(x.values())
#     print("#{} {}".format(test_case, ans))

T = int(input())
for test_case in range(T):
    # str1 = list(set(input()))
    # str1 = set(input())
    str1 = input()
    str2 = input()
    ans = 0
    for i in str1:
        ans = max(ans, str2.count(i))
    print("#{} {}".format(test_case + 1, ans))