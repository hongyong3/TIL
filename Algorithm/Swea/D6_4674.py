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
num = [[0, 0]] * 2000
T = int(input())
for test_case in range(T):
    N = int(input()) + 1

    nam = N % 10
    mok = []
    for i in range(1, 19):
        temp = N // 10 ** i
        if temp:
            mok.append(temp)
        else:
            break
    print(mok)