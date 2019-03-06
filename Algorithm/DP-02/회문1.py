def Xcount(data):
    global count, X, flag
    for i in range(X):
        for j in range(X-N+1):
            flag = 1
            for k in range(N//2):
                if data[i][j+k] != data[i][j+N-1-k]:
                    flag = 0
                    break
            if flag:
                count += 1

def Ycount(data):
    global count, X, flag
    for i in range(X):
        for j in range(X-N+1):
            flag = 1
            for k in range(N//2):
                if data[j+k][i] != data[j+N-1-k][i]:
                    flag = 0
                    break
            if flag:
                count += 1

import sys
sys.stdin = open("회문1_input.txt", "r")
for test_case in range(10):
    N = int(input())
    X= 8
    stack_a = []
    stack_b = []
    data = [input() for _ in range(X)]
    count = 0
    flag = 0
    Xcount(data)
    Ycount(data)
    print("#{} {}".format(test_case + 1, count))