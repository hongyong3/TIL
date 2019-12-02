import sys
sys.stdin = open("부분집합의합_input.txt")

T = int(input())
A = list(range(1, 13))
n = len(A)
for test_case in range(1, T+1):
    N, K = map(int, input().split())

    for i in range(1 << n):  # 1<<n : 부분 집합의 갯수
        sum = 0
        count = 0
        count_1 = 0
        for j in range(n):  # # 원소의 수만큼 비트를 비교
            if i & (1 << j):  # i의 j번째 비트가 1이면 j번째 원소 출력 10진수를 2진수로
                sum += A[j]
                count_1 += 1
            if sum == K and count_1 == N:
                count += 1
    print("#{} {}".format(test_case, count))