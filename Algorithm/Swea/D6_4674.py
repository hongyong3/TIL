import sys
sys.stdin = open("D6_4674_input.txt", "r")

'''
0이 생성되는 조건 : 2 * 5가 있어야 한다.
즉, 
0 ~ 4 : 0이 짝수
5 ~ 9 : 0이 홀수
10 ~ 14 : 0이 짝수
15 ~ 19 : 0이 홀수
20 ~ 24 : 0이 짝수
25 ~ 29 : 0이 홀수

만약 100이면?
    1000?
'''

# T = int(input())
# for test_case in range(T):
#     N = int(input())
#
#     nam = N % 10
#     mok = []
#     for i in range(1, 19):
#         temp = N // 10 ** i
#         if temp:
#             mok.append(temp)
#         else:
#             break
#     print(mok)

num = [[0, 0]] * 27
T = int(input())
for test_case in range(T):
    N = int(input())
    N += 1
    num[0][0] = 1
    cnt, ans = 1, 0

    for i in range(1, 27):
        cnt *= 5
        if i % 2:
            num[i][0] = num[i - 1][0] * 5
            num[i][1] = num[i - 1][1] * 5
        else:
            num[i][0] = num[i - 1][0] * 3 + num[i - 1][1] * 2
            num[i][1] = num[i - 1][0] * 2 + num[i - 1][1] * 3
        if cnt > N:
            cnt //= 5
            k = i - 1
            break

    reverse = False
    while N > 0:
        for j in range(5):
            if cnt > N:
                k -= 1
                cnt //= 5
                break
            N -= cnt
            ans += num[k][reverse]
            if k % 2:
                if reverse == False:
                    reverse = True
                else:
                    reverse = False

    print(ans)