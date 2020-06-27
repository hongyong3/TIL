import sys
sys.stdin = open("D6_1266_input.txt", "r")

perAB = [[0] * 19 for _ in range(19)]
def solve():
    perAB[0][0] = 1
    for i in range(1, 19):
        for j in range(min(i, 18) + 1):
            perAB[i][j] = perAB[i - 1][j - 1] + perAB[i - 1][j]

T = int(input())
solve()
for test_case in range(T):
    a, b = map(int, input().split())
    a, b = a / 100, b / 100
    perA, perB = [1] + [0] * 18, [1] + [0] * 18

    for i in range(1, 19):
        perA[i] = 1.0 * perAB[18][i]
        perB[i] = 1.0 * perAB[18][i]
        for j in range(1, i + 1):
            perA[i] *= (1.0 * a)
            perB[i] *= (1.0 * b)
        for j in range(18 - i):
            perA[i] *= (1.0 - (1.0 * a))
            perB[i] *= (1.0 - (1.0 * b))

    ansA, ansB = 0.0, 0.0
    for i in [2, 3, 5, 7, 11, 13, 17]:
        ansA += perA[i]
        ansB += perB[i]

    print("#{} {}".format(test_case + 1, format(ansA + ansB - ansA * ansB, ".6f")))