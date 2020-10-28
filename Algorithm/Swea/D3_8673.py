import sys
sys.stdin = open("D3_8673_input.txt", "r")

# T = int(input())
# for test_case in range(T):
#     K = int(input())
#     data = list(map(int, input().split()))
#     ans = 0
#     while K:
#         for i in range(pow(2, K - 1)):
#             ans += abs(data[2 * i] - data[2 * i + 1])
#             win = data[2 * i] if data[2 * i] > data[2 * i + 1] else data[2 * i + 1]
#             data.append(win)
#         data = data[pow(2, K):]
#         K -= 1
#     print("#{} {}".format(test_case + 1, ans))

T = int(input())
for test_case in range(T):
    K = int(input())
    data = list(map(int, input().split()))
    ans = 0
    while K:
        for i in range(0, pow(2, K), 2):
            ans += abs(data[i] - data[i + 1])
            win = data[i] if data[i] > data[i + 1] else data[i + 1]
            data.append(win)
        data = data[pow(2, K):]
        K -= 1
    print("#{} {}".format(test_case + 1, ans))