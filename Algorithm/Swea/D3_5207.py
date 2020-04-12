import sys
sys.stdin = open("D3_5207_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    count = 0

    for num in B:
        start, end, flag = 0, N - 1, 0

        while start <= end:
            mid = (start + end) // 2

            if num >= A[mid]:
                if num == A[mid]:
                    count += 1
                    break
                start = mid + 1
                if flag == 1:
                    break
                flag = 1
            else:
                end = mid - 1
                if flag == - 1:
                    break
                flag = - 1
    print("#{} {}".format(test_case + 1, count))