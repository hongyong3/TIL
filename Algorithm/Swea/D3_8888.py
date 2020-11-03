import sys
sys.stdin = open("D3_8888_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M, P = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    grade = [[0, 0, i] for i in range(1, N + 1)]  # 점수, 푼 문제 수, 참가자
    score = [0] * M

    for i in range(N):
        grade[i][1] = sum(data[i])
        for j in range(M):
            if not data[i][j]:
                score[j] += 1

    for i in range(N):
        for j in range(M):
            grade[i][0] += score[j] * data[i][j]

    grade = sorted(grade, key= lambda x : (- x[0], - x[1], x[2]))

    for i in range(N):
        if grade[i][2] == P:
            ans = (grade[i][0], i + 1)
            break
    print("#{}".format(test_case + 1), *ans)