import sys
sys.stdin = open("D1_2072_input.txt", "r")

T = int(input())
for test_case in range(T):
    print("#{} {}".format(test_case + 1, sum(i for i in list(map(int, input().split())) if i % 2)))

# T = int(input())
# for t in range(T):
#     numbers = list(map(int, input().split()))
#     sum = 0
#     r = []
#     for i in range(len(numbers)):
#         if numbers[i] % 2 != 0:
#             r.append(numbers[i])
#     print(r)
#     print("#{} {}".format(t, sum(r)))

# T = int(input())
# for t in range(1, T + 1):
#     numbers = list(map(int, input().split()))
#     ans = 0
#     for i in range(len(numbers)):
#         if numbers[i] % 2 != 0:
#             ans += numbers[i]
#     print("#{0} {1}".format(t, ans))