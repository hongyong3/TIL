import sys
sys.stdin = open("D4_4699_input.txt", "r")

m = [[0] * 2002 for _ in range(2002)]
T = int(input())
for test_case in range(T):
    L, K = map(int, input().split())
    data, price = input(), {}
    for k in range(K):
        p1, p2 = map(int, input().split())
        price[chr(97 + k)] = min(p1, p2)

    for i in range(L):
        m[i][i] = 0
        for j in range(i + 1, L):
            m[i][j] = float('inf')

    for k in range(1, L):
        i, j = 0, k
        for _ in range(L - k):
            m[i][j] = min(m[i][j], m[i + 1][j] + price[data[i]])
            m[i][j] = min(m[i][j], m[i][j - 1] + price[data[j]])
            if data[i] == data[j]:
                m[i][j] = min(m[i][j], m[i + 1][j - 1])
            i += 1
            j += 1
    print("#{} {}".format(test_case + 1, m[0][L - 1]))