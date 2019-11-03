import sys
sys.stdin = open("D4_3812_input.txt", "r")

T = int(input())
for test_case in range(T):
    X, Y, Z, A, B, C, N = map(int, input().split())
    if N == 1:
        print("#{} {}".format(test_case + 1, X*Y*Z))
    ans = [0 for _ in range(N)]
    for x in range(X):
        for y in range(Y):
            for z in range(Z):
                ans[(abs(x - A) + abs(y - B) + abs(z - C)) % N] += 1
    print("#{}".format(test_case + 1), *ans)