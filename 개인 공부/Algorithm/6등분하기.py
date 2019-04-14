import sys
sys.stdin = open("6등분하기_input.txt", "r")
def comb(idx, count, L):
    if count == 3:
        k = []
        for idx in range(len(check)):
            if check[idx] == 1:
                k.append(L[idx])
        result_check.append(k[:])
        return`
    if idx >= 6:
        return
    check[idx] = 1
    comb(idx + 1, count + 1, L)
    check[idx] = 0
    comb(idx + 1, count, L)

def mycal(LS):
    n1 = LS[0]
    n2 = LS[1]
    n3 = LS[2]
    return abs(n1 - n2) + abs(n2 - n3) + abs(n3 - n1)

T = int(input())
for test_case in range(1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    s_data = []
    check = [0 for _ in range(6)]
    for Y in range(1, N):
        for X1 in range(1, M - 1):
            for X2 in range(X1 + 1, M):
                t1, t2, t3, t4, t5, t6 = 0, 0, 0, 0, 0, 0
                for y in range(Y):
                    for x in range(X1):
                        t1 += data[y][x]
                for y in range(Y):
                    for x in range(X1, X2):
                        t2 += data[y][x]
                for y in range(Y):
                    for x in range(X2, M):
                        t3 += data[y][x]
                for y in range(Y, N):
                    for x in range(X1):
                        t4 += data[y][x]
                for y in range(Y, N):
                    for x in range(X1, X2):
                        t5 += data[y][x]
                for y in range(Y, N):
                    for x in range(X2, M):
                        t6 += data[y][x]
                s_data.append([t1, t2, t3, t4, t5, t6])
    result_check = []
    for i in range(len(s_data)):
        comb(0, 0, s_data[i])
    result = []
    for i in result_check:
        result.append(mycal(i))
    print("#{} {}".format(test_case + 1, max(result)))