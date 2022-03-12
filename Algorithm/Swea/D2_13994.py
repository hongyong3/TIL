import sys
sys.stdin = open("D2_13994_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    arr = [0] * 1001
    ans = 0
    for _ in range(N):
        K, A, B = map(int, input().split())
        if K == 1:
            for i in range(A, B + 1):
                arr[i] += 1
        elif K == 2:
            for i in range(A, B + 1, 2):
                arr[i] += 1
        else:
            for i in range(A, B + 1):
                if (A % 2 and not i % 3 and i % 10) or (not A % 2 and not i % 4):
                    arr[i] += 1
    print("#{} {}".format(test_case + 1, max(arr)))