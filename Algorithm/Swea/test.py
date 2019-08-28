import sys
sys.stdin = open("test_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    ans, X, count = [], N - 1, 0
    for i in range(1, N + 1):
        ans.append(i)

    if data == ans or data == ans[:: -1]:
        print("#{} {}".format(test_case + 1, count))
        continue
    else:
        for j in range(N//2):
            count += 1
            if j % 2 == 0:
                data[N // 2 - 1 + j], data[N // 2 + j] = data[N // 2 + j], data[N // 2 - 1 + j]
                if data == ans or data == ans[:: -1]:
                    if count <= 5:
                        print("#{} {}".format(test_case + 1, count))
                        continue
                    else:
                        print("#{} {}".format(test_case + 1, -1))
                        continue
            else:
                data[N // 2 - 1 + j], data[N // 2 + j] = data[N // 2 + j], data[N // 2 - 1 + j]
                data[N // 2 - 1 - j], data[N // 2 - j] = data[N // 2 - j], data[N // 2 - 1 - j]
                if data == ans or data == ans[:: -1]:
                    if count <= 5:
                        print("#{} {}".format(test_case + 1, count))
                        continue
                    else:
                        print("#{} {}".format(test_case + 1, -1))
                        continue