import sys
sys.stdin = open("D3_5215_input.txt", "r")

# def combination(score, cal, k):
#     global maxScore, N
#     if k + 1 > N:
#         if cal <= L and score > maxScore:
#             maxScore = score
#         return
#     combination(score, cal, k + 1)
#     combination(score + data[k][0], cal + data[k][1], k + 1)
#
#
# T = int(input())
# for test_case in range(T):
#     N, L = map(int, input().split())
#     data = [list(map(int, input().split())) for _ in range(N)]
#     maxScore = 0
#     combination(0, 0, 0)
#     print("#{} {}".format(test_case + 1, maxScore))

T = int(input())
for Count in range(T):
    N, L = map(int, input().split())
    score_list = [0]
    cal_list = [0]
    for _ in range(N):
        score, cal = map(int, input().split())
        F_score_list = score_list[:]
        F_cal_list = cal_list[:]
        if cal > L:
            continue
        for i in range(len(score_list)):
            if cal_list[i] + cal <= L:
                if cal_list[i] + cal in cal_list:
                    idx = cal_list.index(cal_list[i] + cal)
                    if score_list[idx] < score_list[i] + score:  # ? vs 300
                        F_score_list[idx] = F_score_list[i] + score
                else:
                    F_score_list.append(score_list[i] + score)
                    F_cal_list.append(cal_list[i] + cal)
        score_list = F_score_list[:]
        cal_list = F_cal_list[:]

    print("#{} {}".format(Count + 1, max(score_list)))