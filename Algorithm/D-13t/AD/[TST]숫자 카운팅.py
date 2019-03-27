import sys
sys.stdin = open("[TST]숫자 카운팅_input.txt", "r")

n = int(input())
narr = list(map(int, input().split()))
m = int(input())
marr = list(map(int, input().split()))
parr = [0]*(narr[-1]+1)

for i in narr:
    parr[i]+=1
for i in marr:
    if i > narr[-1]:
        print(0, end=" ")
    else:
        print(parr[i], end=" ")

#---------------------------------------------------------------------------------------


# 왼쪽 탐색
def lowerbound(s, e, data):
    sol = -1
    while s<=e:
        m = (s+e)//2
        if narr[m] == data:
            sol = m
            e = m-1
        elif narr[m] < data:
            s = m+1
        else:
            e = m-1

    return sol

# 오른쪽 탐색
def upperbound(s, e, data):
    sol = -1
    while s<=e:
        m = (s+e)//2
        if narr[m] == data:
            sol = m
            s = m+1
        elif narr[m] < data:
            e = m-1
        else:
            e = m-1
    return sol


narr.sort()
for i in range(m):
    a = lowerbound(0, n-1, marr[i])
    if a>=0:
        b = upperbound(a, n-1, marr[i])
        print(b-a+1, end=" ")
        # print(a)
    else:
        print(0, end=' ')

