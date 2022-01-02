import sys
sys.stdin = open("D2_4861_input.txt", "r")

# T = int(input())
# for test_case in range(T):
#     N, M = map(int, input().split())
#     data = [input() for _ in range(N)]
#     dataT = [''.join(x) for x in zip(*data)]
#     mat = ''
#     for x, y in zip(data, dataT):
#         i = 0
#         while i < N - M + 1:
#             if x[i: M + i] == x[i: M + i][:: - 1]:
#                 mat += x[i: M + i]
#                 break
#             if y[i: M + i] == y[i: M + i][:: - 1]:
#                 mat += y[i: M + i]
#                 break
#             i += 1
#         if mat:
#             print("#{} {}".format(test_case + 1, mat))
#             break

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    lst = [input() for i in range(N)]
    res = ''  # 회문 저장용
    ok = False  # 회문 찾았는지 확인용
    for i in range(N):  # 가로에서 회문이 있는지 확인
        for k in range(N - M + 1):
            front = []  # 회문 확인을 위해 문자 앞쪽 저장용
            rear = []  # 문자 뒤쪽 저장용
            mid = []
            for j in range(M):  # 회문 문자 수만큼 반복
                if M % 2 == 0:
                    if j < M // 2:
                        front.append(lst[i][j + k])  # 문자열의 앞쪽 반을 front에 저장
                    else:
                        rear.append(lst[i][j + k])  # 뒤쪽 반을 rear에 저장
                else:
                    if j < M // 2:
                        front.append(lst[i][j + k])
                    elif j > M // 2:
                        rear.append(lst[i][j + k])
                    else:
                        mid.append(lst[i][j + k])
            if front == rear[::-1]:  # 앞쪽 문자열과 뒤집은 뒤쪽 문자열이 같다면 res에 저장하고 ok = True
                if len(mid):
                    res = ''.join(front) + ''.join(mid) + ''.join(rear)
                    ok = True
                    break
                else:
                    res = ''.join(front) + ''.join(rear)
                    ok = True
                    break
        if ok == True:
            break
    if not ok:  # 가로에서 회문이 없을경우 세로 확인
        for i in range(N):
            for k in range(N - M + 1):  # 0 ~ 7
                front = []
                rear = []
                mid = []
                for j in range(M):
                    if M % 2 == 0:
                        if j < M // 2:
                            front.append(lst[j + k][i])
                        else:
                            rear.append(lst[j + k][i])
                    else:
                        if j < M // 2:
                            front.append(lst[j + k][i])
                        elif j > M // 2:
                            rear.append(lst[j + k][i])
                        else:
                            mid.append(lst[j + k][i])
                if front == rear[::-1]:
                    if len(mid):
                        res = ''.join(front) + ''.join(mid) + ''.join(rear)
                        ok = True
                        break
                    else:
                        res = ''.join(front) + ''.join(rear)
                        ok = True
                        break
            if ok == True:
                break
    if ok == True:
        print("#{0} {1}".format(test_case, res))
    else:
        print("없음")