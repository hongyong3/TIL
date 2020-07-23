import sys
sys.stdin = open("D5_10204_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = sorted([list(map(int, input().split())) for _ in range(N)], key = lambda x : (- x[0], - x[1]))
    ans = [data[i][0] if not i % 2 else - data[i][1] for i in range(N)]
    print("#{} {}".format(test_case + 1, sum(ans)))
    # print(ans)
    # sortedData = sorted(data, key = lambda x : (- x[0], - x[1]))
    # ans = 0
    # print(sortedData)
    # for i in range(N):
    #     if not i % 2:
    #         ans += sortedData[i][0]
    #     else:
    #         ans -= sortedData[i][1]
    # print("#{} {}".format(test_case + 1, ans1 - ans2))
    # print("#{} {}".format(test_case + 1, ans))