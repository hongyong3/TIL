import sys
sys.stdin = open("베이비진 게임_input.txt", "r")

T = int(input())
for test_case in range(T):
    data = list(map(int, input().split()))
    flag = 0
    A_ans = [0] * 12
    B_ans = [0] * 12

    for i in range(len(data)//2):
        A_ans[data[2 * i]] += 1
        B_ans[data[2 * i + 1]] += 1
        if i >= 2:
            # A
            if A_ans[data[2 * i]] == 3:
                flag = 1
                break
            elif A_ans[data[2 * i]] != 0 and A_ans[data[2 * i] - 1] != 0 and A_ans[data[2 * i] + 1] != 0:
                flag = 1
                break
            elif A_ans[data[2 * i]] != 0 and A_ans[data[2 * i] + 1] != 0 and A_ans[data[2 * i] + 2] != 0:
                flag = 1
                break
            elif A_ans[data[2 * i]] != 0 and A_ans[data[2 * i] - 1] != 0 and A_ans[data[2 * i] - 2] != 0:
                flag = 1
                break

            # B
            if B_ans[data[2 * i + 1]] == 3:
                flag = 2
                break
            elif B_ans[data[2 * i + 1]] != 0 and B_ans[data[2 * i + 1] - 1] != 0 and B_ans[data[2 * i + 1] + 1] != 0:
                flag = 2
                break
            elif B_ans[data[2 * i + 1]] != 0 and B_ans[data[2 * i + 1] + 1] != 0 and B_ans[data[2 * i + 1] + 2] != 0:
                flag = 2
                break
            elif B_ans[data[2 * i + 1]] != 0 and B_ans[data[2 * i + 1] - 1] != 0 and B_ans[data[2 * i + 1] - 2] != 0:
                flag = 2
                break

    print("#{} {}".format(test_case + 1, flag))
