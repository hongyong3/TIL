import sys
sys.stdin = open("D3_7728_input.txt", "r")

# T = int(input())
# for test_case in range(T):
#     print("#{} {}".format(test_case + 1, len(set(map(str, input())))))

# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     arr = [0] * 10
#
#     while N:
#         arr[N % 10] = 1
#         N //= 10
#     print("#{} {}".format(test_case + 1, arr.count(1)))

T = int(input())
for test_case in range(T):
    N = int(input())
    arr = [0] * 10
    ans = 0

    while N:
        arr[N % 10] = 1
        N //= 10

    for i in range(10):
        if arr[i]:
            ans += 1
    print(ans)