import sys
sys.stdin = open("D4_8568_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [0] + list(map(int, input().split()))
    arr = [[0] * 3 for _ in range(3)]
    for i in range(1, N + 1):
        if data[i] % 3 != i % 3:
            arr[i % 3][data[i] % 3] += 1
    print("#{} {}".format(test_case + 1, arr[0][1] + arr[0][2] + max(arr[1][2], arr[2][1])))

# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     data = list(map(int, input().split()))
#     arr = [[0] * 3 for _ in range(3)]
#     for i in range(N):
#         if data[i] % 3 != i % 3:
#             arr[i % 3][data[i] % 3] += 1
#     print("#{} {}".format(test_case + 1, arr[0][1] + arr[0][2] + max(arr[1][2], arr[2][1])))