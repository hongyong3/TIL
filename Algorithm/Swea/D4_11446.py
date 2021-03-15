import sys
sys.stdin = open("D4_11446_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int,input().split())
    data = list(map(int, input().split()))
    low, high = 1, max(data)

    while low <= high:
        mid = (low + high) // 2
        total = 0
        for i in data:
            total += (i // mid)
        if total < M:
            high = mid - 1
        else:
            low = mid + 1
    print("#{} {}".format(test_case + 1, high))