import sys
sys.stdin = open("D4_3814_input.txt", "r")


T = int(input())
for test_case in range(T):
    N, K = map(int, input().split())
    data = list(map(int, input().split()))
    temp = data
    ans, s, e = 0, 0, N

    while s < e:
        m = (s + e) // 2
        check = True

        for i in range(N - 1):
            if data[i + 1] - data[i] >= m:
                K -= data[i + 1] - data[i] - m
                data[i + 1] -= data[i + 1] - data[i] - m

                if K < 0:
                    check = False
                    break

        for i in range(N - 1, 0, - 1):
            if data[i - 1] - data[i] >= m:
                K = K - data[i - 1] - data[i] - m
                data[i - 1] -= data[i - 1] - data[i] - m

                if K < 0:
                    check = False
                    break

        if check:
            e = m
        else:
            s = m + 1
            ans = s

    print("#{} {}".format(test_case + 1, ans))

