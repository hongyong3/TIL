import sys
sys.stdin = open("D3_1209_input.txt", "r")

for test_case in range(10):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    trans_data = [[0] * 100 for _ in range(100)]

    for i in range(len(data)):
        for j in range(len(data)):
            trans_data[j][i] = data[i][j]

    ans, ans1, ans2 = [], 0, 0
    for i in range(len(data)):
        ans.append(sum(data[i]))    # 가로
        ans.append(sum(trans_data[i]))  # 세로
        ans1 += data[i][i]          # 좌하향대각
        ans2 += trans_data[i][i]  #우상향대각
    ans.append(ans1), ans.append(ans2)
    print("#{} {}".format(test_case + 1, max(ans)))