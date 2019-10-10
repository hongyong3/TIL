import sys
sys.stdin = open("D4_6959_input.txt", "r")

# def solve(data):
#     global count
#     if len(data) >= 3:
#         ans = str(data[0: len(data) - 2]) + str(int(data[- 2]) + int(data[- 1]))
#         count += 1
#         solve(ans)
#     elif len(data) == 2:
#         ans = str(int(data[- 2]) + int(data[- 1]))
#         count += 1
#         solve(ans)
#     return count
#
# T = int(input())
# for test_case in range(T):
#     data = str(input())
#     if len(data) == 1:
#         print("#{} {}".format(test_case + 1, "B"))
#         continue
#     count = 0
#     solve(data)
#     if count % 2:
#         print("#{} {}".format(test_case + 1, "A"))
#     else:
#         print("#{} {}".format(test_case + 1, "B"))

T = int(input())
for test_case in range(T):
    data = str(input())
    ans, count = 0, 0
    for i in range(len(data)):
        ans += int(data[i])
        count += 1
        if ans >= 10:
            ans = ans // 10 + ans % 10
            count += 1
    if count % 2:
        print("#{} {}".format(test_case + 1, "B"))
    else:
        print("#{} {}".format(test_case + 1, "A"))