import sys
sys.stdin = open("D4_15231_input.txt", "r")

'''
이진트리 깊이 30
갈 수 있는 길 29
n = 0~ 
[2^n, 2^(n+1) - 1]
'''

# 18090 // 100000 Runtime Error
arr = []
s, e = 1, 0
for i in range(30):
    e += s
    s *= 2
    arr.append([i, s // 2, (s // 2) + (s // 4), e])    # depth, startNum, middleNum, endNum

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())

    for i in arr:
        # N depth
        if i[1] <= N <= i[3]:
            NDepth = i[0]
            if i[1] <= N < i[2]:
                Nlr = 0
            else:
                Nlr = 1
        # start depth
        if i[1] <= M <= i[3]:
            startDepth = i[0]
            if i[1] <= M < i[2]:
                lr = 0
            else:
                lr = 1
    print("#{} {}".format(test_case + 1, NDepth + startDepth))