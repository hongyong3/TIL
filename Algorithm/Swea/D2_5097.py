import sys
sys.stdin = open("D2_5097_input.txt", "r")

# 이전 풀이
# T = int(input())
# for test_case in range(1, T+1):
#     N, M = list(map(int, input().split()))
#     data = list(input().split())
#     ans = data[M % N]
#     print(f"#{test_case} {ans}")

# 풀이 1
T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    print("#{} {}".format(test_case + 1, data[M % N]))

# 풀이 2
T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    print("#{} {}".format(test_case + 1, list(map(int, input().split()))[M % N]))