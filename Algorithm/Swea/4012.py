import sys
sys.stdin = open("4012_input.txt", "r")

from itertools import combinations

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    ans = float('inf')
    for g1 in combinations(range(N), N // 2):
        g2 = [i for i in range(N) if i not in g1]
        food1, food2 = 0, 0
        for i in range(N // 2 - 1):
            for j in range(i + 1, N // 2):
                food1 += data[g1[i]][g1[j]] + data[g1[j]][g1[i]]
                food2 += data[g2[i]][g2[j]] + data[g2[j]][g2[i]]

        temp = abs(food1 - food2)
        if temp < ans:
            ans = temp
    print("#{} {}".format(test_case + 1, ans))