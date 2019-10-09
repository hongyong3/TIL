import sys
sys.stdin = open("D4_6959_input.txt", "r")

# def solve(data):
#     global count
#     ans = []
#     if len(data) >= 3:
#         for i in range(len(data) - 2):
#             ans += data[i]
#     ans += str(int(data[- 2]) + int(data[- 1]))
#     count += 1
#     if len(ans) > 1:
#         solve(ans)
#
# T = int(input())
# for test_case in range(T):
#     data = str(input())
#     count = 0
#     if len(data) < 2:
#         print("#{} {}".format(test_case + 1, 'B'))
#     else:
#         solve(data)
#         answer = "B"
#         if count % 2: answer = "A"
#         print("#{} {}". format(test_case + 1, answer))
def solve(data):
    global count
    if len(data) == 1:
        return count
    if len(data) >= 3:
        ans = str(data[0: len(data) - 2]) + str(int(data[- 2]) + int(data[- 1]))
        count += 1
        solve(ans)
    else:
        ans = str(int(data[- 2]) + int(data[- 1]))
        count += 1
        solve(ans)


T = int(input())
for test_case in range(T):
    data = str(input())
    count = 0
    solve(data)
    if count % 2:
        print("#{} {}".format(test_case + 1, "A"))
    else:
        print("#{} {}".format(test_case + 1, "B"))