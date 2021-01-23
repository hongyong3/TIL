import sys
sys.stdin = open("D5_6484_input.txt", "r")

# arr = [0] * 100001
# arr[0] = 1
# T = int(input())
# for test_case in range(T):
#     N, K = map(int, input().split())
#     for i in range(1, N + 1):
#         arr[i] = (arr[i - 1] * i) % 1000000007
T = int(input())
for test_case in range(T):
    N, K = map(int, input().split())
    num, arr, ans, idx = 1, {}, 1, 2
    for i in range(N - K + 1, N + 1):
        num = (num * i) % 100000007
    for i in range(1, K + 1):
        num = (num // i) % 100000007
    num %= 100000007

    while num != 1:
        if num % idx == 0:
            num //= idx
            if idx not in arr:
                arr[idx] = 1
            else:
                arr[idx] += 1
        else:
            idx +=1

    for i in arr.values():
        ans *= (i + 1)

    print("#{} {}".format(test_case + 1, ans % 1000000007))