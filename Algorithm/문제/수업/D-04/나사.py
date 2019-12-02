import sys
sys.stdin = open("나사_input.txt")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))

    for i in range(len(data)-1, 0, -1):     # 4 3 2 1
        for j in range(0, i):               # 4 3 2 1
            if data[j] > data[j+1]:         # 오름차순
                data[j], data[j+1] = data[j+1], data[j]
    print(data)
                #
                # for i in range(1, len(data)-1):
                #     x = ''
                #     if data[i-1] != data[i] and data[i] != data[i+1]:
                #         x = str(data[i])
    # print(x)
    #
    #
    #         #     print("#{} {}".format(tc+1, ans))
    # print(data)





# import sys
# sys.stdin = open("view_input.txt")
# T = 10
# for tc in range(10):
#     ans = 0
#     N = int(input())
#     data = list(map(int, input().split()))
#     for i in range(2,len(data)-1):
#         if data[i] > data[i-1] and data[i] > data[i-2] and data[i] > data[i+1] and data[i] > data[i+2]:
#             ans += data[i] - max(data[i-1], data[i-2], data[i+1], data[i+2])
#     print("#{} {}".format(tc+1, ans))