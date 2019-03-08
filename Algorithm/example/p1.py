T = int(input())
for test_case in range(T):
    N, K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    ans = [[0 for _ in range(K)] for _ in range(K)]
    stack = []
    answer = []
    L_sum, R_sum = 0, 0

    for k in range(N-K+1):
        for i in range(K):
            for j in range(K):
                ans[i][j] = data[i+k][j+k]
    stack.append(ans)

    for k in range(len(stack)):
        for i in range(len(ans)):
            R_sum += stack[k][i][i]
            L_sum += stack[k][len(ans)-1-i][i]

    answer.append(max(R_sum, L_sum) - min(R_sum, L_sum))
    answer2 = min(answer)
    R_sum = 0
    L_sum = 0
    print("#{} {}".format(test_case+1, answer2))