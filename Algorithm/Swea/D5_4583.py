import sys
sys.stdin = open("D5_4583_input.txt", "r")

# T = int(input())
# for test_case in range(T):
#     M, K = map(int, input().split())
#     num = ['0', '1', '2', '3', '4', '5', '6']
#     arr = ['0123456']
#     data = [list(map(int, input().split())) for _ in range(M)]
#
#     c = True
#     while c:
#         for a, b in data:
#             num[a - 1], num[b - 1] = num[b - 1], num[a - 1]
#             joinNum = ''.join(num)
#             if joinNum not in arr:  # testcase 1번이 반례.. 다시 짜자...
#                 arr.append(joinNum)
#             else:
#                 cycle = len(arr)
#                 c = False
#                 break
#     ans = arr[M] if M > K else arr[K % cycle]
#     print("#{} {}".format(test_case + 1, ans))

T = int(input())
for test_case in range(T):
    M, K = map(int, input().split())
    num = ['0', '1', '2', '3', '4', '5', '6']
    data = [list(map(int, input().split())) for _ in range(M)]

    cnt, chk = 0, True
    while chk:
        for i in range(K):
            num[data[cnt][0] - 1], num[data[cnt][1] - 1] = num[data[cnt][1] - 1], num[data[cnt][0] - 1]
            cnt += 1
            if cnt >= M:
                cnt = 0
                if num == ['0', '1', '2', '3', '4', '5', '6']:
                    K %= (i + 1)
                    break
        else:
            chk = False
    print("#{} {}".format(test_case + 1, ''.join(num)))