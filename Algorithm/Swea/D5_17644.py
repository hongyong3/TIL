import sys

sys.stdin = open("D5_17644_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, X = map(int, input().split())
    ans = [i for i in range(1, N + 1)]
    if (N == 1 and X != 0) or X > 2 ** (N - 1) - 1:
        ans = - 1
    else:
        x = 0
        if X > 1:
            x = 1
            while True:
                if 2 ** (x - 1) - 1 <= X:
                    x += 1
                else:
                    x -= 1
                    break
            X -= 2 ** (x - 1) - 1
            ans = ans[1:x] + [1] + ans[x:]
        while X:
        print(X, x)
        print(ans)
        # while X:

    # print("#{} {}".format(test_case + 1, ans))
